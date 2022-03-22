'''
Author: YJR-1100
Date: 2022-03-22 14:26:44
LastEditors: YJR-1100
LastEditTime: 2022-03-22 14:40:21
FilePath: \wx_RoomOrder\RoomOrderbackend\app.py
Description: 

Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
'''

from flask_script import Manager
from apps import create_app
from flask_migrate import Migrate,MigrateCommand
from exts import db


app = create_app()

manager = Manager(app=app)

migrate = Migrate(app = app,db = db)

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()