import requests

session = requests.session() # 打开一个会话窗口

resp = session.get("https://www.icourse163.org/home.htm?userId=1396867645#/home/course")

resp = requests.get("https://www.icourse163.org/home.htm?userId=1396867645#/home/course")
print(resp.text)
