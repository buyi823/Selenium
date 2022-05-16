#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-16 15:38:59
# Description: open window

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.imooc.com/user/newlogin/from_url/")
time.sleep(3)
driver.find_element_by_name('email').send_keys('13488359081')
driver.find_element_by_name('password').send_keys('1q2w3e4R')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(3)
# 上面的代码实际运行需要输入验证码，无法跳转
# 下面的完全按照课程示例，实际无法运行
driver.get('https://www.imooc.com/user/setbindsns')
driver.find_element_by_class_name('inner-i-box')[1].find_element_by_class_name('moco-btn-normal').click()

# 不同浏览器的TAB页相当于句柄
hand_list = driver.window_handles
current_handles = driver.current_window_handle
print(hand_list)
time.sleep(15)

for i in hand_list:
    if i != current_handles:
        time.sleep(3)
        driver.switch_to.window(i)
        ti = EC.title_contains("网站连接")
        if ti(driver) == True:
            break
time.sleep(5)
driver.find_element_by_id('userId').send_keys('test')
time.sleep(5)
driver.close()