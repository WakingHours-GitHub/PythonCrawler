import requests

session = requests.session()


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
    "cookie": "buvid3=8CEA9115-1147-AD18-721E-65AE18785EB078201infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(JYl)|~)Rmm0J'uYJu)RlJmk; fingerprint=a56548ecfc3ef73978bc657b68ac3de2; buvid_fp=8CEA9115-1147-AD18-721E-65AE18785EB078201infoc; buvid_fp_plain=85E7AB53-F216-8591-8992-AFB6AE2B6B4408134infoc; CURRENT_QUALITY=80; _uuid=E0A031FD-E9BE-AB30-930B-F685F7E3F2EA82326infoc; SESSDATA=d57273e7%2C1647411002%2C83828%2A91; bili_jct=e287496aaaccd65ca4514ea68d1dfb0e; DedeUserID=26537959; DedeUserID__ckMd5=70b0bd7ba36a814f; sid=bq9vj6p7; innersign=0"
}
url = "https://space.bilibili.com/26537959/favlist"
resp = session.get(url,headers=headers)
resp.encoding="utf-8"
print(resp.text)

resp.close()