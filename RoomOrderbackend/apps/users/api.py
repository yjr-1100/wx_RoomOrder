#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-19 23:02:05
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from flask import Blueprint, request, make_response
from apps.users.models import Users
import settings
from common.result import trueReturn, falseReturn
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import or_, and_
import requests
import json
import os
import datetime
import random
import requests
from settings import defaultimage
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


@user_bp.route('/submitinnerverify', methods=['POST'])
def submitinnerverify():
    data = request.get_json()
    print(data)
    try:
        uid = data['uid']
    except:
        return falseReturn(msg="no uid")
    user = Users.query.filter(Users.uid == uid).first()
    try:
        user.isinsider = 2
        user.orgid = data['orgid']
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    jsonuser = json.dumps(user, cls=AlchemyEncoder)
    dictuser = json.loads(jsonuser)
    return trueReturn(data=dictuser)


# 得到用户信息
@user_bp.route('/getuserinfo', methods=['POST'])
def getuserinfo():
    data = request.get_json()
    print(data)
    try:
        uid = data['uid']
    except:
        return falseReturn(msg="no openid")

    try:
        user = Users.query.filter(Users.uid == uid).first()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    jsonuser = json.dumps(user, cls=AlchemyEncoder)
    dictuser = json.loads(jsonuser)
    return trueReturn(data=dictuser)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def create_uuid():  # 生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
    randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum)
    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum


@user_bp.route('/uploadaccessimage', methods=['POST'])
def uploadaccessimage():
    img = request.files.get('file')
    print(img.filename)
    file_dir = defaultimage.access_UPLOAD_img
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if img and allowed_file(img.filename):
        ext = img.filename.rsplit('.', 1)[1]
        new_filename = create_uuid() + '.' + ext
        file_path = file_dir+new_filename
        img.save(file_path)
        return trueReturn(msg='上传成功', data={'imgurl': defaultimage.showsaccessimgurl+new_filename})
    else:
        return falseReturn(msg='请上传png/jpg图片')


# show photo
@user_bp.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = defaultimage.access_UPLOAD_img
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' %
                              filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
