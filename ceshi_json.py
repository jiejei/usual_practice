#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import random


class Mingrenmingyan:
    """
    处理名人名言接口返回的数据
    """
    def __init__(self):
        """
        初始化相关数据,包括接口的url,headers和parm
        :return: None
        """
        self.url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=218.4.255.255'
        self.headers = {"apikey": "your key"}
        self.parm = {
            "dtype": "JSON",
            "keyword": "人生",
            "page": "1",
            "rows": "10"
        }

    def get_mrmy(self):
        """
        从接口获取名人名言数据,随机选取一条返回,返回json数据.
        :return:json, 名人名言数据
        """
        wb_data = requests.get(self.url, headers=self.headers, params=self.parm)
        data = wb_data.json()
        if data['error_code'] == 0:
            result = data['result']
            random_num = random.randint(0, 19)
            return json.dumps(result[random_num])
        else:
            return json.dumps(data)








