#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-25 23:24:58
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-26 22:51:59
# @FilePath: \wx_RoomOrder\RoomOrderbackend\common\result.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#
from flask import request,Response
import json
import os
def trueReturn(data=None,code=1, msg="", st=True):
    return json.dumps({
        'responsedata': data,
        'code':code,
        'msg': msg,
        'status': st
    })

def falseReturn(data=None,code=0 ,msg="", st=False):
    return json.dumps({
        'responsedata': data,
        'code':code,
        'msg': msg,
        'status': st
    })

def send_file(store_path):
    # store_path = "./Ligandfiles/234665431/120l.pdb"
    with open(store_path, 'rb') as targetfile:
        while 1:
            data = targetfile.read(20 * 1024 * 1024)   # 每次读取20M
            if not data:
                break
            yield data

# 创建文件夹，如果已经存在返回 1 创建成功返回2 创建失败返回 0
def creat_file_path(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return 2
        else:
            return 1
    except:
        return 0