#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:58:57
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-17 20:38:19
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\managers\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:53:05
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-13 13:57:47
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\organizations\models.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
from exts import db
from datetime import datetime


class Managers(db.Model):
    # 管理员id
    mid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 管理员等级 管理员 1 超级管理员 2
    mlevel = db.Column(db.Integer, default=1)
    # 管理员名称
    mname = db.Column(db.String(64), nullable=False)
    # 管理员密码
    mpassword = db.Column(db.String(128), nullable=False)
    # 管理员手机号
    mphonenum = db.Column(db.String(15), nullable=False)
    # 管理员所属组织
    m2org = db.Column(db.Integer, nullable=False)
    # 组织是否被删除
    # 1 没有被删除 0，被删了
    isdelet = db.Column(db.Integer, default=1)

    def __str__(self):
        return self.rid

    def todict(self):
        managerdict = {}
        managerdict['mid'] = self.mid
        managerdict['mlevel'] = self.mlevel
        managerdict['mname'] = self.mname
        managerdict['mphonenum'] = self.mphonenum
        managerdict['m2org'] = self.m2org

        return managerdict
