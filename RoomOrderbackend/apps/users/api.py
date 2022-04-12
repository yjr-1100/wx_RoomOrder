#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-12 22:20:11
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

import re
from flask import Blueprint, request, redirect, render_template, url_for
from pandas import isnull
from apps.users.models import Users
import settings
from common.result import trueReturn, falseReturn
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import or_, and_
import requests
import json
# from flask_cors import cross_origin
user_bp = Blueprint('users', __name__)


# 得到用户的openid


@user_bp.route('/getopenid', methods=['GET'])
def getOpenId():
    code = request.args.get('code')
    code2session_url = "https://api.weixin.qq.com/sns/jscode2session"
    data = {
        "appid": settings.wxappConfig.appid,
        "secret": settings.wxappConfig.appsecret,
        "js_code": code,
        "grant_type": "authorization_code"
    }
    # parameters
    r = requests.get(code2session_url, params=data)
    print(r.json())
    return r.json()

# 授权后更新用户信息


@user_bp.route('/updateuser', methods=['POST'])
def updateuser():
    # application/jso
    data = request.get_json()
    try:
        uopenid = data['openid']
    except:
        return falseReturn(msg="no openid")
    print(uopenid)
    nickname = data['nickName']
    avatarurl = data['avatarUrl']

    user = Users.query.filter(Users.uopenid == uopenid).first()
    if not user:
        user = Users(uopenid=uopenid, nickname=nickname, avatarUrl=avatarurl)
        db.session.add(user)
        db.session.commit()
        return trueReturn(data=user.todict())
    else:
        jsonuser = json.dumps(user, cls=AlchemyEncoder)
        dictuser = json.loads(jsonuser)
        return trueReturn(data=dictuser)


# 授权阅读预约规则
@user_bp.route('/modifyreaded', methods=['POST'])
def userhaveread():
    data = request.get_json()
    try:
        uopenid = data['openid']
    except:
        return falseReturn(msg="no openid")
    user = Users.query.filter(Users.uopenid == uopenid).first()
    try:
        user.isreadedrules = 1
        db.session.commit()
    except:
        return falseReturn(msg="数据库错误")
    jsonuser = json.dumps(user, cls=AlchemyEncoder)
    dictuser = json.loads(jsonuser)
    return trueReturn(data=dictuser)

# 授权后用户编辑个人信息


@user_bp.route('/edituserinfo', methods=['POST'])
def edituserinfo():
    data = request.get_json()
    print(data)
    try:
        uopenid = data['openid']
    except:
        return falseReturn(msg="no openid")
    user = Users.query.filter(Users.uopenid == uopenid).first()
    try:
        user.isbasaceinfo = 1
        user.uname = data['uname']
        user.uphonenum = data['uphonenum']
        user.schoolid = data['schoolid']
        user.profassionclass = data['profassionclass']
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    jsonuser = json.dumps(user, cls=AlchemyEncoder)
    dictuser = json.loads(jsonuser)
    return trueReturn(data=dictuser)

# isinsider
# 内部人员认证

# 管理员登录


@user_bp.route('/managerlogin', methods=['POST'])
def managerlogin():
    data = request.get_json()
    print(data)
    try:
        username = data['username']
        password = data['password']
    except:
        return falseReturn(msg="缺少必要参数")
    user = Users.query.filter(
        and_(Users.uphonenum == username, Users.upassword == password)).first()
    if user is None:
        return trueReturn(data='', code=0, msg='用户名或密码错误')
    try:
        jsonuser = json.dumps(user, cls=AlchemyEncoder)
        dictuser = json.loads(jsonuser)
        print(dictuser)
        return trueReturn(data=dictuser)
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
