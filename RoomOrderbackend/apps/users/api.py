#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-26 00:00:35
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

import re
from flask import Blueprint,request,redirect,render_template,url_for
from pandas import isnull
from apps.users.models import Users
import settings 
import hashlib
from exts import db
from sqlalchemy import or_
import requests
user_bp = Blueprint('users',__name__)

# 得到用户的openid
@user_bp.route('/getopenid',methods=['GET'])
def getOpenId():
    code = request.args.get('code')
    code2session_url = "https://api.weixin.qq.com/sns/jscode2session"
    data = {
        "appid" : settings.wxappConfig.appid,
        "secret" : settings.wxappConfig.appsecret,
        "js_code": code,
        "grant_type":"authorization_code"
    }
    # parameters
    r = requests.get(code2session_url,params=data)
    print(r.json())
    return r.json()

# 更新用户信息
@user_bp.route('/updateuser',methods=['POST'])
def updateuser():
    # application/jso
    data = request.get_json()
    uid = data['openid']
    print(uid)
    nickname = data['nickName']
    avatarurl = data['avatarUrl']
    user = Users.query.get(uid)
    if not user :
        user = Users(uid=uid,nickname=nickname,avatarUrl=avatarurl)
        db.session.add(user)
        db.session.commit()
    else:
        pass
        user.schoolid="123"
        db.session.commit()

    return "12"
