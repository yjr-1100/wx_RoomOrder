#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:06:39
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:12:17
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\orderitem\models.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from exts import db
from datetime import datetime

class Orderitems(db.Model):
    oid = db.Column(db.Integer,primary_key = True,autoincrement = True)
    odatetime = db.Column(db.DateTime,default=datetime.now)

    # 是否审核 审核结果
    # -1 未审核
    # 0  不通过
    # 1  通过
    ostatus = db.Column(db.Integer,default=-1)
    
    # 申请人id
    
    # 审核人id

    def __str__(self):
        return self.oid