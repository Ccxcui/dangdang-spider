# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    table = 'dangdangpythonbook'
    title = scrapy.Field()#书名
    author = scrapy.Field()
    price = scrapy.Field()
    comment_num = scrapy.Field()#评论数
    detail = scrapy.Field()#详情
    picurl = scrapy.Field()
