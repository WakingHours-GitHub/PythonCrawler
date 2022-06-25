# 豆瓣TOP250是服务器渲染, 数据和页面一起返回
# 拿到页面源代码. requests
# 通过re模块来提取想要的有效信息 re

import requests
import re
import csv  # 补充

# csv的特点是以,作分割,这样可以方便数据导入

url = "https://movie.douban.com/top250"  # get方式

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
}

# 请求, 返回响应.
resp = requests.get(url, headers=headers)
page_content = resp.text  # 拿到页面源代码

# print(resp.text)

# 解析数据, 使用预加载正则表达式
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?"v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)  # 观察页面源代码，找到我们需要的内容然后爬取
# 往文件里写入: # 文件操作, 能理解就行
f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)  # 这样读入csvwriter就可以直接往文件中写了

result = obj.finditer(page_content)

for it in result:
    # 需要将数据整理称为字典的格式
    dic = it.groupdict()  # 分组名字作为key,每一个(it)匹配到的对象为value
    # 以字典的形式进行返回, 但是我们需要对year这一数据进行特殊的处理.
    # print(dic)
    # year需要单独的处理.
    dic['year'] = it.group("year").strip()  # 需要对year这个key对应的value进行处理,取出空格
    # print(dic)
    csvwriter.writerow(dic.values())  # 将所有的value写进入
    # 分组名是keys
    # print(it.group("name"))
    # print(it.group("year").strip())  # 我们发现year前面一大堆空格,我们可以使用strip函数,取出两边空格
    # print(it.group('score'))
    # print(it.group("num"))

# 这仅仅是爬了一篇的数据,我们要爬多页,就需要修改url后面的参数
# https://movie.douban.com/top250?start=25&filter=


print('over!')
f.close()  # 关闭文件
resp.close()  # 关闭请求
