import requests
from bs4 import BeautifulSoup
import autoMail


message = [] # 信息栏
url = "http://quotes.money.163.com/trade/lsjysj_600519.html#01b07"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

resp = requests.get(url, headers=headers)
# print(resp.text)
bs = BeautifulSoup(resp.text, "html.parser")
table = bs.find("table", class_="table_bg001 border_box limit_sale")

trs = table.find_all("tr")
ths = trs[0]  # 获取头
th_list = ths.find_all('th')
ths_list = []
for th in th_list[0:6]:
    print(th.text)
    ths_list.append(th.text)
print(ths_list)
for i in ths_list:
    print(i, end='        ')
print()
message.append(ths_list)
for tr in trs[1:]:
    # temp = []
    # print(tr)
    td_list = tr.find_all("td")
    day = td_list[0].text
    start = td_list[1].text
    max = td_list[2].text
    min = td_list[3].text
    end = td_list[4].text
    change_count = td_list[5].text
    # print(day,start,max,min,end,change_count,sep='\t\t')
    temp = [day, start, max, min, end, change_count]
    print(temp)
    message.append(temp)

print(str(message))

autoMail.autoSend(str(message))

resp.close()


