# 爬虫： 通过编写程序来获取互联网上的资源
# 我们点击http://www.baidu.com, 就是访问百度的URL
# 需求： 用程序模拟浏览器，输入一个网址，从该网址中获取资源或者内容

# 导入包
from urllib.request import urlopen  # 从urllib库的request导入urlopen

url = "http://www.baidu.com"
resp = urlopen(url)  # 得到响应
# resp.read() # 读取内容, 但是网页传输的都是bin字节文件, 所以我们需要decode,
# 写入文件:
with open("mybaidu.html", mode="w", encoding="utf-8") as f:  # 这是文件内容的知识
    f.write(resp.read().decode("utf-8"))  # 读取网页的页面源代码

print('over')  # 表示程序结尾
