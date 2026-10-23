# 🚀 AntiVPN - 一键自建高速抗封锁节点 (VLESS-Reality + BBR)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Ubuntu%20%7C%20Debian%20%7C%20CentOS%20%7C%20AlmaLinux-green.svg)]()
[![Protocol](https://img.shields.io/badge/Protocol-VLESS--Reality-orange.svg)]()
[![Optimization](https://img.shields.io/badge/Acceleration-Linux%20Kernel%20BBR-purple.svg)]()

> 专为 **外贸办公、科研检索、海外 AI 大模型开发（Antigravity、ChatGPT、Claude、Cursor）** 设计的轻量级自建节点工具。  
> **真正小白化**：免自购域名、免配 SSL 证书、无感 TLS 伪装、抗 GFW DPI 封锁，一键生成全平台可用配置！

---

## 🎁 特惠 VPS 推荐通道（支持支付宝 / 微信）

自建独享节点最重要的一步是拥有一台干净、稳定的海外 VPS 服务器。推荐使用以下高性价比通道：

| 云厂商 | 特点与推荐机房 | 专属优惠通道 |
| :--- | :--- | :--- |
| **NovixLink (推荐首选)** | **原生双ISP 纯净住宅IP**（通过所有欺诈库检测，被识别为美国家庭宽带）、**中国大陆优化高速直连**、流媒体与海外 AI (ChatGPT/Claude/Antigravity) 100% 满血解锁，告别封号与拦截 | [👉 点击前往 NovixLink 优惠购买](https://novixlink.com/aff.php?aff=580) |

> 🌟 **为什么必须选择【原生双ISP住宅IP】？**  
> 普通机房 VPS（数据中心 IP）早已被 OpenAI、Claude、Google、TikTok 等海外平台的风控系统列入黑名单，极易触发验证码、Access Denied 甚至封号！  
> **NovixLink 的原生双 ISP 住宅 IP** 在各大 IP 数据库中均显示为真实美国家庭住宅宽带，配合中国优化网络直连，兼具**极低延迟**与**最高等级安全信用度**，是外贸、AI 开发与跨国办公的绝对首选。

---

## ⚡ 极速一键安装

通过 SSH 连接到你的 VPS 之后，只需复制并粘贴以下整行命令运行：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/gkismet/antivpn/main/install.sh)
```
*(注：如果使用自建仓库，请将上方链接中的用户名替换为你的 GitHub 用户名)*

### 脚本全自动为你完成：
1. **自动开启 Linux 原生 BBR 拥塞控制**（成倍降低高延迟长距离跨国传输的丢包重传）。
2. **自动拉取官方最新原生 Xray-core** 并部署 **VLESS + XTLS-Reality**。
3. **真实合法大厂 TLS 流量伪装**（借用苹果/微软官方 SNI，GFW 无法通过特征识别）。
4. **全自动配置防火墙端口放行**。
5. **在终端一键打印**：
   - 📋 客户端通用导入链接 (`vless://...`)
   - 📱 手机即时扫码二维码 (ASCII QR Code)
   - 💻 Windows / macOS (v2rayN) 一键秒级导入指引
6. **安装系统全局指令**：后续在 VPS 任何位置输入 `vpn` 即可随时重新调出菜单。

---

## 📱 全平台客户端连接推荐

为了让 **Antigravity IDE、终端命令、Git、浏览器、Python** 全局生效，建议在客户端中开启 **TUN 虚拟网卡模式**：

| 平台 | 推荐客户端 | 下载地址 | 使用说明 |
| :--- | :--- | :--- | :--- |
| **Windows** | **v2rayN** | [GitHub Releases](https://github.com/2dust/v2rayN/releases) | 复制上方 `vless://` 链接在主界面按 `Ctrl+V` 一键导入，底部勾选 **【启用Tun模式】** 与 **【自动配置系统代理】** |
| **macOS** | **v2rayN (Mac版)** / **Sing-box** | [GitHub Releases](https://github.com/2dust/v2rayN/releases) | 复制链接导入节点，开启 **【Tun 模式】**（弹窗允许安装网卡驱动） |
| **iOS** | **Shadowrocket (小火箭)** / **Sing-box** | App Store (海外区) | 手机打开软件，直接扫描脚本生成的二维码即可秒连 |
| **Android** | **v2rayNG** | [GitHub Releases](https://github.com/2dust/v2rayNG/releases) | 点击右上角 `+` 扫描终端二维码，右下角开启连接 |

---

## 🛠️ VPS 常用管理命令

安装完成后，在 VPS 终端直接执行：
```bash
vpn
```
即可调出交互式管理菜单：
- 查看当前节点链接、二维码与客户端导入指引
- 重启 / 检查节点服务状态
- 单独检查 BBR 拥塞控制
- 一键彻底卸载清理

---

## ⚖️ 免责声明 (Disclaimer)

本项目仅用于个人学习、开发测试及合法学术科研网络加速用途。请遵守当地法律法规，严禁利用本项目从事任何违法违规网络活动。
