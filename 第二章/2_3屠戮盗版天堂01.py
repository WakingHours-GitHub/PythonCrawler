# 思路是非常明确的: 我们需要确认是服务器渲染, 还是客户端渲染.
# 我们需要首页中的一部分, 所以我们需要先定位到我们需要的位置: 2020必看片
# 然后从2020必看片中提取到子页面的url地址
# 请求子页面的链接地址, 拿到我们想要的下载地址

import requests
import re

domain = "https://www.dytt89.com/"
# 注意, 该网站是https, 采用的是加密的一些问题. 请求时候会发送一些证书.
# 于是我们需要将安全认证去掉即可.

child_href_list = []

resp = requests.get(domain, verify=False)  # verify=False 去掉安全认证, 在控制台中会警告
resp.encoding = 'gb2312'  # 指定编码字符集
print(resp.text)  # 设置resp的encoding = 'gb2312'即可
# print(resp.text) # 默认是utf-8 # 出现乱码, 在页面源代码中charset= 表示页面使用的编码方式

# 补充一点html基础的东西:
# html在a标签表示超链接: <a href = 'url'> 名称 </a> # 只要点击这个名称就会跳转到url

# 定位到2021必看热片, 并找到下面的列表
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S) # 捕捉2021必看热片的区域内容.
obj2 = re.compile(r"href='(?P<href>.*?)'", re.S)  # 捕捉子页面的url
obj3 = re.compile(r'>◎片　　名　(?P<movie>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',
                  re.S)  # 提取子页面中下载链接

result1 = obj1.finditer(resp.text) # 捕捉2021必看热片

for it in result1:
    # print(it.group("ul")) # 这样就拿到了必看热片中的源代码
    # ul = it.group("ul")
    # 在拿到的子页面中提取每一条的url
    result2 = obj2.finditer(it.group("ul"))
    for it2 in result2:
        # print(it2.group('href')) # 这样就打印出来了所有子界面的url
        # 然后去除'/'再拼接上主url,就可以访问到子界面了
        # 拼接子页面的url地址: 域名 + 子页面地址
        child_href = domain + it2.group('href').strip('/')
        child_href_list.append(child_href)  # 添加进去
# 提取页面内容:

for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)  # 在子页的页面源代码中提取
    print(result3.group("movie"))
    print(result3.group("download"))
