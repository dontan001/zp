# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZpItem(scrapy.Item):
    zwmc=scrapy.Field()#职位名称
    gsmc=scrapy.Field()#公司名称
    flxx=scrapy.Field()#福利信息
    min_zwyx=scrapy.Field()#职位月薪(最低)
    max_zwyx = scrapy.Field()  # 职位月薪(最高)
    gzdd=scrapy.Field()#工作地点
    fbrq=scrapy.Field()#发表日期
    gsxz=scrapy.Field()#公司性质
    gzjy=scrapy.Field()#工作经验
    zdxl=scrapy.Field()#最低学历
    zprs=scrapy.Field()#招聘人数
    zwlb=scrapy.Field()#职位类别
    gsgm=scrapy.Field()#公司规模
    gshy=scrapy.Field()#公司行业
    gwzz=scrapy.Field()#岗位职责
    gwzz_fenci=scrapy.Field()
    rzyq=scrapy.Field()#任职要求
    rzyq_fenci = scrapy.Field()