#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-04-13 13:58:57
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-13 17:28:33
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

    def __str__(self):
        return self.rid

    def __init__(self, mname, mpassword, mphonenum, m2org, mlevel=1):
        self.mlevel = mlevel
        self.mname = mname
        self.mpassword = mpassword
        self.mphonenum = mphonenum
        self.m2org = m2org

    def todict(self):
        managerdict = {}
        managerdict['mid'] = self.mid
        managerdict['mlevel'] = self.mlevel
        managerdict['mname'] = self.mname
        managerdict['mphonenum'] = self.mphonenum
        managerdict['m2org'] = self.m2org

        return managerdict
