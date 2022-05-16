#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-16 16:46:56
# Description: switch window study 
# 切换到百度TAB页，然后输入test

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://www.qq.com')
time.sleep(20)

handle_list = driver.window_handles
current_window = driver.current_window_handle

# switch_to.window()方法的使用
# handles = driver.window_handles  # 获取当前浏览器的所有窗口句柄
# driver.switch_to.window(handles[-1]) # 切换到最新打开的窗口
# driver.switch_to.window(handles[-2]) # 切换到倒数第二个打开的窗口
# driver.switch_to.window(handles[0])  # 切换到最开始打开的窗口

for i in handle_list:
    if i != current_window:
        time.sleep(3)
        driver.switch_to.window(i)
        ti = EC.title_contains("百度")
        if ti(driver) == True:
            break
time.sleep(5)
driver.find_element_by_id('kw').send_keys('test')
time.sleep(5)
driver.close()
