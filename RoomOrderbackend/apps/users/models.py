#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 15:53:04
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-13 21:46:49
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#


from exts import db
from datetime import datetime


class Users(db.Model):
    # ---------------------------------------------------------------
    # 用户id
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户openid 28位，我们多给几位
    uopenid = db.Column(db.String(64), nullable=True)
    # 昵称
    nickname = db.Column(db.String(64), nullable=True)
    # 头像
    avatarUrl = db.Column(db.String(1024), nullable=True)
    # ----------------------------------------------------------
    # 姓名
    uname = db.Column(db.String(64), nullable=True)
    # 手机号
    uphonenum = db.Column(db.String(15), nullable=True)
    # 学号
    schoolid = db.Column(db.String(64), nullable=True)
    # 专业班级
    profassionclass = db.Column(db.String(256), nullable=True)
    # ------------------------------------------------------------
    # 所属组织
    orgid = db.Column(db.Integer, db.ForeignKey(
        'organizations.orgid'), nullable=True)
    # 是否内部人员认证 0:NO 1:YES -1拒绝申请 2 提交申请
    isinsider = db.Column(db.Integer, default=0)
    # 是否完善身份信息 就是填写姓名学号手机号等 0:NO 1:YES
    isbasaceinfo = db.Column(db.Integer, default=0)
    # 是否阅读借阅须知 0:NO 1:YES
    isreadedrules = db.Column(db.Integer, default=0)

    def __str__(self):
        return self.rid

    def __init__(self, uopenid="", nickname="", avatarUrl=""):
        self.uopenid = uopenid
        self.nickname = nickname
        self.avatarUrl = avatarUrl

    def todict(self):
        userdict = {}
        userdict['uid'] = self.uid
        userdict['uopenid'] = self.uopenid
        userdict['nickname'] = self.nickname
        userdict['avatarUrl'] = self.avatarUrl
        userdict['uname'] = self.uname
        userdict['uphonenum'] = self.uphonenum
        userdict['schoolid'] = self.schoolid
        userdict['profassionclass'] = self.profassionclass
        userdict['isinsider'] = self.isinsider
        userdict['isbasaceinfo'] = self.isbasaceinfo
        userdict['isreadedrules'] = self.isreadedrules
        return userdict
