# 本次使用的案例是爬取梨视频
#

import requests
from 其他.获取chatset.getChatset import getChatset
from 其他.爬取免费代理ip.getRefererUrl import getRefererUrl
# from 其他.爬取免费代理ip.getIpDict import getIpDict

url = "https://www.pearvideo.com/video_1721605"

videoUrl = "https://video.pearvideo.com/mp4/adshort/20210227/cont-1721605-15617918_adpkg-ad_hd.mp4"

prostr = getRefererUrl()
print(prostr)
proxies = {
    "https": prostr
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52",
    # 当添加user-Agent仍然没有爬取到内容时, 我们就需要考虑防盗链了
    "Referer": url
}

resp = requests.get(videoUrl,headers=headers, proxies=proxies)
print(resp.text)
resp.encoding = getChatset(resp.text)  # 返回charset



resp.close()
