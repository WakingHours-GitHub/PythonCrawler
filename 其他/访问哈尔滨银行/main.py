import requests
from lxml import etree
#
# url = "https://ibank.hrbb.com.cn/main.html?eyJFTVBfU0lEIjoiSEtCRUhRRFRHTEJCQkFETUlOQU1KR0dCSk5CTUFGSVhKU0ZZREpDTiJ9"
#
#
# session = requests.session()
# resp = session.post(url)
# # resp = requests.post(url)
# resp.encoding="utf-8"
#
# print(resp.text)
#
#
# resp.close()



url = "https://ibank.hrbb.com.cn/js/frontpage/framejs/frame_main.js?_=1631861428273"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
    "Cookie": "oneapmclientid=17bf1840f40303-0dfc7ef0f95ffa-57341040-1fa400-17bf1840f411c7; __smVisitorID=NNr3tWzqW99; oneapmbiswitch=event=1; ONEAPM_BI_sessionid=7400.740|1631860991899|; JSESSIONID=qZ4m6MghJX7NcyjV5P6aV13PPWDfRXjdiTGUk9n9xakYfCkdphKw15W9ssRwFEQJ.dXBhc19kb21haW4vcGVyYmFuazI=",
    "Referer": "https://ibank.hrbb.com.cn/main.html?eyJFTVBfU0lEIjoiSEtCRUhRRFRHTEJCQkFETUlOQU1KR0dCSk5CTUFGSVhKU0ZZREpDTiJ9"
}

resp = requests.session().get(url,headers=headers)
print(resp.text)
tree = etree.HTML(resp.text)
print(tree.text)
menoy = tree.xpath("/html/body/div[6]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr/td[7]")
print(menoy)

resp.close()




