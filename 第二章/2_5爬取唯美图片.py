# bs4实战环节: 爬取图片
# 思路:
# 1. 拿到页面源代码. 获取子页面的链接地址(使用href)
# 2. 通过href获取到子页面的内容, 从子页面中找到下载地址.
#   img -> src 地址.
# 3. 将文件下载

import requests
import re
from bs4 import BeautifulSoup
import time


# url:
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

# resp
resp = requests.get(url, headers=headers)  # 请求主页面
re_ = re.compile(r'charset="(?P<char>.*?)"')
its = re_.search(resp.text)
charset = its.group("char")
# print(charset, type(charset))
resp.encoding = charset  # 设置编码格式

# 将页面源代码交给bs解析 并且指定解析器为html.parser. parser: 分析程序, 语法刨析程序
main_page = BeautifulSoup(resp.text, "html.parser")

# 一步一步定位
# 首先先找div标签, 属性class为TypeList, 然后找a标签.
#
alist = main_page.find("div", class_="TypeList").find_all("a")  # 从div 属性class中找a标签
# 找到所有的a标签, 返回为一个list.
for a_it in alist:
    # 从bs对象中拿到属性值. 通过get拿到属性值.
    href = a_it.get("href")  # 爬取所有的链接
    print(href) # 子页面的链接
    # 拼接下载地址.
    href = "https://www.umei.cc" + href
    # href = url.rstrip('/')
    print(href)

    # 请求子页面链接
    subresp = requests.get(href)
    subCharset = re_.search(subresp.text)
    subresp.encoding = subCharset

    # 将子页面的页面源代码交给bs4进行解析.
    subPage = BeautifulSoup(subresp.text, "html.parser")  # 返回子页面的bs对象
    # 一般不通过align进行定位. 都是通过class和id进行定位
    p = subPage.find("p", align="center")  # 标签+属性定位
    img = p.find("img")  # 拿到img的整个标签
    imgSrc = img.get("src")  # 直接拿到属性
    # 这就是图片的下载路径.

    # 最后下载图片:
    # 直接请求到这个地址. 然后使用.content字节形式, 然后将字节写入到文件里面去, 加上后缀名就是一个特定格式的文件了
    # content返回字节内容, 所以我们把一张图片的字节都写入一个文件,那自然就是整张图片了
    # img_resp.content是没意义的. 因为是字节
    img_resp = requests.get(imgSrc) # 请求
    img_name = imgSrc.split("/")[-1]  # 切割,然后拿最后一个元素, 作为名字.
    # wb写二进制.
    with open("img/" + img_name, mode="wb") as f:  # 写入文件夹img中
        f.write(img_resp.content)  # 将图片内容写入文件
    # 为了频繁请求导致服务器封锁ip我们可以使用time.sleep进行程序睡眠

    subresp.close() # 关闭流; # 不停的请求,

resp.close() # 关闭;
