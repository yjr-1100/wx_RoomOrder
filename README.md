<!--
 * @Author: YJR-1100
 * @Date: 2022-03-21 20:06:11
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-15 17:44:24
 * @FilePath: \wx_RoomOrder\README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
-->

# 校园教室预约小程序

![](https://img.shields.io/badge/flask-v1.1.2-blue) ![](https://img.shields.io/badge/Python-v3.9.6-blue) ![](https://img.shields.io/badge/Vue-2.0-brightgreen) ![](https://img.shields.io/badge/%40vue%2Fcil-v5.0.4-brightgreen) ![](https://img.shields.io/badge/-Element-blue) 

![](https://img.shields.io/github/last-commit/yjr-1100/wx_RoomOrder)

## 需求与设计

### 后端设计

由于微信审核过程较慢，所以将一些可能经常更改的资源文件放在服务器上，通过请求来获取
1. :heavy_check_mark: 返回openid的接口

2. :heavy_check_mark: 创建用户的接口

3. :clock130: 更新用户信息的接口

    1. :clock130: 更新阅读状态

        1. :clock10: 重置所有人的阅读状态为没有阅读

        2. :heavy_check_mark: 用户阅读后修改状态为已阅读

    2. :heavy_check_mark: 更新个人信息

    3. :heavy_check_mark: 更新身份认证

4. :clock10: 创建教室的接口

5. :clock10: 更新教室的接口

5. :heavy_check_mark: 获取所有教室信息

6. :heavy_check_mark: 教室可用时间查询接口

6. :heavy_check_mark: 预约记录查询接口

7. :heavy_check_mark: 预约审核接口

8. :heavy_check_mark: 获取轮播图的接口

加油 :poultry_leg: :poultry_leg: :poultry_leg:

### 小程序设计

#### 需求

1. :heavy_check_mark: 微信授权登录

2. :heavy_check_mark: 编辑用户信息

3. :heavy_check_mark: 阅读借阅须知

2. :heavy_check_mark: 身份认证，提供不同认证方式，根据需要进行选择

    1.  :worried: 认证是本校学生/教师，并得到相关身份信息（学校不同需要调整user数据库字段）这个需要等官方配合，暂时无法完成
   
    2.  :heavy_check_mark: 选择对应组织，由组织管理员来确认通过

    3.  :stuck_out_tongue_winking_eye: 如果是其他用途，则使用完善用户信息的接口，用户填写并提交后才可以进行教室预约 （可以使用和上面`2` 相同的接口，修改提交数据即可）

3. :heavy_check_mark: 教室预约，选择时间段，填写必要信息，提交后等待审核

4. :heavy_check_mark: 已预约信息查看，可以看到审核状态

5. :dizzy_face: 轮播图动态更新后可以进行对应信息的展示,此项需求需要根据轮播图情况来定


### web端设计

通过vue2搭建web端，部分UI使用 `Element` 组件库

[Element传送门](https://element.eleme.cn/#/zh-CN)

#### 需求

1. :heavy_check_mark: 审核人员和超级管理员登录

1. :clock10: 可以更新教室信息

2. :heavy_check_mark: 进行教室使用的审核

3. :clock10: 进行教室状态的查询

4. :clock10: 更新小程序中的预约须知

5. :clock10: 更新小程序首页轮播图

6. :clock10: 用户权限控制 高级管理员(2)，教室管理员(1)，普通用户(0)无法登录，高级管理员可有创建教室管理员



## 效果展示

### 小程序效果
![](https://cdn.jsdelivr.net/gh/yjr-1100/Photobag/img/202204151744957.gif)

### 管理后台效果