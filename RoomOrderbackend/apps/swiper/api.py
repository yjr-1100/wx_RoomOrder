#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-19 15:46:22
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\swiper\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from flask import Blueprint, request, make_response
from common.result import falseReturn, trueReturn
from common.tooken import certify_token
from apps.swiper.models import Swiper
from apps.managers.models import Managers
import settings
from exts import db
from sqlalchemy import or_
from settings import defaultimage
import os
import datetime
import random
swiper_bp = Blueprint('swiper', __name__)

# 得到轮播图


@swiper_bp.route('/getswiperimage', methods=['GET'])
def getOpenId():
    try:
        swiperlists = Swiper.query.filter(Swiper.isdelet == 1).all()
    except:
        return falseReturn(data=[settings.defaultimage.swiperdefaultimage], msg="database failed")
    swiperurl = []
    for item in swiperlists:
        swiperurl.append(item.surl)
    if not swiperurl:
        return trueReturn(data=[settings.defaultimage.swiperdefaultimage], msg="no swiper image")
    else:
        return trueReturn(data=swiperurl, msg="success")

# 上传轮播图


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


@swiper_bp.route('/uploadswiperimage', methods=['POST'])
def uploadrooomimage():
    img = request.files.get('file')
    print(img.filename)
    file_dir = defaultimage.swiper_UPLOAD_img
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if img and allowed_file(img.filename):
        ext = img.filename.rsplit('.', 1)[1]
        new_filename = create_uuid() + '.' + ext
        file_path = file_dir+new_filename
        img.save(file_path)
        swip = Swiper()
        swip.surl = defaultimage.showswiperimgurl+new_filename
        try:
            db.session.add(swip)
            db.session.commit()
        except:
            return falseReturn(msg="数据库错误")
        return trueReturn(msg='上传成功', data={'imgurl': defaultimage.showswiperimgurl+new_filename})
    else:
        return falseReturn(msg='请上传png/jpg图片')


# show photo
@swiper_bp.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = defaultimage.swiper_UPLOAD_img
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' %
                              filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response

# 删除轮播图


@swiper_bp.route('/rmswiperimage', methods=['POST'])
def rmswiperimage():
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
        url = data['url']
    except:
        return falseReturn(msg="缺少必要参数")

    try:
        swip = Swiper.query.filter(Swiper.surl == url).first()
    except:
        return falseReturn(msg="数据库错误")
    swip.isdelet = 0

    try:
        db.session.commit()
    except:
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="删除成功")
