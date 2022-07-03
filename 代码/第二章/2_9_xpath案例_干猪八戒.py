# 拿到页面源代码
# 提取和解析数据
# 猪八戒网足够复杂, 足够练手d
import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas" # 这里搜索的是saas
resp = requests.get(url)
# print(resp.text) # 拿出页面源代码

# 解析
html = etree.HTML(resp.text) # 不能混着用, html不能用xml

# 一块一块来定位
# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div") # 返回所有的div(所有的服务商)
for div in divs:  # 每一个服务商信息
    # 细心, 层层
    # // *[ @ id = "utopia_widget_76"] / a[2] / div[2] / div[1] / span[1] # 不是很推荐使用带有id的进行匹配, 因为id一般都是唯一的
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥") # 价格
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    # 标题 .去页面源代码可以看出, 他是将saas高凉了,所以分割开了, 所以直接用saas.join拼接起来
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0] #
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    # print(com_name)
