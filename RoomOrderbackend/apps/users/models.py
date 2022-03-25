#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 15:53:04
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-25 23:39:45
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\models.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#


from exts import db
from datetime import datetime

class Users(db.Model):
    # 用户id 28位，我们多给几位
    uid = db.Column(db.String(64),primary_key = True)
    # 用户名
    uname = db.Column(db.String(64),nullable=True)
    # 昵称
    nickname =db.Column(db.String(64),nullable=True)
    # 头
    avatarUrl =db.Column(db.String(1024),nullable=True)
    # 手机号
    uphonenum = db.Column(db.Integer,nullable = True)
    # 学号
    schoolid = db.Column(db.String(64),nullable = True)
    # 专业班级
    profassionclass = db.Column(db.String(256),nullable = True)
    # 是否内部人员认证 0:NO 1:YES
    isinsider = db.Column(db.Integer,default = 0)
    # 是否完善身份信息 就是填写姓名学号手机号等 0:NO 1:YES
    isbasaceinfo = db.Column(db.Integer,default = 0)
    # 是否阅读借阅须知
    isreadedrules = db.Column(db.Integer,default = 0)
    

    def __str__(self):
        return self.rid
    
    def __init__(self,uid="",uname="",nickname="",avatarUrl="",uphonenum=-1,schoolid="",profassionclass="",isinsider=0,isbasaceinfo=0,isreadedrules=0):
        self.uid = uid
        self.uname = uname
        self.nickname = nickname
        self.avatarUrl = avatarUrl
        self.uphonenum = uphonenum
        self.schoolid = schoolid
        self.profassionclass = profassionclass
        self.isinsider = isinsider
        self.isbasaceinfo = isbasaceinfo
        self.isreadedrules = isreadedrules










