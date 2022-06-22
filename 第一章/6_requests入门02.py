"""
第二个项目我们想通过requests获取百度翻译
sug -> suggestion 请求。
from data -> 要发送的数据

"""
import requests


url = "https://fanyi.baidu.com/sug" # 在抓包工具中,我们看到是以POST方式请求的
# post就是隐式请求方式。
word = input("请输入要翻译的英文单词")
# 请求头。
header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
}

# POST方式是data
dat = {  # 数据仍然以字典形式
    "kw": word  # 参数
}

# 发送post请求，发送的数据必须在data参数中进行传递
resp = requests.post(url, data=dat, headers=header)
print(resp.text) # 打印页面源代码
print('---'*10)
print(resp.json()) # 将服务器返回的内容直接处理成为json() -> python中的dict
