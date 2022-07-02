# 因为北京新发地换页面了
# 所以这里使用豆瓣TOP排行榜来练习

# 线程池案例应用:

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor  # 导入线程池
import csv

f = open("data.csv", mode='w', encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    f = open("data.csv", mode='a', encoding="utf-8")
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0 Win64x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 93.0.4577.82Safari / 537.36Edg / 93.0.961.52"}
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    resp.encoding = 'utf-8'

    html = etree.HTML(resp.text)
    # 利用xpath查找内容
    ol = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol")[0]
    names = ol.xpath("./li/div/div[2]/div[1]/a/span[1]/text()")
    commits = ol.xpath("./li/div/div[2]/div[2]/div/span[4]/text()")
    for i in range(len(names)):
        csvwriter.writerow([names[i], commits[i]])

    # print(ol)
    f.close()
    resp.close()


if __name__ == '__main__':
    # download_one_page("https://movie.douban.com/top250")
    with ThreadPoolExecutor(5) as t:
        for i in range(11):  # 循环
            t.submit(download_one_page, f"https://movie.douban.com/top250?start={i * 25}&filter=")

    print('下载完毕')
