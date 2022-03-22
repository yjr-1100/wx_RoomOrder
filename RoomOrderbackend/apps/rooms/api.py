#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:23:51
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-22 17:11:07
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rooms\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Blueprint,request,redirect,render_template,url_for
from apps.rooms.models import Rooms
import hashlib
from exts import db
from sqlalchemy import or_
rooms_bp = Blueprint('rooms',__name__)


