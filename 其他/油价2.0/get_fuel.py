import requests
import re
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 更新时间是否要精确的时间, 如果为True保留时间, 如果False则只保留年月日
IS_TIME = False

ATTENTION_LIST = ["黑龙江"]

class SpiderFuelPrices():
    def __init__(self):
        self.url = "http://youjia.chemcp.com/index.asp"
        self.request = None
        self.headers = {
            "User-Agent": UserAgent().chrome,

        }
        self.response = None


    def get_charset(self) -> str:
        """获取网页的charset, 解决乱码"""
        return re.findall(
            '<meta .*? charset=(.*?)" />',
            self.response.text,
            re.S
        )[0]

    def start_spider(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.response.encoding = self.get_charset()
        # print(self.response.text)
        bs_page = BeautifulSoup(self.response.text, "html.parser") # 使用bs4进行解析
        div_bs_page = bs_page.find("div", attrs={
            "class": "cpbaojia" # 拿到最外层的盒子.
        })
        table_b4_page = div_bs_page.find("table")
        region_fuel_price_list = table_b4_page.text.split("\n\n") # 按行切割.
        region_fuel_price_list = [ele.strip().split("\n") for ele in region_fuel_price_list if ele != '']
        # print(region_fuel_price_list)
        header = region_fuel_price_list[0] # 拿到header头
        selected_region = list()
        for region in region_fuel_price_list:
            if region[0] in ATTENTION_LIST:
                region.pop(1)
                region.pop(-2)
                selected_region.append(region)

        # 对header进行处理: 去除#89, 和柴油
        header.pop(1)
        header.pop(-2)




        return header, selected_region









# 测试
if __name__ == '__main__':
    sfp = SpiderFuelPrices()
    sfp.start_spider()