import re
import requests
from bs4 import BeautifulSoup

# 更新时间是否要精确的时间, 如果为True保留时间, 如果False则只保留年月日
IS_TIME = False

ATTENTION_LIST = ["黑龙江"]


def get_charset(resp) -> str:
    return re.compile('<meta.*?charset=(?P<charset>.*?) .*?/>', re.S).search(resp.text).group("charset").strip().strip('"')


def get_oil_price() -> list:
    today_oil_price = [["region", "#92", "#95", "#98", "update date"]]

    url = "http://youjia.chemcp.com/index.asp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    }
    # 请求
    resp = requests.get(url, headers=headers)
    resp.encoding = get_charset(resp) #  指定编码
    source_page = resp.text #  页面源代码
    # 交给bs4进行解析.
    bs_page = BeautifulSoup(source_page, "html.parser")
    # 定位到国内油价的盒子
    county_oil_box_page = bs_page.find("div", class_="cpbaojia")
    table_trs = county_oil_box_page.find_all("tr") # zho
    head_list = table_trs[0].text.split("\n")[1:-1]
    for tr in table_trs[1:]:
        area_list = tr.text.split("\n")[1:-1]
        # print(area_list)
        if area_list[0] in ATTENTION_LIST:
            area = area_list[0]
            gasoline_92 = area_list[2]
            gasoline_95 = area_list[3]
            gasoline_98 = area_list[4]
            update_date = area_list[-1]
            if not IS_TIME: #
                update_date = update_date.split(' ')[0]
            today_oil_price.append([area, gasoline_92, gasoline_95, gasoline_98, update_date])

            # 如果列表>2, 那么不能直接退出而是需要等待.
            if not len(ATTENTION_LIST) > 1:
                break
    resp.close()
    return today_oil_price


# 测试用
if __name__ == '__main__':
    print(get_oil_price())
