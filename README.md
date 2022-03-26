<!--
 * @Author: YJR-1100
 * @Date: 2022-03-21 20:06:11
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-26 23:53:30
 * @FilePath: \wx_RoomOrder\README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
-->

# 校园教室预约小程序  ![](https://img.shields.io/badge/flask-v1.1.2-blue) ![](https://img.shields.io/badge/Python-v3.9.6-blue) 

## 后端设计

由于微信审核过程较慢，所以将一些可能经常更改的资源文件放在服务器上，通过请求来获取
1. :heavy_check_mark: 返回openid的接口

2. :heavy_check_mark: 创建用户的接口

3. :clock30: 更新用户信息的接口

    1. :clock30: 更新阅读状态

        1. :clock10: 重置所有人的阅读状态为没有阅读

        2. :heavy_check_mark: 用户阅读后修改状态为已阅读

    2. :heavy_check_mark: 更新个人信息

    3. :clock10: 更新身份认证

4. :clock10: 创建教室的接口

5. :clock10: 更新教室的接口

5. :clock10: 获取所有教室信息

6. :clock10: 预约记录查询接口

7. :clock10: 预约审核接口

8. :heavy_check_mark: 获取轮播图的接口

加油 :poultry_leg: :poultry_leg: :poultry_leg:

## 小程序设计

### 需求

1. :heavy_check_mark: 微信授权登录

2. :heavy_check_mark: 编辑用户信息

3. :heavy_check_mark: 阅读借阅须知

2. :clock10: 身份认证，

    1. :clock10: 认证是本校学生/教师，并得到相关身份信息（学校不同需要调整user数据库字段）

    2. :clock10: 如果是其他用途，则使用完善用户信息的接口，用户填写并提交后才可以进行教室预约

3. :clock10: 教室预约，选择时间段，填写必要信息，提交后等待审核

4. :clock10: 已预约信息查看，可以看到审核状态

5. :clock10: 轮播图动态更新后可以进行对应信息的展示


## web端设计

### 需求

1. :clock10: 可以更新教室信息

2. :clock10: 进行教室使用的审核

3. :clock10: 进行教室状态的查询

4. :clock10: 更新小程序中的预约须知

5. :clock10: 更新小程序首页轮播图

6. :clock10: 用户权限控制 高级管理员(2)，教室管理员(1)，普通用户(0)无法登录，高级管理员可有创建教室管理员