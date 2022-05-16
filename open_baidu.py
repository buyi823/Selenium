#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-11 21:24:04
# Description: selenium launch browser

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver:
    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser =='firefox':
            self.driver = webdriver.Firefox()
        elif browser =='ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Edge()
        time.sleep(5)
        return self.driver

        

    def get_url(self, url):
        if self.driver != None:
            time.sleep(1)
            self.driver.maximize_window()
            if 'http' in url:
                self.driver.get(url)
            elif 'D' in url:
                self.driver.get(url)
            else:
                print('Your url incorrect')
        else:
            print('case failed.')

    def handle_window(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print("Your parameter is incorrect.")
        time.sleep(3)
        self.driver.quit()

        # driver = open_browser('chrome')
    def assert_title(self, title_name=None):
        '''
        判断title是否正确
        '''
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver) 

    def open_url_is_true(self, url, title_name=None):
        '''
        判断打开的页面是否正确
        '''
        self.get_url(url)
        return self.assert_title(title_name)
    
    def close_driver(self):
        self.driver.close()

    # 切换窗口
    def switch_window(self, title_name=None):
        handle_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handle_list:
            if i != current_window:
                time.sleep(3)
                self.driver.switch_to.window(i)
                ti = EC.title_contains("百度")
                if self.assert_title(title_name):
                    break
        time.sleep(3)
# driver1 = open_browser('chrome')
# driver1.get('http://www.imooc.com')

# handle_window('max')
# time.sleep(3)
# handle_window(200, 300)


if __name__ == '__main__':
    selenium_driver = SeleniumDriver('chrome')
    # selenium_driver.handle_window('max')
    selenium_driver.open_url_is_true('http://www.baidu.com', 'helloworld')
    print(selenium_driver.open_url_is_true('http://www.baidu.com', 'helloworld'))
    selenium_driver.close_driver()
    # selenium_driver.switch_window('网站连接') 








# 将浏览器设置环境变量path,然后将浏览器器driver放在python安装根目录下，可以不用带路径启动浏览器
# driver = webdriver.Chrome("D:\\BrowserDriver\\chromedriver.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 

# firefox不带driver路径反而可以打开，带路径打不开
# Firefox_profile 已经被遗弃了，需要找到一个新的option（对象）。
# 应该是这个路径有问题，通过网上查找资料，我发现这种方法已经不适用了。
# 需要在前面加上一个执行路径：executable_path("  "),然后问题就可以解决了。
# driver = webdriver.Firefox()
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 

# driver = webdriver.Ie("D:\\IEDriverServer\\IEDriverServer.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 

# driver = webdriver.Edge("D:\\edgedriver_win64\\msedgedriver.exe")
# driver.set_window_size(1024, 768)
# driver.get('https:\\www.baidu.com') 