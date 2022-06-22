import requests
import json

"""
XHR: ajxs请求, 一般来说就是第二次请求, 即数据的请求

URL中, ?前面是网址链接, ?后面是参数.

"""

url = "https://movie.douban.com/j/chart/top_list"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"

}
# get请求的参数: Query String Parameters
# 或者在负载(payload)中, 里面存放这本次请求所需要的参数.
# 这的参数也可以不写死, 这样可以实现翻页的效果.
param = {  # 使用字典形式封装参数

    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
# 如果使用的get请求的Url连接特别长, 那么你就可以采用第二种方式进行连接.
# 重新封装参数:
# 就是使用params参数进行封装.
# 发送请求. get请求, 来自于通过网页进行查询
# post请求发送带参数请求为data, 但是get请求发送请求参数为params
resp = requests.get(url=url, params=param, headers=header)

# 从响应头找到请求对象, 然后打印请求的URL链接.
# 所以直接在URL显式的加上参数, 和使用params加上参数结果一样.
print(resp.request.url) # 打印的就是组合在一起的URL: URL?参数


print(resp.text)  # 当没有任何结果时, 说明我们被反扒了. 我们第一个需要考虑的就是UserAgent,
print(resp.request.headers)  # 查看当前的User—Agent, 默认的User-Agent, 然后加上header后再查看一下.
# print(resp.json()) # 处理成为JSON, 从响应预览.


# resp也是一个流管道, 这里表示关闭链接.
# 也可以在请求同中将: Keep-Alive: false #
resp.close() # 关掉resp， 如果不关掉这个resp访问过多很可能会报错