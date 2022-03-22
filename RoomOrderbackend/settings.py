'''
Author: YJR-1100
Date: 2022-03-22 14:26:49
LastEditors: YJR-1100
LastEditTime: 2022-03-22 14:39:51
FilePath: \wx_RoomOrder\RoomOrderbackend\settings.py
Description: 

Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
'''

# 为app创建的配置文件
class Config:
    ENV= 'development'
    DEBUG=True
    # 使用的数据库+驱动://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123zxc@127.0.0.1:3306/roomorder'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV= 'production'
    DEBUG=False 
