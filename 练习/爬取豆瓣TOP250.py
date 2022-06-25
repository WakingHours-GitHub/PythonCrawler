import re
import requests
import pandas as pd


def get_top_250():
    # URL = "https://movie.douban.com/top250"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",

    }
    # "https://movie.douban.com/top250?start=25&filter="
    for i in range(0, 100, 25):
        URL = fr"https://movie.douban.com/top250?start={i}&filter="
        # print(URL)

        resp = requests.get(URL, headers=headers)
        # +
        #             '.*?<span property="v:best" content="10.0"></span> <span>(?P<comment_count>.*?)人评价</span>'+
        #             '.*?<p class="quote"><span class="inq">(?P<comment>,*?)</span>',
        regular_comp = re.compile(
            '<li>.*?<span class="title">(?P<film_name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'+
            '.*?<span>(?P<comment_count>.*?)人评价</span>.*?<span class="inq">(?P<comment>.*?)</span>',re.S)

        iter = regular_comp.finditer(resp.text)

        for it in iter:
            dic = it.groupdict() # 这样直接以字典形式打印出来
            dic['year'] = dic['year'].strip() # 处理两边空格和\n
            dic['comment'] = dic['comment']+"\n"
            # print(dic.values())
            with open("./test.csv","a") as f:
                f.write(','.join(dic.values()))




        resp.close()


if __name__ == '__main__':
    get_top_250()
