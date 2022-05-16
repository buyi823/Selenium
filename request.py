#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-12 20:15:43
# Description: request study

import requests
import json

class requests_webdriver:
    def __init__(self):
        self.driver = self.chrome_driver()

    def chrome_driver(self):
        url = "http://127.0.0.1:4444/wd/hub/session/"
        data = json.dumps({
            "Capabilities": {
                "browserName": "chrome"
            }
        })
        # requests.post(url, data)
        res = requests.post(url, data).json()
        session = res['sessionId']
        driver = url + session
        return driver

    def get_url(self, url):
        base_url = self.driver + '/url'
        data = json.dumps({
            "url": url
        })
        requests.post(base_url, data)

    def find_element_by_id(self, value):
        base_url = self.driver + '/element'
        data = json.dumps({
            "using": 'name',
            "value": value
        })
        res = requests.post(base_url, data).json()['value']['element-6066-11e4-a52e-4f735466cecf']
        print(res)

if __name__ == '__main__':
    request_driver = requests_webdriver()
    request_driver.get_url('https://www.imooc.com/user/newlogin/from_url/')
    request_driver.find_element_by_id('email')