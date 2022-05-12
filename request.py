#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine
# Time: 2022-05-12 20:15:43
# Description: request study

import requests
import json

url = "http://127.0.0.1:4444/wd/hub/session"
data = json.dumps({
    "Capabilities": {
        "browserName": "chrome"

    }
})

# requests.post(url, data)
print(requests.post(url, data).json())