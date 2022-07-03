# 拿到页面源代码.   requests
# 通过re来提取想要的有效信息  re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num"))
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
print("over!")





