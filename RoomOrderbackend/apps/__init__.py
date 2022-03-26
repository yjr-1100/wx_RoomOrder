#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 14:27:40
# @LastEditors: YJR-1100
# @LastEditTime: 2022-03-26 15:51:20
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\__init__.py
# @Description: 
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
#--------------#--------------#

from flask import Flask
import settings
from exts import db
from apps.users.api import user_bp
from apps.orderitem.api import orderitems_bp
from apps.rooms.api import rooms_bp
from apps.swiper.api import swiper_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.DevelopmentConfig)

    db.init_app(app=app)
    app.register_blueprint(user_bp,url_prefix="/api/v1/user")
    app.register_blueprint(orderitems_bp,url_prefix="/api/v1/orderitems")
    app.register_blueprint(rooms_bp,url_prefix="/api/v1/room")
    app.register_blueprint(swiper_bp,url_prefix="/api/v1/swiper")
    print(app.url_map)
    return app