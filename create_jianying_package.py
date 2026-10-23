import subprocess
import os

WORK_DIR = "/Users/canyu/Desktop/gemini/vpn"

# 1. Update SRT subtitles with Dual-ISP narrative
srt_entries = [
    ("00:00:00,000", "00:00:04,500", "你是不是也经常遇到这种情况："),
    ("00:00:04,500", "00:00:09,000", "花钱买的机场节点，动不动就断线、跑路？"),
    ("00:00:09,000", "00:00:15,500", "尤其是用 ChatGPT、Claude 或者 Antigravity 写代码时，动不动就封号或拦截？"),
    ("00:00:15,500", "00:00:21,500", "想自己搭建，一搜教程又是买域名、配证书，还有一堆 Linux 报错直接劝退？"),
    ("00:00:21,500", "00:00:27,500", "今天这期视频，我教大家用最便宜的一顿外卖钱，通过我们开源的极速脚本，"),
    ("00:00:27,500", "00:00:33,000", "真正做到零基础、不需要买域名、不需要懂任何代码！"),
    ("00:00:33,000", "00:00:38,650", "在终端复制粘贴一行命令，30 秒搭好属于你的独享专线！全平台秒开 4K！"),
    
    ("00:00:38,650", "00:00:44,000", "自建节点最关键的一步，是拥有一台干净、稳定、没有被滥用的海外服务器。"),
    ("00:00:44,000", "00:00:51,500", "为什么很多人自己搭节点用 ChatGPT 依然被封？因为普通机房 IP 早被各大平台风控拉黑了！"),
    ("00:00:51,500", "00:00:58,000", "这里强烈推荐视频下方置顶链接中的 NovixLink 原生双 ISP 住宅 IP 云服务器。"),
    ("00:00:58,000", "00:01:06,000", "它最大的王炸优势，是提供纯正的美国家庭宽带住宅 IP，欺诈评分极低，海外 AI 与流媒体 100% 满血解锁！"),
    ("00:01:06,000", "00:01:14,000", "而且专门做了中国大陆优化的高速直连网络，超低延迟！免去繁琐实名，支持快捷支付，即买即用！"),
    ("00:01:14,000", "00:01:21,000", "下单后大概一分钟，系统就会把服务器 IP 和 root 密码发送到你的后台。"),
    
    ("00:01:21,000", "00:01:26,500", "拿到服务器之后，新手不用怕命令行，这一步非常简单！"),
    ("00:01:26,500", "00:01:33,000", "无论 Windows 还是苹果 Mac，直接打开系统自带的终端或 PowerShell。"),
    ("00:01:33,000", "00:01:39,500", "输入 ssh root 艾特你的服务器 IP，按下回车。"),
    ("00:01:39,500", "00:01:48,000", "接着把后台密码粘贴进去按回车，跳出欢迎信息就代表成功连入云服务器了！"),
    
    ("00:01:48,000", "00:01:53,000", "接下来就是见证奇迹的时刻！完全不需要手动敲复杂的配置。"),
    ("00:01:53,000", "00:01:59,500", "直接把我放在置顶评论里的一行开源脚本完整复制，粘贴到终端按回车！"),
    ("00:01:59,500", "00:02:06,000", "脚本会自动帮你开启 Linux 原生 BBR 拥塞控制，自动拉取最新 Xray 核心，"),
    ("00:02:06,000", "00:02:13,000", "并全自动配置抗封锁能力最强的 VLESS-Reality 真实大厂 TLS 伪装！"),
    ("00:02:13,000", "00:02:22,000", "前后只要 30 秒，屏幕上就会自动打印出专属节点链接与大尺寸二维码！"),
    
    ("00:02:22,000", "00:02:28,000", "节点生成后怎么用呢？电脑端推荐使用开源小巧的 v2rayN 客户端。"),
    ("00:02:28,000", "00:02:34,000", "复制生成的 vless 链接，在 v2rayN 主界面按 Ctrl + V 即可秒级导入！"),
    ("00:02:34,000", "00:02:41,000", "最关键的一步：在底部勾选【启用 Tun 模式】和【自动配置系统代理】！"),
    ("00:02:41,000", "00:02:50,000", "开启 Tun 模式后，浏览器、Git、终端以及 Antigravity IDE 全电脑网络自动走专线加速！"),
    ("00:02:50,000", "00:03:03,000", "如果是手机端，打开小火箭或 v2rayNG 扫描屏幕上的二维码即可一键连接！"),
    
    ("00:03:03,000", "00:03:10,000", "连接成功后看一下实际效果：打开 YouTube 播放 4K 60 帧视频，直接秒开拖拽无卡顿！"),
    ("00:03:10,000", "00:03:18,500", "用它跑 Antigravity 或者 ChatGPT 长文本对话，丝滑顺畅，完全没有断流和掉线问题！"),
    ("00:03:18,500", "00:03:28,000", "本期视频用到的 NovixLink 原生双 ISP 特惠购买通道与一键开源脚本，都在置顶评论和视频描述栏里。"),
    ("00:03:28,000", "00:03:42,000", "觉得视频有帮助请务必点赞、收藏、订阅频道并打开小铃铛！感谢大家收看，我们下期再见！")
]

srt_path = f"{WORK_DIR}/subtitles_for_jianying.srt"
with open(srt_path, "w", encoding="utf-8") as f:
    for i, (start, end, text) in enumerate(srt_entries, 1):
        f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

print("Updated SRT Subtitles:", srt_path)

txt_path = f"{WORK_DIR}/jianying_voice_script.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    for _, _, text in srt_entries:
        f.write(f"{text}\n")

print("Updated Plaintext Script:", txt_path)

# 2. Build silent video with padded scene durations
scenes_dur = [38.65, 42.50, 27.00, 34.00, 41.00, 39.00]
scene_silent_vids = []

for idx, dur in enumerate(scenes_dur, 1):
    frame_path = f"{WORK_DIR}/video_build/frame_{idx}.png"
    silent_vid = f"{WORK_DIR}/video_build/silent_scene_{idx}.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", frame_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-t", str(dur),
        "-vf", "scale=1920:1080",
        silent_vid
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    scene_silent_vids.append(silent_vid)

concat_list = f"{WORK_DIR}/video_build/silent_concat.txt"
with open(concat_list, "w") as f:
    for v in scene_silent_vids:
        f.write(f"file '{v}'\n")

silent_output = f"{WORK_DIR}/antivpn_silent_video.mp4"
cmd_concat = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    silent_output
]
subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Updated Silent Video:", silent_output)
