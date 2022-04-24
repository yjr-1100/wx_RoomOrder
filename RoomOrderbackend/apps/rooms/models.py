#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 14:54:42
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-24 17:35:51
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rooms\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#


from exts import db
from datetime import datetime


class Rooms(db.Model):

    # 房间id
    rid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 房间名称
    rname = db.Column(db.String(64), nullable=False)
    # 房间地址
    raddress = db.Column(db.String(512), nullable=False)
    # 房间描述
    rdescribe = db.Column(db.String(512), nullable=False)
    # 房间照片地址
    rphotoURL = db.Column(db.String(1024), nullable=True,
                          default="http://imgnotes.jerryfirst.top/noroomphoto.jpeg")
    # 房间申请表
    pdfname = db.Column(db.String(1024), nullable=True)
    pdfurl = db.Column(db.String(1024), nullable=True)
    # 房间可用时间
    rcanbeusetimes = db.Column(
        db.String(512), nullable=True, default="8:00-9:00;")
    # 所属组织
    orgid = db.Column(db.Integer, db.ForeignKey(
        'organizations.orgid'), nullable=False)
    # 教室是否被删除 1 没有 0 删了
    isdelet = db.Column(db.Integer, default=1)

    def __str__(self):
        return self.rid
