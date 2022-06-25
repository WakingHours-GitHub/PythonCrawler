# 因为bs4是额外的模块， 所以需要安装
# pip install bs4
# 简单介绍一下bs4:
# 他是根据html的标签来匹配内容的， 通过html语法<标签>以及属性可以精确匹配内容

# 因为北京新发地网站的页面源代码变了, 所以这里使用股票数据的表格来代替

# 使用bs4：
# 1. 拿到页面源代码
# 2. 使用bs4进行解析, 拿到所需要的数据
from bs4 import BeautifulSoup
import requests
# from bs4 import BeautifulSoup # 从bs4包中导入BeautifunSoup
import csv

f = open("400436.csv", mode="w",encoding="utf-8")
csvWirster = csv.writer(f)

url = "http://quotes.money.163.com/trade/lsjysj_600436.html#01b07"  # url
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8" # 任何页面在请求的时候设置charset
# print(resp.text) # 打印页面源代码

# 解析页面源代码
# 1. 把页面源代码交给BeautifulSoup进行处理, 返回bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器, 这样不会报错
# 2. 从bs对象中查找数据
# find(标签, 属性=属性值)  # find就是查找第一个匹配到的数据
# find_all(标签, 属性=属性值) # 找出所有匹配的数据
table = page.find("table", class_="table_bg001 border_box limit_sale")  # class是关键字, 在参数class后面加上_区分开

# 另一种方式是:使用attrs={}以字典的形式
# table = page.find("table", attrs={"class":"table_bg001 border_box limit_sale"})
# 得到的table是整个从<table> </table> 中的内容

# 然后我们从table中拿到所有的数据行
print("-" * 60)
print(table.find_all("tr"))
# 提取出表头
trs = table.find_all('th') # 拿出表头块
temp = []
for tr in trs:
    temp.append(tr.text)
    # csvWirster.writerow(tr) # 一列数据如何以行保存
    # print(tr.text)
csvWirster.writerow(temp)

trs = table.find_all("tr")[1:]  # 剔除第一行标头的元素
# 返回的trs是整个块

for tr in trs:  # 分离出每一行
    tds = tr.find_all("td")  # 分割出一行中的每一列
    date = tds[0].text # 直接用text就可以拿出标签标记的内容
    start = tds[1].text
    max = tds[2].text
    min = tds[3].text
    end = tds[4].text
    change_count = tds[5].text
    change_rate = tds[6].text
    num = tds[7].text
    num_count = tds[8].text
    rate = tds[9].text
    huanshou = tds[10].text

    csvWirster.writerow([date, start, max, min, end, change_count, change_rate, num, num_count,rate,huanshou])
    print(date, start, max, min, end, change_count, change_rate, num, num_count)

resp.close()
f.close()
