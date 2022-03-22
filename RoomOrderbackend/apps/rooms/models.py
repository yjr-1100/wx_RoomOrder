#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 14:54:42
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:12:42
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rooms\models.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#


from exts import db
from datetime import datetime

class Rooms(db.Model):
    rid = db.Column(db.String(8),primary_key = True)
    rname = db.Column(db.String(64),nullable=False)
    raddress = db.Column(db.String(512),nullable = False)
    rdescribe = db.Column(db.String(512),nullable = False)
    rphotoURL = db.Column(db.String(1024),nullable = True)

    def __str__(self):
        return self.rid