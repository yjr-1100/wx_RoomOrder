#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:58:40
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-24 17:55:16
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\managers\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
from flask import Blueprint, request
from apps.managers.models import Managers
from apps.organizations.models import Organizations
from apps.users.models import Users
from apps.rooms.models import Rooms
from common.result import trueReturn, falseReturn
from common.tooken import generate_token, certify_token
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import null, or_, and_, true
import json
# from flask_cors import cross_origin
manager_bp = Blueprint('managers', __name__)

# 管理员登录


@manager_bp.route('/managerlogin', methods=['POST'])
def managerlogin():
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
    except:
        return falseReturn(msg="缺少必要参数")
    tooken = generate_token(str(username)+str(password), 7200)
    user = Managers.query.filter(
        and_(Managers.mphonenum == username, Managers.mpassword == password)).first()
    if user is None:
        return trueReturn(data='', code=0, msg='用户名或密码错误')
    try:
        jsonuser = json.dumps(user, cls=AlchemyEncoder)
        dictuser = json.loads(jsonuser)
        print(dictuser)
        return trueReturn(data={'dictuser': dictuser, 'tooken': tooken})
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
        if status == 0:
            user.orgid = None
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="修改成功")


# 修改教室
@manager_bp.route('/updaterooms', methods=['POST'])
def updaterooms():
    data = request.get_json()
    print(data)
    try:
        isnewroom = data['isnewroom']
    except:
        return falseReturn(msg="缺少必要参数")
    if isnewroom == 1:
        room = Rooms()
        room.orgid = data['orgid']
    else:
        room = Rooms.query.filter(Rooms.rid == data['rid']).first()

    room.rname = data['name']
    room.raddress = data['adress']
    room.rdescribe = data['describe']
    room.pdfname = data['pdfname']
    room.pdfurl = data['pdfurl']
    room.rphotoURL = ';'.join(data['imageurl'])
    room.rcanbeusetimes = ';'.join(data['rcanbeusetimes'])
    try:
        if isnewroom == 1:
            db.session.add(room)
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="操作成功")

# 得到所有管理员


@manager_bp.route('/getallmanager', methods=['POST'])
def getallmanager():
    data = request.get_json()
    try:
        tooken = data['tooken']
        mid = data['mid']
    except:
        return falseReturn(msg="登录过期，请重新登录1")
    mpwd = Managers.query.get(mid).mpassword
    mphonenum = Managers.query.get(mid).mphonenum
    if not certify_token(str(mphonenum)+str(mpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    try:
        managerlists = Managers.query.filter(
            and_(Managers.isdelet == 1, Managers.m2org != 1)).all()
        # print(swiperlists)
    except:
        return falseReturn(msg="database failed")
    allmanagers = []
    for m in managerlists:
        manageritem = {}
        manageritem['mid'] = m.mid
        manageritem['mpassword'] = m.mpassword
        manageritem['mphonenum'] = m.mphonenum
        manageritem['mname'] = m.mname
        manageritem['m2org'] = m.m2org
        manageritem['orgname'] = Organizations.query.get(m.m2org).orgname
        allmanagers.append(manageritem)
    if not allmanagers:
        return trueReturn(msg="no manager")
    else:
        return trueReturn(data=allmanagers, msg="success")

# 删除管理员


@manager_bp.route('/rmmanager', methods=['POST'])
def rmmanager():
    data = request.get_json()
    print(data)
    try:
        tooken = data['tooken']
        optmid = data['optmid']
    except:
        return falseReturn(msg="登录过期，请重新登录1")
    optmpwd = Managers.query.get(optmid).mpassword
    optmphonenum = Managers.query.get(optmid).mphonenum
    if not certify_token(str(optmphonenum)+str(optmpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    try:
        mid = data['mid']
        optm2org = data['optm2org']
    except:
        return falseReturn(msg="缺少必要参数")

    if optm2org != 1:
        return falseReturn(msg="权限不足")
    else:
        try:
            m = Managers.query.filter(Managers.mid == mid).first()
        except:
            return falseReturn(msg="数据库错误")
        m.isdelet = 0
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return falseReturn(msg="删除失败")
        return trueReturn(msg="操作成功")


# 添加管理员
@manager_bp.route('/addmanager', methods=['POST'])
def addmanager():
    data = request.get_json()
    print(data)
    try:
        tooken = data['tooken']
        optmid = data['optmid']
        isnew = data['isnew']
    except:
        return falseReturn(msg="登录过期，请重新登录1")
    optmpwd = Managers.query.get(optmid).mpassword
    optmphonenum = Managers.query.get(optmid).mphonenum
    if not certify_token(str(optmphonenum)+str(optmpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    if isnew:
        manager = Managers()
    else:
        mid = data['mid']
        manager = Managers.query.filter(Managers.mid == mid).first()
    manager.mname = data['mname']
    manager.mpassword = data['mpassword']
    manager.mphonenum = data['mphonenum']
    manager.m2org = data['m2org']

    try:
        if isnew:
            db.session.add(manager)
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="操作成功")
