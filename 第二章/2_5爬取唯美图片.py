# bs4实战环节: 爬取图片
# 1. 拿到页面源代码. 获取子页面的链接地址(使用href)
# 2. 通过href获取到子页面的内容, 从子页面中找到下载地址
# 3. 将文件下载

import requests
import re
from bs4 import BeautifulSoup


url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

resp = requests.get(url, headers=headers)
re_ = re.compile(r'charset="(?P<char>.*?)"')
its = re_.search(resp.text)
charset = its.group("char")
# print(charset, type(charset))
resp.encoding=charset # 设置编码格式

# 将页面源代码交给bs解析
main_page = BeautifulSoup(resp.text, "html.parser")
# 一步一步定位
alist = main_page.find("div", class_="TypeList").find_all("a") # 从div 属性class中找a标签
for a_it in alist:
    href = a_it.get("href") # 爬取所有的链接
    print(href)
    href = "https://www.umei.cc"+href
    # href = url.rstrip('/')
    print(href)
    # 请求子页面链接
    subresp = requests.get(href)
    subCharset = re_.search(subresp.text)
    subresp.encoding=subCharset

    subPage = BeautifulSoup(subresp.text, "html.parser") # 返回子页面的bs对象
    p = subPage.find("p", align="center") # 标签+属性定位
    pic = p.find("img") # 拿到img的整个标签
    picSrc = pic.get("src") # 直接拿到属性

    # 下载图片:
    # content返回字节内容, 所以我们把一张图片的字节都写入一个文件,那自然就是整张图片了

    img_resp = requests.get(picSrc)
    img_name =  picSrc.split("/")[-1] # 切割,然后拿最后一个元素
    with open("img/"+img_name, mode="wb") as f: # 写入文件夹img中
        f.write(img_resp.content) # 将图片内容写入文件

    subresp.close()





resp.close()