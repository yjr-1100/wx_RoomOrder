<!--
 * @Author: YJR-1100
 * @Date: 2022-03-21 20:06:11
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-22 15:49:29
 * @FilePath: \wx_RoomOrder\README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
-->

# 校园教室预约小程序  ![](https://img.shields.io/badge/flask-v1.1.2-blue) ![](https://img.shields.io/badge/Python-v3.9.6-blue) 

## 后端设计

由于微信审核过程较慢，所以将一些可能经常更改的资源文件放在服务器上，通过请求来获取

## 小程序设计

### 需求

1. 微信授权登录

2. 身份认证，

    1. 认证是本校学生/教师，并得到相关身份信息（学校不同需要调整user数据库字段）

    2. 如果是其他用途，则使用完善用户信息的接口，用户填写并提交后才可以进行教室预约

3. 教室预约，选择时间段，填写必要信息，提交后等待审核

## web端设计

### 需求

1. 可以更新教室信息

2. 进行教室使用的审核