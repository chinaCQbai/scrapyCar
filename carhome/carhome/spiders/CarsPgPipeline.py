#!/usr/bin/env python
# coding=utf-8
import scrapy
import redis
import re
import time
from selenium import webdriver
from carhome.items import CarhomeItem

class CarhomePipeline(scrapy.Spider):
    name = 'carhome'

    def __init__(self):
        super(CarhomePipeline, self).__init__()
        self.allowed_domains = ["bitauto.com"]
        self.start_urls = ['http://car.bitauto.com/quanxinaodia4l/peizhi/']
        #self.driver = webdriver.Firefox()

    # 易车这里的目录总共分为三级 第三级下才有具体信息的链接地址
    # 例如：一级=奥迪 二级=一汽大众奥迪 三级=A3
    # 获取所有的1级链接下的车型相信信息url
    #self.driver.find_elements_by_class_name('mainBrand'):
    #self.driver.find_element_by_xpath('//*[@id="treeList"]//a[@class="mainBrand"]'):
    def parse(self, response):
            #self.driver.get(response.url)
            #page_url=self.driver.find_element_by_xpath('//*[@id="car_tag"]/nav/div/div/ul/li[2]/a').get_attribute('href')
            page_url=response.url
            yield scrapy.Request(url=page_url,
                                 callback=self.parse_detail_page)
            time.sleep(15)
            #self.driver.close()

    def parse_detail_page(self, response):
        # 命令行测试 scrapy shell http://car.bitauto.com/changchengh5/peizhi/

        ff = re.search('\[\[\[.*\]\]\]', response.body).group()  # str
        infos = eval(ff)

        for s_second in infos:
            item = CarhomeItem()

            item['carid'] = s_second[0][0]  # "117388"
            item['url'] = response.url
            item['brand'] = ''  ###
            item['treeurl'] = ''  ###
            item['brandurl'] = s_second[0][6]  ##changchengh5,benchieji
            item['brandmodel4'] = s_second[0][4]  # "哈弗H5" "奔驰E级"
            item['brandmodel5'] = s_second[0][5]  ###
            item['version'] = s_second[0][1]  # "经典版 2.0T 手动 两驱 精英型",
            item['image'] = s_second[0][2]
            item['cyear'] = s_second[0][7]
            item['ctype'] = s_second[0][12]  # "SUV"
            item['color'] = s_second[0][13]
            item['price1'] = s_second[1][0]  # 厂家指导价
            item['price2'] = s_second[1][1]  # 商家报价
            item['displacement'] = s_second[1][5]  # "2.0", 排量(L)
            item['shiftgears'] = s_second[1][6]  # "6"
            item['shifttype'] = s_second[1][7]  # "手动"
            item['clength'] = s_second[2][0]  # 长宽高，为了清楚表示，加了前缀c
            item['cwidth'] = s_second[2][1]  # 长宽高，为了清楚表示，加了前缀c
            item['cheight'] = s_second[2][2]  # 长宽高，为了清楚表示，加了前缀c
            item['wheelbase'] = s_second[2][3]  # 轴距
            item['mingrounddistance'] = s_second[2][8]  # 最小离地间隙
            item['motor'] = s_second[3][1]  # 发动机型号
            item['intaketype'] = s_second[3][5]  # 进气形式
            item['maxhorsepower'] = s_second[3][13]  # 最大马力(Ps)
            item['maxpower'] = s_second[3][14]  # 最大功率(kW)
            item['maxrpm'] = s_second[3][15]  # 最大功率转速(rpm)
            item['oiltype'] = s_second[3][19]  # 燃料类型
            item['oilsupply'] = s_second[3][21]  # 供油方式
            item['tankvolume'] = s_second[3][22]  # 燃油箱容积(L)
            item['drivetype'] = s_second[5][6]  # 驱动方式
            item['braketype'] = s_second[5][5]  # 驻车制动类型
            item['frontwheel'] = s_second[7][0]  # 前轮
            item['backwheel'] = s_second[7][1]  # 后轮
            yield item


