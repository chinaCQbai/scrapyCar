#!/usr/bin/env python
# coding=utf-8
import scrapy
import MySQLdb
import time
from selenium import webdriver
from carhome.items import carInfoList

class carLink(scrapy.Spider):
    name = 'carInfoLink'

    def __init__(self):
        super(carLink, self).__init__()
        # 获取所有的1级链接
        urllist=[]
        conn = MySQLdb.connect(user='root', passwd='gaoxia', db='cardb', host='120.24.229.126', charset="utf8",
                               use_unicode=True)
        cursor = conn.cursor()
        sql = 'SELECT url FROM carlist limit 2'
        cursor.execute(sql)
        info=cursor.fetchall()
        for i in info:
            urllist.append(i[0])
        self.allowed_domains = ["bitauto.com"]
        self.start_urls = urllist

    #self.driver.find_elements_by_class_name('mainBrand'):
    #self.driver.find_element_by_xpath('//*[@id="treeList"]//a[@class="mainBrand"]'):
    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)
        item = carInfoList()
        for list in driver.find_elements_by_xpath('//*[@id="divCsLevel_0"]//div[@class="col-xs-3"]'):
            item['sourelink']=response.url
            item['url'] = list.find_element_by_xpath('.//div[@class="img"]/a').get_attribute('href')
            item['name'] = list.find_element_by_xpath('.//div[@class="img"]/a').get_attribute('title')
            yield item
        time.sleep(15)
        driver.close()

