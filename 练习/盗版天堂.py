import re
import requests



# 电影天堂主URL
main_url = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}
resp = requests.get(main_url, headers=headers, verify=False)
resp.encoding = "gb2312"
# print(resp.text) # 实际上在输出text时, 系统就已经进行decode了, 于是我们需要提前将encode设置一下

# 然后我们准备re: compile进行预加载
ul_li_total_str = re.compile(".*?2022必看热片.*?<ul>(?P<li>.*?)</ul>", re.S).search(resp.text).group("li").strip()

iter = re.compile("<li><a href='(?P<href>.*?)' title=.*?", re.S).finditer(ul_li_total_str)

# 用于匹配电影名字以及下载链接的。
comp = re.compile('.*?◎片　　名　(?P<movie_name>.*?)<br />.*?<div class=player_list>.*?<ul>		<li><a href="(?P<download_link>.*?)">', re.S)
for it in iter:
    child_url = main_url+it.group("href").strip("/")
    child_resp = requests.get(child_url, headers=headers)
    child_resp.encoding="gb2312"
    print(comp.search(resp.text).groupdict())

    child_resp.close()




resp.close()


