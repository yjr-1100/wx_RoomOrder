#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:23:55
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:12:24
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\orderitem\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Blueprint,request,redirect,render_template,url_for
from apps.orderitem.models import Orderitems
import hashlib
from exts import db
from sqlalchemy import or_
orderitems_bp = Blueprint('orderitems',__name__)
