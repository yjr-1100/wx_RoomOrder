#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:06:39
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-15 17:17:29
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\orderitem\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from exts import db
from datetime import datetime


class Orderitems(db.Model):

    # 订单号
    oid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 申请时间
    odatetime = db.Column(db.DateTime, default=datetime.now)
    # 申请人id
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    # 申请的教室编号
    room_id = db.Column(db.String(8), db.ForeignKey(
        'rooms.rid'), nullable=False)
    # 教室所属组织
    room2orgid = db.Column(db.Integer, db.ForeignKey(
        'organizations.orgid'), nullable=False)
    # 申请使用时间段
    usingtime = db.Column(db.String(64), nullable=True)
    # 教室的用途
    roomusage = db.Column(db.String(1024), nullable=False)
    # 负责人签字盖章图片
    autograph = db.Column(db.String(1024), nullable=True)
    # -------------------------------------------------------------------------
    # 拒绝理由
    rejectreasion = db.Column(db.String(512), nullable=True)
    # 审核人id
    checker_id = db.Column(
        db.Integer, db.ForeignKey('managers.mid'), nullable=True)

    # 是否审核 审核结果
    # -1 未审核
    # 0  不通过
    # 1  通过
    ostatus = db.Column(db.Integer, default=-1)

    # 审核时间
    ochecktime = db.Column(db.DateTime, nullable=True)

    def __str__(self):
        return self.oid
