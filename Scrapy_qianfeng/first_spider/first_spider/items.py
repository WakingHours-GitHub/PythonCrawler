# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
数据需要组装起来, 成为一个item对象
所以我们需要自定义一个类, 去继承Item类
我们要定义字段, 与我们爬取时所定义的字段相同. 这也是属性. 我们在爬虫程序中也会用到


"""

class MovieItem(scrapy.Item):
    # 定义字段, 给item
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()


class FirstSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
