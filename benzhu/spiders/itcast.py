# -*- coding: utf-8 -*-

import scrapy
import json
from ..items import VirmachItem
from ..email import BenzhuEmail
from ..file import JsonFile
from ..message import Message


class ItcastSpider(scrapy.Spider):
    #爬虫的名字 必须是唯一的
    name = 'virmach'
    #是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    allowed_domains = ['virmach.com']
    #爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    start_urls = ['https://billing.virmach.com/modules/addons/blackfriday/new_plan.json']

    #解析的方法，每个初始URL完成下载后将被调用
    def parse(self, response):
        if(response.text == 'None' or response.text == ""):
            print("获取内容失败")
        else:
            #获取上一次number的数据
            jsonFile = JsonFile()
            oldnumber = jsonFile.getJsonFile();
            print("上一次查询的价格为："+str(oldnumber))
            #把表更新为最新的数据
            jsonFile.setJsonFile(response)
            #解析json数据
            jsobj = json.loads(response.body)
            #获取数据模型
            item = VirmachItem()
            #放入数据
            price = str(jsobj['price'])
            newprice = price[1:price.index(' ')]
            print("本次查询的价格为："+newprice)
            item['price'] = newprice
            item['virt'] = str(jsobj['virt'])
            item['ram'] = str(jsobj['ram'])
            item['cpu'] = str(jsobj['cpu'])
            item['hdd'] = str(jsobj['hdd'])
            item['bw'] = str(jsobj['bw'])
            item['ips'] = str(jsobj['ips'])
            addres = str(jsobj['location'])
            item['addres'] = addres
            #获取价格小数点之前的位数 判断价格是否小于等于15元
            number = price[1:price.index(".")]
            JsonFile.textLog(newprice,oldnumber,item)
            if(int(number) <=15 and oldnumber!=newprice):
                #小于15元 发送邮件
                benzhuEmail = BenzhuEmail()
                benzhuEmail.send(item)
                if (addres == 'CHICAGO, IL' or addres == 'PISCATAWAY, NJ' or addres =='SAN JOSE, CA' or addres == 'San Jose, CA'):
                    #等于这三个地区的话就发送短信
                    message = Message()
                    #message.sendMessage(newprice)
                    #发送微信提醒
                    #message.sendServerFtqq(item)