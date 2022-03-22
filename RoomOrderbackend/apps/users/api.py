#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:10:50
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\users\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Blueprint,request,redirect,render_template,url_for
from apps.users.models import Users
import hashlib
from exts import db
from sqlalchemy import or_
user_bp = Blueprint('users',__name__)


@user_bp.route('/getopenid',methods=['GET','POST'])
def getOpenId():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            user=Users()
            user.username=username
            user.password=hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone=phone
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.user_center'))
    return "ssssss"