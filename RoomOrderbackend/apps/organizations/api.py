#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:52:57
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-13 14:22:27
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\organizations\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
import re
from flask import Blueprint, request, redirect, render_template, url_for
from pandas import isnull
from apps.organizations.models import Organizations
import settings
from common.result import trueReturn, falseReturn
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import or_, and_
import requests
import json
# from flask_cors import cross_origin
org_bp = Blueprint('orgs', __name__)

# 得到轮播图


@org_bp.route('/getallorg', methods=['GET'])
def getOpenId():
    try:
        orglists = Organizations.query.filter(Organizations.isdelet == 1).all()
        # print(swiperlists)
    except:
        return falseReturn(data=[settings.defaultimage.swiperdefaultimage], msg="database failed")
    allorgs = []
    for org in orglists:
        orgitem = {}
        orgitem['orgid'] = org.orgid
        orgitem['orgname'] = org.orgname
        allorgs.append(orgitem)
    if not allorgs:
        return trueReturn(data=[settings.defaultimage.swiperdefaultimage], msg="no organization")
    else:
        return trueReturn(data=allorgs, msg="success")

# 上传轮播图

# 删除轮播图
