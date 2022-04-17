#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 15:53:04
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-17 23:02:49
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rules\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#


from exts import db
from datetime import datetime


class Rule(db.Model):
    ruid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rutext = db.Column(db.String(2048), nullable=True)
    # 1 没有被删除 0，被删了
    isdelet = db.Column(db.Integer, default=1)
