# 原理. 通过第三方的一个机器去发送请求
import requests


# 218.60.8.83:3129
proxies = {
    # "http":"",
    # "https":"", # 老版本的直接写ip即可, 但是新版本还需要写入http://ip:port
    "https": "https://218.60.8.83:3129"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
