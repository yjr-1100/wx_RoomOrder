#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-17 15:14:27
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-17 15:31:24
# @FilePath: \wx_RoomOrder\RoomOrderbackend\common\tooken.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

import time
import base64
import hmac

from pip import main

'''
@Args:
  key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
  expire: int(最大有效时间，单位为s)
@Return:
  state: str
'''


def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


'''
@Args:
  key: str
  token: str
@Returns:
  boolean
'''


def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True


if __name__ == 'main':
    key = "JD98Dskw=23njQndW9D"
    # 一小时后过期
    token = generate_token(key, 3600)
    certify_token(key, token)
