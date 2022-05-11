#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-11 21:24:04
# Description: selenium launch browser

from selenium import webdriver

# 将浏览器设置环境变量path,然后将浏览器器driver放在python安装更目录下，可以不用带路径启动浏览器
# driver = webdriver.Chrome("D:\\BrowserDriver\\chromedriver.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 



# firefox不带driver路径反而可以打开，带路径打不开
driver = webdriver.Firefox("C:\\python\\geckodriver.exe")
driver.set_window_size(1024, 768)
driver.get('https:\\www.baidu.com') 

# driver = webdriver.Ie("D:\\IEDriverServer\\IEDriverServer.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 

# driver = webdriver.Edge("D:\\edgedriver_win64\\msedgedriver.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 