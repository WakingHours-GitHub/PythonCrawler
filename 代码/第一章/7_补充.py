import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 1,
    "limit": 20,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}

resp = requests.get(url=url, params=param, headers=headers)

print(resp.json())
resp.close()  # 关掉resp
