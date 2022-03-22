#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 15:53:04
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:12:50
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\models.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#


from exts import db
from datetime import datetime

class Users(db.Model):
    uid = db.Column(db.String(8),primary_key = True)
    uname = db.Column(db.String(64),nullable=False)
    uphonenum = db.Column(db.Integer,nullable = False)
    schoolid = db.Column(db.String(64),nullable = False)
    profassionclass = db.Column(db.String(256),nullable = True)

    def __str__(self):
        return self.rid