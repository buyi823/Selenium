#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-16 12:03:15
# Description: assert title

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.imooc.com")
title_name = driver.title
# 看源码这里的title是个装饰器，python中的装饰器不理解

if '慕课网' in title_name:
    print('open right')
else:
    print('open wrong')

# 
title_a = EC.title_is("慕课网")
print(title_a(driver))
title_b = EC.title_contains("慕课网")
print(title_b(driver))
driver.close()
