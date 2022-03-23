#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-23 11:21:29
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Blueprint,request,redirect,render_template,url_for
from apps.users.models import Users
import settings 
import hashlib
from exts import db
from sqlalchemy import or_
import requests
user_bp = Blueprint('users',__name__)


@user_bp.route('/getopenid',methods=['GET'])
def getOpenId():
    code2session_url = "https://api.weixin.qq.com/sns/jscode2session"
    data = {
        "appid" : settings.wxappConfig.appid,
        "secret" : settings.wxappConfig.appsecret,
        "js_code":"013ceh200JTJuN1iYz1009eU0V3ceh2w",
        "grant_type":"authorization_code"
    }
    # parameters
    r = requests.get(code2session_url,params=data)
        
    return r