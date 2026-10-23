#!/usr/bin/env bash
# ==============================================================================
# 项目名称: AntiVPN - 一键自建高速抗封锁节点 (专为 AI 工具/外网全平台优化)
# 适用系统: Ubuntu / Debian / CentOS / AlmaLinux / Rocky
# 支持协议: VLESS + XTLS-Reality (免域名、免证书、真实 TLS 伪装、抗 GFW DPI 封锁)
# ==============================================================================

# -------------- [在此处修改你的推广与频道信息] --------------
AUTHOR_NAME="我的科技频道"
AFF_VPS_NAME="NovixLink 原生双ISP住宅IP (中国优化高速云)"
AFF_VPS_URL="https://novixlink.com/aff.php?aff=580"  # 👈 用户的专属 VPS 返佣推广链接
YOUTUBE_CHANNEL="https://youtube.com/@yourchannel"  # 👈 你的 YouTube 频道链接（可在开播后替换）
TG_GROUP="https://t.me/yourgroup"                  # 👈 你的 TG 交流群（可选）
# -------------------------------------------------------------

# 字体颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
PLAIN='\033[0m'
BOLD='\033[1m'

CONFIG_DIR="/usr/local/etc/antivpn"
CONFIG_FILE="${CONFIG_DIR}/config.json"
INFO_FILE="${CONFIG_DIR}/node_info.env"

# 检查 root 权限
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}[错误]${PLAIN} 此脚本必须以 root 权限运行！请使用 'sudo -i' 或以 root 用户登录。"
        exit 1
    fi
}

# 打印横幅与推广信息
print_banner() {
    clear
    echo -e "${CYAN}${BOLD}"
    cat << "EOF"
    ___          __  _ _    ______  _   __
   /   |  ____  / /_(_) |  / / __ \/ | / /
  / /| | / __ \/ __/ / / | / / /_/ /  |/ / 
 / ___ |/ / / / /_/ / /| |/ / ____/ /|  /  
/_/  |_/_/ /_/\__/_/_/ |___/_/   /_/ |_/   
EOF
    echo -e "${PLAIN}"
    echo -e "${BOLD}${PURPLE}==================================================================${PLAIN}"
    echo -e " 🚀 ${GREEN}${BOLD}AntiVPN 极速抗封锁节点一键部署工具${PLAIN} (VLESS-Reality + BBR)"
    echo -e " 👨‍💻 制作维护: ${CYAN}${AUTHOR_NAME}${PLAIN}"
    echo -e " 📺 YouTube:  ${BLUE}${YOUTUBE_CHANNEL}${PLAIN}"
    echo -e " 🎁 特惠 VPS: ${YELLOW}${AFF_VPS_NAME}${PLAIN}"
    echo -e " 🔗 购买链接: ${YELLOW}${AFF_VPS_URL}${PLAIN}"
    echo -e "${BOLD}${PURPLE}==================================================================${PLAIN}"
    echo ""
}

# 检测系统架构与包管理器
check_os() {
    if [[ -f /etc/os-release ]]; then
        source /etc/os-release
        OS_ID=$ID
    else
        echo -e "${RED}[错误]${PLAIN} 无法识别当前操作系统！"
        exit 1
    fi

    ARCH=$(uname -m)
    case "$ARCH" in
        x86_64 | amd64) XRAY_ARCH="64" ;;
        aarch64 | arm64) XRAY_ARCH="arm64-v8a" ;;
        *)
            echo -e "${RED}[错误]${PLAIN} 暂不支持的架构: $ARCH"
            exit 1
            ;;
    esac
}

# 开启 BBR
enable_bbr() {
    echo -e "${BLUE}[1/5] 检查并开启 Linux 原生 BBR 拥塞控制...${PLAIN}"
    if sysctl net.ipv4.tcp_congestion_control | grep -q bbr; then
        echo -e "${GREEN}✓ BBR 加速已在运行中，无需重复开启。${PLAIN}"
    else
        echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
        echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
        sysctl -p > /dev/null 2>&1
        if sysctl net.ipv4.tcp_congestion_control | grep -q bbr; then
            echo -e "${GREEN}✓ BBR 拥塞控制开启成功！已极大降低跨国长距离传输丢包率。${PLAIN}"
        else
            echo -e "${YELLOW}! 开启 BBR 失败，可能受限于当前 VPS 虚拟化类型 (如 OpenVZ/LXC)。${PLAIN}"
        fi
    fi
}

# 安装基础依赖
install_dependencies() {
    echo -e "${BLUE}[2/5] 正在安装系统基础工具包...${PLAIN}"
    if [[ "$OS_ID" == "ubuntu" || "$OS_ID" == "debian" ]]; then
        apt-get update -y -q > /dev/null 2>&1
        apt-get install -y -q curl wget tar jq qrencode openssl socat ca-certificates > /dev/null 2>&1
    elif [[ "$OS_ID" == "centos" || "$OS_ID" == "almalinux" || "$OS_ID" == "rocky" ]]; then
        yum install -y -q epel-release > /dev/null 2>&1
        yum install -y -q curl wget tar jq qrencode openssl socat ca-certificates > /dev/null 2>&1
    fi
    echo -e "${GREEN}✓ 基础工具包就绪。${PLAIN}"
}

# 获取 VPS 公网 IP
get_public_ip() {
    SERVER_IP=$(curl -s4m 5 https://api.ipify.org || curl -s4m 5 https://ip.sb || curl -s4m 5 https://icanhazip.com)
    if [[ -z "$SERVER_IP" ]]; then
        echo -e "${YELLOW}未能自动探测到 IPv4，请输入你的 VPS 公网 IP:${PLAIN}"
        read -rp "IP: " SERVER_IP
    fi
}

# 安装并配置 Xray 核心 (原生 VLESS-Reality)
install_xray_reality() {
    echo -e "${BLUE}[3/5] 正在部署最新 Xray-core 原生网络引擎...${PLAIN}"
    
    mkdir -p "$CONFIG_DIR"
    mkdir -p /usr/local/bin
    
    # 获取 Xray 官方最新版本
    LATEST_VER=$(curl -s https://api.github.com/repos/XTLS/Xray-core/releases/latest | jq -r .tag_name)
    [[ -z "$LATEST_VER" ]] && LATEST_VER="v26.10.10"
    
    TMP_ZIP="/tmp/xray.zip"
    DOWNLOAD_URL="https://github.com/XTLS/Xray-core/releases/download/${LATEST_VER}/Xray-linux-${XRAY_ARCH}.zip"
    
    curl -sL "$DOWNLOAD_URL" -o "$TMP_ZIP"
    if [[ ! -s "$TMP_ZIP" ]]; then
        echo -e "${RED}[错误]${PLAIN} 下载 Xray 核心失败，请检查 VPS 外网连通性！"
        exit 1
    fi
    
    unzip -q -o "$TMP_ZIP" -d /usr/local/bin/ xray
    chmod +x /usr/local/bin/xray
    rm -f "$TMP_ZIP"
    
    echo -e "${BLUE}[4/5] 正在生成专属 TLS-Reality 加密密钥对与配置...${PLAIN}"
    
    # 自动生成密钥与 UUID
    KEYS=$(/usr/local/bin/xray x25519)
    PRIVATE_KEY=$(echo "$KEYS" | grep -i "PrivateKey" | awk '{print $2}')
    PUBLIC_KEY=$(echo "$KEYS" | grep -i "Password" | awk '{print $3}')
    UUID=$(cat /proc/sys/kernel/random/uuid)
    SHORT_ID=$(openssl rand -hex 4)
    
    # 随机选择 10000-60000 间的高位安全端口
    LISTEN_PORT=$(shuf -i 15000-55000 -n 1)
    
    # 伪装目标 SNI (使用全球高信任度合法域名)
    DEST_SNI="gateway.icloud.com"
    DEST_TARGET="gateway.icloud.com:443"
    
    # 写入 Xray 服务端配置
    cat << EOF > "$CONFIG_FILE"
{
  "log": {
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "port": ${LISTEN_PORT},
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "id": "${UUID}",
            "flow": "xtls-rprx-vision"
          }
        ],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "show": false,
          "dest": "${DEST_TARGET}",
          "xver": 0,
          "serverNames": [
            "${DEST_SNI}"
          ],
          "privateKey": "${PRIVATE_KEY}",
          "shortIds": [
            "${SHORT_ID}"
          ]
        }
      },
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls", "quic"]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "tag": "direct"
    },
    {
      "protocol": "blackhole",
      "tag": "blocked"
    }
  ]
}
EOF

    # 配置 systemd 守护进程
    cat << EOF > /etc/systemd/system/antivpn.service
[Unit]
Description=AntiVPN Xray-core Service
After=network.target

[Service]
ExecStart=/usr/local/bin/xray run -config ${CONFIG_FILE}
Restart=always
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    systemctl enable antivpn > /dev/null 2>&1
    systemctl restart antivpn

    # 放行系统防火墙端口
    if command -v ufw > /dev/null 2>&1; then
        ufw allow ${LISTEN_PORT}/tcp > /dev/null 2>&1
    fi
    if command -v iptables > /dev/null 2>&1; then
        iptables -I INPUT -p tcp --dport ${LISTEN_PORT} -j ACCEPT > /dev/null 2>&1
    fi
    
    # 生成 VLESS 链接
    VLESS_URL="vless://${UUID}@${SERVER_IP}:${LISTEN_PORT}?type=tcp&security=reality&pbk=${PUBLIC_KEY}&fp=chrome&sni=${DEST_SNI}&sid=${SHORT_ID}&spx=%2F&flow=xtls-rprx-vision#AntiVPN-${SERVER_IP}"
    
    # 保存配置信息
    cat << EOF > "$INFO_FILE"
SERVER_IP="${SERVER_IP}"
LISTEN_PORT="${LISTEN_PORT}"
UUID="${UUID}"
PUBLIC_KEY="${PUBLIC_KEY}"
PRIVATE_KEY="${PRIVATE_KEY}"
SHORT_ID="${SHORT_ID}"
DEST_SNI="${DEST_SNI}"
VLESS_URL="${VLESS_URL}"
EOF

    # 安装全局快捷指令 'vpn'
    cat << 'EOF' > /usr/local/bin/vpn
#!/usr/bin/env bash
bash /usr/local/etc/antivpn/install.sh
EOF
    chmod +x /usr/local/bin/vpn
    cp "$0" /usr/local/etc/antivpn/install.sh 2>/dev/null || true

    echo -e "${GREEN}✓ Xray Reality 服务启动成功！${PLAIN}"
}

# 显示最终节点信息与 Clash 配置
show_node_info() {
    if [[ ! -f "$INFO_FILE" ]]; then
        echo -e "${RED}[错误]${PLAIN} 未检测到已安装的节点配置，请先运行安装！"
        return
    fi
    
    source "$INFO_FILE"
    
    echo ""
    echo -e "${GREEN}${BOLD}══════════════════════════════════════════════════════════════════${PLAIN}"
    echo -e " 🎉 ${GREEN}${BOLD}恭喜！AntiVPN 专属高速节点已部署成功！${PLAIN}"
    echo -e "${GREEN}${BOLD}══════════════════════════════════════════════════════════════════${PLAIN}"
    echo -e " 📡 ${BOLD}节点名称:${PLAIN} AntiVPN-${SERVER_IP}"
    echo -e " 🌐 ${BOLD}服务器 IP:${PLAIN} ${CYAN}${SERVER_IP}${PLAIN}"
    echo -e " 🚪 ${BOLD}连接端口:${PLAIN} ${CYAN}${LISTEN_PORT}${PLAIN}"
    echo -e " 🛡️  ${BOLD}加密协议:${PLAIN} VLESS + XTLS-Reality (Chrome 浏览器指纹)"
    echo -e " 🎭 ${BOLD}伪装域名:${PLAIN} ${DEST_SNI}"
    echo -e ""
    echo -e " 📋 ${YELLOW}${BOLD}【节点一键导入链接 (VLESS)】${PLAIN}"
    echo -e " 复制下方单行链接并在客户端点击【从剪贴板导入】:"
    echo -e "${CYAN}${VLESS_URL}${PLAIN}"
    echo ""
    echo -e " 📱 ${YELLOW}${BOLD}【手机扫码一键导入 (iPhone小火箭 / 安卓)】${PLAIN}:"
    qrencode -t UTF8 "$VLESS_URL"
    echo ""
    echo -e "${PURPLE}${BOLD}──────────────────────────────────────────────────────────────────${PLAIN}"
    echo -e " 💻 ${BOLD}【Windows / macOS 推荐客户端 - v2rayN】${PLAIN}:"
    echo -e " 1. 下载打开 v2rayN: ${CYAN}https://github.com/2dust/v2rayN${PLAIN}"
    echo -e " 2. 复制上方 ${CYAN}vless://${PLAIN} 链接，在 v2rayN 界面按 ${YELLOW}Ctrl+V${PLAIN} 即可秒级导入！"
    echo -e " 3. 底部勾选 ${GREEN}【启用Tun模式】${PLAIN} 与 ${GREEN}【自动配置系统代理】${PLAIN} 即可全系统加速。"
    echo -e "${PURPLE}${BOLD}──────────────────────────────────────────────────────────────────${PLAIN}"
    echo -e " 💡 ${BOLD}提示:${PLAIN} 随时输入 ${GREEN}${BOLD}vpn${PLAIN} 命令即可重新调出此菜单与二维码。"
    echo -e " 🎁 ${BOLD}高性价比 VPS 购买推荐:${PLAIN} ${YELLOW}${AFF_VPS_URL}${PLAIN}"
    echo -e " 📺 ${BOLD}视频教程 & 常见问题:${PLAIN} ${BLUE}${YOUTUBE_CHANNEL}${PLAIN}"
    echo -e "${GREEN}${BOLD}══════════════════════════════════════════════════════════════════${PLAIN}"
    echo ""
}

# 卸载清理
uninstall_all() {
    echo -e "${YELLOW}确定要完全卸载 AntiVPN 及其节点服务吗？[y/N]:${PLAIN} "
    read -rp "" confirm
    if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
        systemctl stop antivpn > /dev/null 2>&1
        systemctl disable antivpn > /dev/null 2>&1
        rm -f /etc/systemd/system/antivpn.service
        systemctl daemon-reload
        rm -rf "$CONFIG_DIR"
        rm -f /usr/local/bin/vpn
        rm -f /usr/local/bin/xray
        echo -e "${GREEN}✓ AntiVPN 已彻底卸载清理干净！${PLAIN}"
    else
        echo -e "${BLUE}已取消卸载。${PLAIN}"
    fi
}

# 主菜单
main_menu() {
    print_banner
    echo -e " ${BOLD}请选择操作:${PLAIN}"
    echo -e "  ${GREEN}1.${PLAIN} 一键极速部署 VLESS-Reality 节点 ${GREEN}(新手推荐、无感防封)${PLAIN}"
    echo -e "  ${GREEN}2.${PLAIN} 查看当前节点链接、二维码与客户端配置"
    echo -e "  ${GREEN}3.${PLAIN} 单独检查并开启 BBR 加速"
    echo -e "  ${GREEN}4.${PLAIN} 重启 AntiVPN 核心服务"
    echo -e "  ${RED}5.${PLAIN} 彻底卸载 AntiVPN"
    echo -e "  ${PLAIN}0.${PLAIN} 退出"
    echo ""
    read -rp "请输入数字 [0-5]: " choice
    case "$choice" in
        1)
            enable_bbr
            install_dependencies
            get_public_ip
            install_xray_reality
            show_node_info
            ;;
        2)
            show_node_info
            ;;
        3)
            enable_bbr
            ;;
        4)
            systemctl restart antivpn
            echo -e "${GREEN}✓ AntiVPN 核心服务已重启！${PLAIN}"
            ;;
        5)
            uninstall_all
            ;;
        0)
            exit 0
            ;;
        *)
            echo -e "${RED}[错误] 请输入有效选项！${PLAIN}"
            ;;
    esac
}

check_root
check_os
main_menu
