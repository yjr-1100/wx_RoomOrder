#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:53:05
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-17 18:45:23
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\organizations\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
from exts import db
from datetime import datetime


class Organizations(db.Model):
    # 组织id
    orgid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 组织名称
    orgname = db.Column(db.String(64), nullable=True)
    # 组织是否被删除
    # 1 没有被删除 0，被删了
    isdelet = db.Column(db.Integer, default=1)

    def __str__(self):
        return self.rid

    def __init__(self, orgname=""):
        self.orgname = orgname

    def todict(self):
        orgdict = {}
        orgdict['orgname'] = self.orgname
        orgdict['orgid'] = self.orgid
        return orgdict
