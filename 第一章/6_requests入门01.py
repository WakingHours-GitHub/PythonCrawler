"""
下面讲解爬虫领域非常重要的一个模块: requests模块
并不是python自带的模块. 所以, 我们需要pip进行安装.

"""
# 安装requests
# 命令：pip install requests
# 国内源：推荐：清华源，阿里源
# pip install -i 源 模块
# 例子: pip install -i Https://pypi.tuna.tsinghua.edu.cn/simple requests

# 第一步， 导入模块
import requests

query = input('请输入要搜索的内容:')

# 在地址栏里进行访问的, 一定都是get方式 进行的提交
url = f"https://cn.bing.com/search?q={query}"  # 在浏览器中中文是以编码形式的
# f-str
# 请求头, 内容从浏览器进行复制.
# 以key: value 的方式进行保存
myHeaders = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38 "
}  # 通过加了一个muHeaders来处理反爬: 伪装的更像浏览器

# 所以这里就直接使用get方式进行提交
resp = requests.get(url, headers=myHeaders)  # 在地址栏中搜索的都是get请求

print(resp)  # <Response [200]> # 显示状态：200 表示没有问题, 这应该是一个对象.
# resp. 可以调出很多东西，例如txt，json...等很多格式的文件
print(type(resp))  # <class 'requests.models.Response'> 一个从来没有见过的文件

print(resp.text)  # 拿到页面源代码
# 可能会被url的后端服务器识别出是程序发出的, 所以我们需要伪装的更像我们的浏览器请求
# 这时候就需要User-Agent, 在network(浏览器抓包工具)中可以找到
