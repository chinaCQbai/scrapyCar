#!/usr/bin/env python
# coding=utf-8
import scrapy
from selenium import webdriver
from carhome.items import carList

class carLink(scrapy.Spider):
    name = 'carLink'

    def __init__(self):
        super(carLink, self).__init__()
        self.allowed_domains = ["bitauto.com"]
        self.start_urls = ["http://car.bitauto.com/"]
        self.driver = webdriver.Firefox()

    # 获取所有的1级链接
    #self.driver.find_elements_by_class_name('mainBrand'):
    #self.driver.find_element_by_xpath('//*[@id="treeList"]//a[@class="mainBrand"]'):
    def parse(self, response):
        self.driver.get(response.url)
        item = carList()
        for list1 in self.driver.find_elements_by_xpath('//*[@id="treeList"]//a[@class="mainBrand"]'):
            item['url']=list1.get_attribute('href')
            item['name']=list1.get_attribute('innerText')
            #list1.click()
            yield item
        self.driver.close()

