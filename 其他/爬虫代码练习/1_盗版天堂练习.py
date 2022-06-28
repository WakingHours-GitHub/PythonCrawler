# 获取盗版天堂中的2021热片栏中的每条电影的下载地址

# 我们首先需要定位到[2021必看热片]
# 然后我们从2021必看热片中获取每条电影的url
# 然后请求每条电影的url,拿到哦我们所需要的下载地址

import re
import requests

source_url = "https://www.dytt89.com/"

headers = {  # 定义user-agent
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "AChrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44 "
}

resp = requests.get(source_url, headers=headers)  # 请求源url的源代码
resp.encoding = 'gb2312'  # 设置字符集: 通常网页源代码中会指定charset=""
print(resp.text)  # 源url的源代码

reex_sou = re.compile(r"2021必看热片.*?<ul>(?P<url>.*?)</ul>", re.S)  # 预返回一个正则表达式
suburl = re.compile(r"<a href='(?P<href>.*?)'", re.S)  # 提取出来每一条的url

url2021 = reex_sou.finditer(resp.text)

for it1 in url2021:
    print(it1.group("url").strip())  # 这样就定位到了2021必看热片

    # 接下来提取每一条的url
    # suburl = re.compile(r"<a href='(?P<href>.*?)'", re.S) # 提取出来每一条的url

    suburlResult = suburl.finditer(it1.group("url"))
    for it2 in suburlResult:
        # print(it2.group("href")) # 打印的是每条的地址
        # 然后拼接:
        subNewUrl = source_url.strip('/') + it2.group("href")  # 每条电影玩完整的url

        # 请求每条电影的url
        subResp = requests.get(subNewUrl, headers=headers)
        subResp.encoding = "gb2312"
        reep_download = re.compile(r'<td style="WORD-WRAP:.*?<a href="(?P<addDownload>.*?)"')
        downloadAdd = reep_download.finditer(subResp.text)
        for it3 in downloadAdd:
            print(it3.group("addDownload")) # 这样就把所有的电影下载地址拷贝下来了
