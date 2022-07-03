# 1. 拿到contId
# 2. 拿到videoStatus返回的json. ->  srcURL
# 3. srcURL里面的内容进行修整
# 4. 下载视频
import requests

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1721605"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    # 防盗链: 溯源, 当前本次请求的上一级是谁
    "Referer": url
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
