#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:23:51
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-27 14:50:32
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rooms\api.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Blueprint,request,redirect,render_template,url_for
from common.result import trueReturn,falseReturn
from apps.rooms.models import Rooms
import hashlib
from exts import db
from sqlalchemy import or_
rooms_bp = Blueprint('rooms',__name__)

# 获取所有教室
@rooms_bp.route('/getrooms',methods=['Get'])
def getrooms():
    try:
        rooms = Rooms.query.filter(Rooms.isdelet == 1).all()
    except:
        return falseReturn(msg="拉取教室信息错误",code = -1)
    
    roomlist = []
    for room in rooms:
        print(room.rphotoURL.split(';'))
        rinfo = {}
        rinfo['rid'] = room.rid
        rinfo['name'] = room.rname
        rinfo['adress'] = room.raddress
        rinfo['describe'] = room.rdescribe
        rinfo['imageurl'] = room.rphotoURL.split(';')
        rinfo['rcanbeusetimes'] = room.rcanbeusetimes.split(';')
        roomlist.append(rinfo)
    return trueReturn(data=roomlist)

