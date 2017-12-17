# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import jieba.analyse as jan
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ZpPipeline(object):

    #默认处理item的方法
    #item 接受一个传递过来的item容器
    #spider 生成对应item的spider爬虫
    def process_item(self, item, spider):
        return item
    #启动spider爬虫的时候调用的方法
    def open_spider(self,spider):
        pass
    #当spider爬虫停止的时候调用的方法
    def close_spider(self,spider):
        pass
    #返回爬虫的实例对象（新建管道的爬虫实例）
    @classmethod
    def from_crawler(cls,crawler):
        pass
#数据去重
class DropItemPipeline(object):
    #初始化建立set集合，存储职位名称+公司名称组合
    def __init__(self):
        self.name_seen=set()
    #默认执行方法，判断item中职位名称+公司名称的组合，
    #是否在set_names中，如果存在，则抛出异常，丢弃Item
    #如果不存在，则在set_names中添加职位名称+公司名称的组合，并且返回item给后面的管道
    #*** 需要在上面引入DropItem模块
    def process_item(self, item, spider):
        zh=item['zwmc']+item['gsmc']+item['zwlb']
        #如果存在，则抛出异常，丢弃Item
        if zh in self.name_seen:
            raise DropItem('had items')
        #如果不存在，则在set_names中添加职位名称+公司名称的组合，并且返回item给后面的管道
        else:
            self.name_seen.add(zh)
            return item

#数据清洗
class DataCleanPipeline(object):
    def process_item(self,item,spider):
        # 对于所有字符串数据，去除两段空格
        for key in item:
            if item[key] is str:
                item[key]=item[key].strip()  #去除两端空格的操作
        # 对于数据进行一步的分割处理
        # 可以将spider中数据处理的操作，放到这里来执行
        # 文本分词，提取关键词
        # jieba中文分词模块，需要在上面引入jieba模块，并且需要使用pip install jieba 安装
        #import jieba.analyse  引入结巴中关键词提取的模块
        # 对于岗位职责和任职要求做关键词提取
        gwzz_fenci=jan.extract_tags(item['gwzz'],topK=10)
        item['gwzz_fenci']='/'.join(gwzz_fenci)
        rzyq_fenci = jan.extract_tags(item['rzyq'], topK=10)
        item['rzyq_fenci'] = '/'.join(rzyq_fenci)
        # 判断异常值或者空值数据，进行数据填充
        #(1)判断最低薪资和最大薪资是否为空的判断和数据填充
        if item['min_zwyx']=='':
            item['min_zwyx'] =0
        elif item['max_zwyx']=='':
            item['max_zwyx'] = 0
        elif item['gsxz']=='':
            item['gsxz']='其他'
        return item
        #。。。。。
#发布日期字符串转化为时间字符串形式
class DataTimePipeline(object):
    def process_item(self,item,spider):
        #引入模块
        import time
        #判断是否是前天
        if item['fbrq']==u'前天':
            #在当前时间戳上减去2天的秒数
            last_day_timetamp=time.time()-2*60*60*24
            item['fbrq']=time.strftime('%Y-%m-%d',time.localtime(last_day_timetamp))
        #判断是否是昨天
        elif item['fbrq']==u'昨天':
            #在当前时间戳上减去1天的秒数
            yesterday_timetamp=time.time()-60*60*24
            item['fbrq']=time.strftime("%Y-%m-%d",time.localtime(yesterday_timetamp))
        #判断是否是今天
        #‘刚刚’，'几小时前'，‘最新’，‘最近’，‘今天’
        elif item['fbrq']==u'刚刚' or item['fbrq']==u'最新' or item['fbrq']==u'最近' or item['fbrq']==u'今天' or u'小时前' in item['fbrq']:
            item['fbrq']=time.strftime('%Y-%m-%d',time.localtime())
        elif u'天前' in item['fbrq']:
            days=int(item['fbrq'].strip(u'天前'))   #提取天数
            days_timetamp=time.time()-days*60*60*24
            item['fbrq']=time.strftime('%Y-%m-%d',time.localtime(days_timetamp))
        else:
            #假设上述内容都不满足，则保存为今天的日期
            item['fbrq'] = time.strftime('%Y-%m-%d', time.localtime())
        return item

import sqlite3
class SaveItemPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('zp')

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        cu = self.conn.cursor()
        sql = 'create tabel zp_list(id integer primary key,zwmc varchar(100),gsmc varchar(100),flxx varchar(100),min_zwyx integer,max_zwyx integer,gzdd varchar(100),fbrq varchar(100),gzxz varchar(100),gzjy varchar(100),zdxl varchar(100),zprs integer,zwlb varchar(100),zwms varchar(100),url varchar(100));'
        








