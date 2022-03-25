<!--
 * @Author: YJR-1100
 * @Date: 2022-03-21 20:06:11
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-25 23:59:26
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

3. :clock10: 更新用户信息的接口

4. :clock10: 创建教室的接口

5. :clock10: 更新教室的接口

6. :clock10: 预约记录查询接口

7. :clock10: 预约审核接口

加油 :poultry_leg:

## 小程序设计

### 需求

1. 微信授权登录

2. 身份认证，

    1. 认证是本校学生/教师，并得到相关身份信息（学校不同需要调整user数据库字段）

    2. 如果是其他用途，则使用完善用户信息的接口，用户填写并提交后才可以进行教室预约

3. 教室预约，选择时间段，填写必要信息，提交后等待审核

4. 已预约信息查看，可以看到审核状态


## web端设计

### 需求

1. 可以更新教室信息

2. 进行教室使用的审核

3. 进行教室状态的查询

4. 更新小程序中的预约须知

5. 更新小程序首页轮播图