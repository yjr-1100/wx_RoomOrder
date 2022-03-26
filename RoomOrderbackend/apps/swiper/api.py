#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-26 17:47:08
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\swiper\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

import re
from flask import Blueprint,request,redirect,render_template,url_for
from pandas import isnull
from common.result import falseReturn, trueReturn
from apps.swiper.models import Swiper
import settings 
from exts import db
from sqlalchemy import or_
import requests
swiper_bp = Blueprint('swiper',__name__)

# 得到轮播图
@swiper_bp.route('/getswiperimage',methods=['GET'])
def getOpenId():
    try:
        swiperlists = Swiper.query.filter(Swiper.isdelet == 1).all()
        # print(swiperlists)
    except:
        return falseReturn(data=[settings.defaultimage.swiperdefaultimage],msg="database failed")
    swiperurl = []
    for item in swiperlists:
        swiperurl.append(item.surl)
    if not swiperurl:
        return trueReturn(data=[settings.defaultimage.swiperdefaultimage],msg="no swiper image")
    else:
        return trueReturn(data=swiperurl,msg="success")

# 上传轮播图

# 删除轮播图
