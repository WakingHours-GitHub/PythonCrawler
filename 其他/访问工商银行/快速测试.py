import requests
import re
from lxml import etree

url = "https://www.icbc.com.cn/icbc/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

resp = requests.get(url, headers=headers)
charset = re.findall(r'charset=(?P<charset>.*?)"',resp.text)[0]
resp.encoding=charset
print(resp.text)



# print(charset)

resp.close()