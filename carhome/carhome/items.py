# -*- coding: utf-8 -*-
import scrapy

class CarhomeItem(scrapy.Item):
    carid = scrapy.Field()
    url = scrapy.Field()
    treeurl = scrapy.Field()
    brand = scrapy.Field()  ###
    brandurl = scrapy.Field()  ###
    brandmodel4 = scrapy.Field()  # "哈弗H5"
    brandmodel5 = scrapy.Field()  # "哈弗H5"
    version = scrapy.Field()  # "经典版 2.0T 手动 两驱 精英型",
    image = scrapy.Field()
    cyear = scrapy.Field()
    ctype = scrapy.Field()  # "SUV"
    color = scrapy.Field()
    price1 = scrapy.Field()  # 厂家指导价
    price2 = scrapy.Field()  # 商家报价
    displacement = scrapy.Field()  # "2.0", 排量(L)
    shiftgears = scrapy.Field()  # "6"
    shifttype = scrapy.Field()  # "手动"
    clength = scrapy.Field()  # 长宽高，为了清楚表示，加了前缀c
    cwidth = scrapy.Field()  # 长宽高，为了清楚表示，加了前缀c
    cheight = scrapy.Field()  # 长宽高，为了清楚表示，加了前缀c
    wheelbase = scrapy.Field()  # 轴距
    mingrounddistance = scrapy.Field()  # 最小离地间隙
    motor = scrapy.Field()  # 发动机型号
    intaketype = scrapy.Field()  # 进气形式
    maxhorsepower = scrapy.Field()  # 最大马力(Ps)
    maxpower = scrapy.Field()  # 最大功率(kW)
    maxrpm = scrapy.Field()  # 最大功率转速(rpm)
    oiltype = scrapy.Field()  # 燃料类型
    oilsupply = scrapy.Field()  # 供油方式
    tankvolume = scrapy.Field()  # 燃油箱容积(L)
    drivetype = scrapy.Field()  # 驱动方式
    braketype = scrapy.Field()  # 驻车制动类型
    frontwheel = scrapy.Field()  # 前轮胎规格
    backwheel = scrapy.Field()  # 后轮胎规格

class carList(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()

class carInfoList(scrapy.Item):
    sourelink=scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()

class linkList(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()