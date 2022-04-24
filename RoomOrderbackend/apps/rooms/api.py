#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:23:51
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-24 17:56:48
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rooms\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from flask import Blueprint, request,  make_response, send_from_directory
from common.result import trueReturn, falseReturn
from apps.rooms.models import Rooms
from exts import db
from settings import defaultimage
import os
import datetime
import random
from sqlalchemy import or_, and_
rooms_bp = Blueprint('rooms', __name__)

# 获取所有教室


@rooms_bp.route('/getrooms', methods=['Get'])
def getrooms():
    try:
        orgid = request.args.get('orgid')
    except:
        orgid = -1
    if orgid is None:
        try:
            rooms = Rooms.query.filter(Rooms.isdelet == 1).all()
        except:
            return falseReturn(msg="拉取教室信息错误", code=-1)

    else:
        try:
            rooms = Rooms.query.filter(
                and_(Rooms.isdelet == 1, Rooms.orgid == orgid)).all()
        except:
            return falseReturn(msg="拉取教室信息错误", code=-1)
    roomlist = []
    for room in rooms:
        print(room.rphotoURL.split(';'))
        rinfo = {}
        rinfo['rid'] = room.rid
        rinfo['orgid'] = room.orgid
        rinfo['name'] = room.rname
        rinfo['adress'] = room.raddress
        rinfo['describe'] = room.rdescribe
        rinfo['pdfname'] = room.pdfname
        rinfo['pdfurl'] = room.pdfurl
        rinfo['imageurl'] = room.rphotoURL.split(';')
        rinfo['rcanbeusetimes'] = room.rcanbeusetimes.split(';')
        roomlist.append(rinfo)
    return trueReturn(data=roomlist)


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


@rooms_bp.route('/uploadrooomimage', methods=['POST'])
def uploadrooomimage():
    img = request.files.get('file')
    print(img.filename)
    file_dir = defaultimage.room_UPLOAD_img
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if img and allowed_file(img.filename):
        ext = img.filename.rsplit('.', 1)[1]
        new_filename = create_uuid() + '.' + ext
        file_path = file_dir+new_filename
        img.save(file_path)
        return trueReturn(msg='上传成功', data={'imgurl': defaultimage.showroomimgurl+new_filename})
    else:
        return falseReturn(msg='请上传png/jpg图片')


# show photo
@rooms_bp.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = defaultimage.room_UPLOAD_img
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' %
                              filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


@rooms_bp.route('/uploadroompdf', methods=['POST'])
def uploadroompdf():
    pdf = request.files.get('file')
    print(pdf.filename)
    file_dir = defaultimage.room_UPLOAD_pdf
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if pdf and ('.' in pdf.filename and pdf.filename.rsplit('.', 1)[1] == 'pdf'):
        ext = pdf.filename.rsplit('.', 1)[1]
        # oldname = pdf.filename.rsplit('.', 1)[0]
        new_filename = create_uuid() + '.' + ext
        file_path = file_dir+new_filename
        pdf.save(file_path)
        return trueReturn(msg='上传成功', data={'pdfurl': defaultimage.dowloadroompdf+new_filename})
    else:
        return falseReturn(msg='请上传pdf文件')


@rooms_bp.route('/getroompdf/<string:filename>', methods=['GET'])
def getroompdf(filename):
    # 判断有有无此文件夹
    path = os.path.isfile(os.path.join(defaultimage.room_UPLOAD_pdf, filename))
    if path:
        response_file = send_from_directory(
            defaultimage.room_UPLOAD_pdf, filename=filename, as_attachment=True, attachment_filename=filename)
        response_file.headers["Content-Disposition"] = "attachment; filename=%s" % filename.encode(
        ).decode('latin-1')
        return response_file
    else:
        return falseReturn(msg="文件不存在")
