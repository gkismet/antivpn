# 🚀 AntiVPN - 一键自建高速抗封锁节点 (VLESS-Reality + BBR)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Ubuntu%20%7C%20Debian%20%7C%20CentOS%20%7C%20AlmaLinux-green.svg)]()
[![Protocol](https://img.shields.io/badge/Protocol-VLESS--Reality-orange.svg)]()
[![Optimization](https://img.shields.io/badge/Acceleration-Linux%20Kernel%20BBR-purple.svg)]()
[![YouTube Video](https://img.shields.io/badge/YouTube-完整实操视频教程-red?logo=youtube)](https://youtu.be/1YFYq-buko0)

> 专为 **外贸办公、科研检索、海外 AI 大模型开发（Antigravity、ChatGPT、Claude、Cursor）** 设计的轻量级自建节点工具。  
> **真正小白化**：免自购域名、免配 SSL 证书、无感 TLS 伪装、抗 GFW DPI 封锁，一键生成全平台可用配置！
> 
> 📺 **配套手把手视频教程**：[https://youtu.be/1YFYq-buko0](https://youtu.be/1YFYq-buko0)  
> 🌐 **图文教程网站**：[https://lab.gkismet.com/antivpn/](https://lab.gkismet.com/antivpn/)

---

## 🎁 第一步：准备一台 VPS（3 分钟选好）

自建独享节点最重要的一步是拥有一台干净、稳定的海外 VPS。我自己视频里用的是 **NovixLink 原生双 ISP 住宅 IP**：

### 👉 [点击前往 NovixLink 购买（支持支付宝 / 微信）](https://novixlink.com/aff.php?aff=580)

📊 **实时库存 + 三条线路详细对比**：<https://lab.gkismet.com/antivpn/plans.html>

**不知道选哪个？直接照抄：**

| 你的情况 | 推荐套餐 | 配置 | 月付价格 |
| :--- | :--- | :--- | :--- |
| ⭐ 现在就想用（有货） | **LAX-BGP Lite 轻量版**（CG 线路） | 1 核 / 768MB / 10GB SSD / 1Gbps / 每月 1000GB | **$5.99 CAD**（约 ¥30） |
| 大流量 / 多人共用（有货） | LAX-BGP Basic 基础版（CG 线路） | 1 核 / 1GB / 10GB SSD / 1.25Gbps / 每月 2000GB | $9.99 CAD（约 ¥50） |
| 人在中国大陆、看重晚高峰速度 | LAX-CUPN / CUPG Lite（NTT / GTT 线路） | 1 核 / 768MB / 10GB SSD / 100Mbps / 每月 500GB | $7.99 CAD（约 ¥40）· 目前售罄，可预订补货 |

> ⚠️ **CG 线路没有中国大陆线路优化**，大陆直连在晚高峰可能偏慢；NTT / GTT 线路回程走联通 9929 + 移动 CMIN2，但经常售罄。价格与库存为 2026-11-24 官网信息，以官网为准。

> 💡 系统选 **Debian 12 或 Ubuntu 22.04/24.04**，开机后用 SSH 登录，复制下方一行命令即可。

> 🌟 **为什么选【原生双 ISP 住宅 IP】而不是普通机房 VPS？**<br>
> 普通机房 VPS（数据中心 IP）在 OpenAI、Claude、Google 等平台的风控里更容易触发验证码、Access Denied 甚至封号。<br>
> 住宅 IP 在主流 IP 数据库中通常被识别为家庭宽带，风控友好度明显更高（实测截图见视频）。适合外贸、AI 开发与跨国办公。

> 📢 **推广说明**：上方 NovixLink 链接为推广链接，通过它购买我会获得一定返佣，你的价格不变。这是维护本项目和持续更新视频的主要动力，感谢支持 🙏

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
