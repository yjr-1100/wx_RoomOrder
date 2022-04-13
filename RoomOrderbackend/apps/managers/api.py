#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:58:40
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-13 23:51:57
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\managers\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
import re
from flask import Blueprint, request, redirect, render_template, url_for
from pandas import isnull
from apps.managers.models import Managers
from apps.users.models import Users
import settings
from common.result import trueReturn, falseReturn
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import or_, and_
import requests
import json
# from flask_cors import cross_origin
manager_bp = Blueprint('managers', __name__)

# 管理员登录


@manager_bp.route('/managerlogin', methods=['POST'])
def managerlogin():
    data = request.get_json()
    print(data)
    try:
        username = data['username']
        password = data['password']
    except:
        return falseReturn(msg="缺少必要参数")
    user = Managers.query.filter(
        and_(Managers.mphonenum == username, Managers.mpassword == password)).first()
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


# 获取管理的所有人员


@manager_bp.route('/getpeople', methods=['Get'])
def getrooms():
    try:
        # request.get_json()
        orgid = request.args.get('orgid')
        # print(orgid)
    except:
        orgid = -1
    try:
        perplelist = Users.query.filter(and_(Users.orgid == orgid, and_(
            Users.isinsider != 0, Users.isinsider != -1))).all()
    except:
        return falseReturn(msg="拉取组织成员信息错误", code=-1)

    personlist = []
    for p in perplelist:
        dictuser = {}
        dictuser['uid'] = p.uid
        dictuser['nickname'] = p.nickname
        dictuser['uname'] = p.uname
        dictuser['uphonenum'] = p.uphonenum
        dictuser['schoolid'] = p.schoolid
        dictuser['profassionclass'] = p.profassionclass
        dictuser['isinsider'] = p.isinsider
        personlist.append(dictuser)
    return trueReturn(data=personlist)


# 操作组织成员状态
@manager_bp.route('/updateinnerpersonstate', methods=['POST'])
def updateinnerpersonstate():
    data = request.get_json()
    try:
        uid = data['uid']
        status = data['status']
    except:
        return falseReturn(msg="no uid")
    user = Users.query.filter(Users.uid == uid).first()
    try:
        user.isinsider = status
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="修改成功")
