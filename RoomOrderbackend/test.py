#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-23 10:21:56
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-23 12:08:38
# @FilePath: \wx_RoomOrder\RoomOrderbackend\test.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#
import requests

code2session_url = "https://api.weixin.qq.com/sns/jscode2session"
data = {
    "appid":"wx731a6c18b6b4904d",
    "secret":"2d332b592fddeb2f7f41c11792511b4a",
    "js_code":"013ceh200JTJuN1iYz1009eU0V3ceh2w",
    "grant_type":"authorization_code"
}
# parameters
r = requests.get(code2session_url,params=data)
print(r.text)