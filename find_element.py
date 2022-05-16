#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-16 23:03:19
# Description: locate element

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.imooc.com')

element = driver.find_element_by_name('password')
element.send_keys('input something')
