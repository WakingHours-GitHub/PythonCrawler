# 因为bs4是额外的模块.所以需要安装
# pip install bs4 -i 清华

# 1. 拿到页面源代码
# 2. 使用bs4进行解析. 拿到数据
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)

f = open("菜价.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

# 解析数据
# 1. 把页面源代码交给BeautifulSoup进行处理, 生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器, 否则它会去猜是什么文件,从而产生warning
# 2. 从bs对象中查找数据
# find(标签, 属性=值) # find就找第一个匹配的标签, 就返回
# find_all(标签, 属性=值)  # 找出所有的
# table = page.find("table", class_="hq_table")  # class是python的关键字,所以在后面加上"_"可以区别开,避免报错
# 另一种方式是:使用attrs={}以字典的形式
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行是一个意思. 此时可以避免class
# print

# 拿到所有数据行
trs = table.find_all("tr")[1:]  # 拿到table然后再find, <tr>是一行, 一列是<td>
# 后面跟上截取, 不要表头, 只要内容
for tr in trs:  # 每一行
    tds = tr.find_all("td")  # 拿到每行中的所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low = tds[1].text  # .text 表示拿到被标签标记的内容
    avg = tds[2].text  # .text 表示拿到被标签标记的内容
    high = tds[3].text  # .text 表示拿到被标签标记的内容
    gui = tds[4].text  # .text 表示拿到被标签标记的内容
    kind = tds[5].text  # .text 表示拿到被标签标记的内容
    date = tds[6].text  # .text 表示拿到被标签标记的内容
    print(name, low, avg, high, gui, kind, date)
    csvwriter.writerow([name, low, avg, high, gui, kind, date])

f.close()
resp.close()
print("over1!!!!")


