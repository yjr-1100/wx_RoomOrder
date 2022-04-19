#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:15:12
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-19 15:46:52
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\rules\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from flask import Blueprint, request
from common.result import falseReturn, trueReturn
from common.tooken import certify_token
from apps.rules.models import Rule
from apps.managers.models import Managers
from apps.users.models import Users
from exts import db
rule_bp = Blueprint('rule', __name__)

# 得到规则


@rule_bp.route('/getrule', methods=['GET'])
def getrule():
    try:
        rule = Rule.query.filter(Rule.isdelet == 1).first()
    except:
        return falseReturn(msg="database failed")
    if not rule:
        return trueReturn(msg="没有须知")
    else:
        return trueReturn(data=rule.rutext, msg="success")

# 上传规则，数据库中只能存在一条有效规则


@rule_bp.route('/uploadrule', methods=['POST'])
def uploadrule():
    data = request.get_json()
    try:
        tooken = data['tooken']
        mid = data['mid']
    except:
        return falseReturn(msg="登录过期，请重新登录1")
    mpwd = Managers.query.get(mid).mpassword
    mphonenum = Managers.query.get(mid).mphonenum
    if not certify_token(str(mphonenum)+str(mpwd), tooken):
        return falseReturn(msg="登录过期，请重新登录2")

    try:
        text = data['text']
    except:
        return falseReturn(msg="缺少必要参数")
    text = text.strip()
    if text:
        text = text.replace('\n', '')
    if not text:
        return falseReturn(msg="您必须写些什么")
    rule = rule = Rule.query.filter(Rule.isdelet == 1).first()
    if rule:
        rule.isdelet = 0
    rule = Rule()
    rule.rutext = text
    userlist = Users.query.filter(Users.isreadedrules == 1).all()
    for user in userlist:
        user.isreadedrules = 0

    try:
        db.session.add(rule)
        db.session.commit()
    except:
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="更新成功")
