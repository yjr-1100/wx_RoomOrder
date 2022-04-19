#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:52:57
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-19 15:47:39
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\organizations\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
import re
from flask import Blueprint, request
from apps.organizations.models import Organizations
import settings
from common.result import trueReturn, falseReturn
from exts import db
from common.tooken import generate_token, certify_token
from apps.managers.models import Managers
from apps.users.models import Users
from sqlalchemy import or_, and_
import requests
import json
# from flask_cors import cross_origin
org_bp = Blueprint('orgs', __name__)

# 得到所有的组织


@org_bp.route('/getallorg', methods=['GET'])
def getallorg():
    try:
        orglists = Organizations.query.filter(Organizations.isdelet == 1).all()
        # print(swiperlists)
    except:
        return falseReturn(msg="database failed")
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

# 添加组织


@org_bp.route('/addorg', methods=['POST'])
def addorg():
    data = request.get_json()
    try:
        tooken = data['tooken']
        mid = data['mid']
        orgname = data['orgname']
    except:
        return falseReturn(msg="缺少必要参数")
    mpwd = Managers.query.get(mid).mpassword
    mphonenum = Managers.query.get(mid).mphonenum
    if not certify_token(str(mphonenum)+str(mpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    org = Organizations(orgname=orgname)
    try:
        db.session.add(org)
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="添加失败")
    return trueReturn(msg="添加成功")


# 删除组织
@org_bp.route('/rmorg', methods=['POST'])
def rmorg():
    data = request.get_json()
    print(data)
    try:
        tooken = data['tooken']
        mid = data['mid']
        orgid = data['orgid']
    except:
        return falseReturn(msg="缺少必要参数")
    mpwd = Managers.query.get(mid).mpassword
    mphonenum = Managers.query.get(mid).mphonenum
    if not certify_token(str(mphonenum)+str(mpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    org = Organizations.query.filter(Organizations.orgid == orgid).first()
    managerlists = Managers.query.filter(
        and_(Managers.isdelet == 1, Managers.m2org == orgid)).all()
    perplelist = Users.query.filter(Users.orgid == orgid).all()
    for m in managerlists:
        m.isdelet = 0
    for p in perplelist:
        p.isdelet = 0
    org.isdelet = 0
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="删除失败")
    return trueReturn(msg="删除成功")
