import os
import subprocess
import json
from PIL import Image, ImageDraw, ImageFont

WORK_DIR = "/Users/canyu/Desktop/gemini/vpn"
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"

scenes = [
    {
        "id": 1,
        "title": "30秒零基础自建专属抗封锁节点",
        "subtitle": "专为 AI 开发与全平台设计 | VLESS-Reality + BBR 极速加速",
        "text": "你是不是也经常遇到这种情况：辛辛苦苦花钱买的机场节点，动不动就断线、跑路？特别是想用 ChatGPT、Claude，或者像 Antigravity 这种 AI 工具写代码的时候，动不动就提示 IP 被拦截、甚至直接封号？想自己搭建吧，一搜教程又是买域名、配证书，还有一堆看不懂的报错直接劝退？今天这期视频，我教大家用最便宜的一顿外卖钱，通过我们开源的极速脚本：真正做到零基础、不需要买域名、不需要懂任何代码！只需要在终端复制粘贴一行命令，30秒搭好属于你自己的独享抗封锁专线！无论是 Windows、Mac 还是手机，全平台秒开 4K！话不多说，我们直接上实操！",
        "bg_img": os.path.join(WORK_DIR, "youtube_cover.jpg"),
        "step_tag": "🔥 2026 最新极速自建方案"
    },
    {
        "id": 2,
        "title": "步骤一：选择 NovixLink 原生双ISP住宅IP云服务器",
        "subtitle": "中国大陆优化直连 | 纯正美国家庭宽带 | 彻底告别 ChatGPT/TikTok 封号",
        "text": "自建节点最关键的一步，就是必须拥有一台干净、稳定、没有被滥用的海外服务器。为什么很多人自己搭了节点，用 ChatGPT、Claude 或者写代码还是动不动提示 Access Denied 甚至封号？因为普通机房 IP 早被各大平台的风控系统拉黑了！这里我强烈推荐大家使用我放在视频下方置顶链接中的 NovixLink 云服务器。它最大的核心王炸优势，就是它提供的是原生双 ISP 住宅 IP！在 IP 数据库里直接被识别为纯正的美国家庭宽带，欺诈值极低，对 OpenAI、Claude、TikTok、海外流媒体 100% 满血解锁，彻底告别封号与拦截！而且它专门做了中国大陆优化的高速直连网络，延迟超低、速度飞快！免去繁琐实名，价格非常亲民，还支持我们常用的快捷支付，即买即用！下单之后，系统大概一分钟就会把服务器的 IP 和密码发到你的后台。",
        "bg_img": os.path.join(WORK_DIR, "scene_novixlink.jpg"),
        "step_tag": "STEP 1: 原生双ISP住宅IP选购"
    },
    {
        "id": 3,
        "title": "步骤二：一键 SSH 连入云服务器",
        "subtitle": "无需任何运维基础，打开系统自带终端即可",
        "text": "拿到服务器之后，很多新手看到命令行就觉得头大。不用怕，这一步真的超级简单！无论你是 Windows 还是苹果 Mac，直接打开系统自带的终端或者 PowerShell。输入 ssh root 艾特你的服务器 IP，按下回车。接着把后台的密码复制粘贴进去，注意输密码看不见字符，直接回车就行！只要看到屏幕上跳出欢迎字符，就代表你已经成功连上这台美国服务器了！",
        "bg_img": None,
        "step_tag": "STEP 2: 终端 SSH 登录演示"
    },
    {
        "id": 4,
        "title": "步骤三：复制运行开源一键安装脚本",
        "subtitle": "bash <(curl -fsSL https://raw.githubusercontent.com/gkismet/antivpn/main/install.sh)",
        "text": "接下来就是见证奇迹的时刻！你完全不需要手动去敲那些复杂的配置命令。直接把我放在视频下方置顶评论里的这一行开源脚本代码：完整复制下来，直接粘贴到终端里，按下回车！你看，脚本会自动帮你检测系统，自动开启 Linux 原生 BBR 拥塞控制，自动拉取最新的 Xray 核心，配置好防封锁能力最强的 VLESS-Reality 协议！整个过程没有任何复杂提问，一路全自动跑完！看！前后不过 30 秒，屏幕上就已经把属于你的专属节点链接和大尺寸二维码全打印出来了！",
        "bg_img": None,
        "step_tag": "STEP 3: 30秒自动化部署全过程"
    },
    {
        "id": 5,
        "title": "步骤四：客户端一键导入 (v2rayN / 手机扫码)",
        "subtitle": "电脑端按 Ctrl+V 秒级导入 | 开启 TUN 模式让 Antigravity 全局生效",
        "text": "节点生成好之后，怎么在电脑和手机上用呢？更加简单！电脑端我推荐大家使用开源免费的 v2rayN。只要把终端里这一整行以 vless 开头的链接复制下来，打开 v2rayN 主界面，按一下键盘上的 Ctrl + V，节点就直接秒级导入进来了！这里有一个最核心的关键设置：导入之后，一定要在软件底部把【启用 Tun 模式】和【自动配置系统代理】勾选上！开启 Tun 模式之后，包括你的终端命令、Git、以及像 Antigravity、Cursor、ChatGPT 桌面版，全电脑的所有流量全都会无缝自动走专线加速，你再也不用手动去配什么烦人的本地端口了！如果是手机端，直接打开小火箭或者 v2rayNG，扫描屏幕上的二维码即可一键连接！",
        "bg_img": None,
        "step_tag": "STEP 4: 全平台客户端连接实操"
    },
    {
        "id": 6,
        "title": "实测体验：YouTube 4K 秒开 & AI 极速对话",
        "subtitle": "NovixLink 购买链接与一键脚本见置顶评论与视频描述栏",
        "text": "我们现在来看一下实际效果：随便点开一段 YouTube 上的 4K 60 帧视频，大家看，进度条直接秒缓冲，随便拖拽毫无卡顿！再切到开发环境，用它跑 Antigravity 或者 ChatGPT 长文本对话，丝滑顺畅，完全没有断流和掉线的问题，稳定度拉满！本期视频用到的 NovixLink 特惠 VPS 购买通道，以及一键开源安装脚本，我都已经整理好放在了置顶评论和视频描述栏里。如果这期视频帮到了你，请一定帮我点赞、收藏、订阅频道并打开小铃铛！感谢大家收看，我们下期视频不见不散！",
        "bg_img": os.path.join(WORK_DIR, "scene_speedtest.jpg"),
        "step_tag": "STEP 5: 测速验证与体验总结"
    }
]

print(">>> [1/4] Generating AI Audio Narrations...")
os.makedirs(f"{WORK_DIR}/video_build", exist_ok=True)

for sc in scenes:
    idx = sc["id"]
    aiff_path = f"{WORK_DIR}/video_build/audio_{idx}.aiff"
    mp3_path = f"{WORK_DIR}/video_build/audio_{idx}.mp3"
    
    subprocess.run(["say", "-v", "Tingting", "-o", aiff_path, sc["text"]], check=True)
    subprocess.run(["ffmpeg", "-y", "-i", aiff_path, "-b:a", "192k", mp3_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", mp3_path]
    probe_res = subprocess.check_output(probe_cmd).decode("utf-8")
    dur = float(json.loads(probe_res)["format"]["duration"])
    sc["duration"] = dur + 1.0
    print(f"Scene {idx} Audio Duration: {dur:.2f}s (Padded: {sc['duration']:.2f}s)")

print("\n>>> [2/4] Rendering 1080P Visual Cards...")

font_tag = ImageFont.truetype(FONT_PATH, 32)
font_title = ImageFont.truetype(FONT_PATH, 54)
font_sub = ImageFont.truetype(FONT_PATH, 34)
font_body = ImageFont.truetype(FONT_PATH, 28)

for sc in scenes:
    idx = sc["id"]
    frame_path = f"{WORK_DIR}/video_build/frame_{idx}.png"
    
    if sc["bg_img"] and os.path.exists(sc["bg_img"]):
        base = Image.open(sc["bg_img"]).convert("RGBA").resize((1920, 1080))
        overlay = Image.new("RGBA", (1920, 1080), (10, 14, 26, 185))
        img = Image.alpha_composite(base, overlay)
    else:
        img = Image.new("RGBA", (1920, 1080), (12, 17, 32, 255))
        draw_tmp = ImageDraw.Draw(img)
        for y in range(0, 1080, 80):
            draw_tmp.line([(0, y), (1920, y)], fill=(24, 34, 60, 120), width=1)
        for x in range(0, 1920, 80):
            draw_tmp.line([(x, 0), (x, 1080)], fill=(24, 34, 60, 120), width=1)

    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([(100, 70), (580, 130)], radius=12, fill=(28, 44, 84, 230), outline=(0, 210, 255, 200), width=2)
    draw.text((125, 83), sc["step_tag"], font=font_tag, fill=(0, 230, 255))
    
    draw.text((100, 170), sc["title"], font=font_title, fill=(255, 255, 255))
    draw.text((100, 250), sc["subtitle"], font=font_sub, fill=(120, 220, 255))
    
    draw.rounded_rectangle([(100, 330), (1820, 960)], radius=20, fill=(16, 23, 44, 235), outline=(50, 70, 120, 180), width=2)
    
    draw.ellipse([(140, 365), (160, 385)], fill=(255, 95, 86))
    draw.ellipse([(175, 365), (195, 385)], fill=(255, 189, 46))
    draw.ellipse([(210, 365), (230, 385)], fill=(39, 201, 63))
    
    if idx == 2: # NovixLink Dual ISP Highlight
        draw.text((140, 420), "🌟 为什么必须选择【NovixLink 原生双ISP住宅IP】？", font=font_title, fill=(255, 215, 0))
        lines = [
            "• 原生双ISP住宅IP：在各大IP库中被识别为纯正美国家庭宽带，欺诈评分极低",
            "• 彻底解决封号：ChatGPT / Claude / TikTok / 奈飞 100% 满血解锁，绝非易风控机房IP",
            "• 中国大陆优化高速网络：超低跨国直连延迟，长连接流式AI生成不中断",
            "• 极速开通：免繁琐实名认证，支持快捷支付，即买即用",
            "👉 专属特惠购买通道：https://novixlink.com/aff.php?aff=580"
        ]
        for l_idx, line in enumerate(lines):
            fill_c = (0, 255, 220) if l_idx == 4 else (190, 220, 255)
            draw.text((140, 510 + l_idx * 75), line, font=font_sub, fill=fill_c)
            
    elif idx == 3: # SSH Demo
        draw.text((140, 430), "# 打开 macOS 终端 或 Windows PowerShell", font=font_body, fill=(110, 130, 170))
        draw.text((140, 480), "$ ssh root@192.220.113.11", font=font_title, fill=(0, 255, 180))
        draw.text((140, 570), "root@192.220.113.11's password: ••••••••••••", font=font_sub, fill=(255, 255, 255))
        draw.text((140, 640), "Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 7.0.0-34-generic x86_64)", font=font_body, fill=(140, 160, 200))
        draw.text((140, 700), "root@VM-a7PfLoNnEM:~# [成功连接！准备运行一键脚本]", font=font_sub, fill=(0, 230, 255))
        
    elif idx == 4: # Script Run
        draw.text((140, 420), "# 复制并在 VPS 终端粘贴运行一键开源部署脚本:", font=font_body, fill=(110, 130, 170))
        draw.text((140, 470), "bash <(curl -fsSL https://raw.githubusercontent.com/gkismet/antivpn/main/install.sh)", font=font_sub, fill=(255, 215, 0))
        draw.text((140, 560), ">>> 自动开启 Linux 原生 BBR 拥塞控制算法... [OK]", font=font_body, fill=(0, 255, 140))
        draw.text((140, 610), ">>> 部署最新 Xray-core 原生网络引擎并配置 VLESS-Reality... [OK]", font=font_body, fill=(0, 255, 140))
        draw.text((140, 660), ">>> 自动生成客户端节点专属配置与大尺寸终端二维码... [OK]", font=font_body, fill=(0, 255, 140))
        draw.text((140, 720), "🎉 恭喜！专属高速节点已部署成功，耗时仅 30 秒！", font=font_title, fill=(0, 255, 220))
        draw.text((140, 810), "特惠 VPS 购买链接: https://novixlink.com/aff.php?aff=580", font=font_sub, fill=(255, 190, 40))
        
    elif idx == 5: # v2rayN Client
        draw.text((140, 420), "💻 电脑端推荐客户端：v2rayN (Windows / macOS)", font=font_title, fill=(255, 255, 255))
        draw.text((140, 520), "1. 复制终端生成的 vless:// 节点链接", font=font_sub, fill=(180, 210, 255))
        draw.text((140, 590), "2. 打开 v2rayN 软件主界面，按下键盘快捷键 Ctrl + V（自动秒级导入）", font=font_sub, fill=(0, 255, 180))
        draw.text((140, 660), "3. 关键一步：勾选底部【启用Tun模式】与【自动配置系统代理】", font=font_sub, fill=(255, 215, 0))
        draw.text((140, 730), "   👉 开启后全电脑网络（浏览器、Git、Antigravity、ChatGPT）自动全加速！", font=font_body, fill=(130, 240, 255))
        draw.text((140, 810), "📱 手机端：Shadowrocket (小火箭) 或 v2rayNG 扫描终端二维码即可秒连！", font=font_sub, fill=(255, 140, 200))
        
    else: # Explanatory Cards
        draw.text((140, 450), "核心亮点解析:", font=font_title, fill=(255, 255, 255))
        lines = [
            "• 真正零门槛：无需繁琐运维，30 秒自动化搞定",
            "• 极强抗封锁：VLESS-Reality 真实大厂 TLS 伪装，远离封号掉线",
            "• 原生双ISP住宅IP：解锁 ChatGPT / Claude / TikTok / 奈飞",
            "• 中国大陆优化直连：BBR 原生加速，为海外 AI 大模型生成深度调优"
        ]
        for l_idx, line in enumerate(lines):
            draw.text((140, 560 + l_idx * 75), line, font=font_sub, fill=(190, 220, 255))

    img.convert("RGB").save(frame_path, "PNG")
    print(f"Rendered Frame {idx} -> {frame_path}")

print("\n>>> [3/4] Encoding Video Scenes...")
scene_vids = []

for sc in scenes:
    idx = sc["id"]
    frame_path = f"{WORK_DIR}/video_build/frame_{idx}.png"
    mp3_path = f"{WORK_DIR}/video_build/audio_{idx}.mp3"
    vid_path = f"{WORK_DIR}/video_build/scene_{idx}.mp4"
    dur = sc["duration"]
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", frame_path,
        "-i", mp3_path,
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-t", str(dur),
        "-vf", "scale=1920:1080",
        vid_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    scene_vids.append(vid_path)
    print(f"Encoded Scene {idx} Video: {vid_path}")

print("\n>>> [4/4] Concatenating Full 1080P YouTube Video...")
concat_list_path = f"{WORK_DIR}/video_build/concat_list.txt"
with open(concat_list_path, "w") as f:
    for v in scene_vids:
        f.write(f"file '{v}'\n")

final_output = f"{WORK_DIR}/antivpn_youtube_tutorial.mp4"

cmd_concat = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list_path,
    "-c", "copy",
    final_output
]
subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Updated Full Video:", final_output)
