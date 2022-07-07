import scrapy
# 导入Selector对象
from scrapy import Selector

from Scrapy_qianfeng.first_spider.first_spider.items import MovieItem

"""
启动蜘蛛程序:
    scrapy crawl 名字 -o 数据存放地址 --nolog # 表示不打印日志
    数据, 支持, csv, xml, xpath, json
    例子:
    scrapy crawl douban -o douban.csv 
    
"""

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 其实URL, 我们就是从这里开始爬, 交给引擎, 交给调度器, 然后交给下载器
    start_urls = ['https://movie.douban.com/top250']

    # parse, 就是通过response进行解析页面.
    def parse(self, response):
        # 包装成selector对象(选择器对象)
        # 该对象支持css解析, 支持xpath解析, 支持re解析
        sel = Selector(response)
        # 样式表使用浏览器开发工具进行寻找.
        # sel.css("#content > div > div.article > ol > li:nth-child(1)")
        # nth-child(1)表示第一个li列表, 所以我们需要去掉
        # 返回的仍然是是一个Selector对象
        list_items = sel.css("#content > div > div.article > ol > li")
        for list_item in list_items:
            movie_item = MovieItem()

            # list_item.css("span.title::text") # 返回的仍然是一个选择器对象, 因此我们需要抽取其中的内容
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            movie_item['rank'] = list_item.css('span.rating)num::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()

            # 到这, 我们的数据就已经组装好了, 组装到我们的item对象中了.
            # 但是我们不能直接返回, 因为在for循环里, 循环一次, 是组装一条.
            # 因此我们需要使用生成器: yield, 产出我们的数据, 交给引擎, 交给数据管道.
            #
            # return movie_item
            yield movie_item

        # Selector对象.
        # sel.css()
        # sel.xpath()
        # sel.re()
