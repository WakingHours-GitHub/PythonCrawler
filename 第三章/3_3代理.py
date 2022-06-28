# 原理, 通过第三方的一个机器去发送请求
# 在你ip被封锁的时候使用该方法
import requests
import 其他.爬取免费代理ip.getIpDict

ipdict = 其他.爬取免费代理ip.getIpDict.getIpDict();

strIp = list(ipdict.keys())[0]
final = "http://"+strIp+":"+ipdict[strIp]
print(final)

proxies = {
    # "https": "http://46.4.96.137:8080" # 新的版本都需要前面加上http// 或者https
    "http": final
}

url = "https://www.bilibili.com/"
resp = requests.get(url, proxies=proxies)
resp.encoding="utf-8"
print(resp.json)
print(resp.text) # 拿到页面网址

resp.close()
