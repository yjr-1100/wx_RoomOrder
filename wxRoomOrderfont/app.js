/**
 * @Author: YJR-1100
 * @Date: 2022-03-21 22:06:52
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-27 20:30:08
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\app.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
import {request} from "./request/index.js"
App({
  onLaunch() {
    var that = this
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    // 登录
    wx.login({
      success (res) {
        if (res.code) {
          //发起网络请求
          console.log(res.code);
          var data={ code: res.code  }
          var myheader={  'content-type': 'application/json'}
          request({url:"/user/getopenid",data:data,method:"GET",header:myheader})
          .then(result=>{
            console.log(result)
            var openid = result.data.openid
            wx.setStorageSync('openid',openid)
            that.globalData.canIlogin=1;
          },err=>{
            wx.showToast({
              title: '网络错误',
              icon: 'error',//
              mask:true,
              duration: 800
            })
          })
        } else {
          wx.showToast({
            title: '数据错误请重开',
            icon: 'error',//
            mask:true,
            duration: 1500
          })
        }
      }
    })
  },
  globalData: {
    userInfo: null,
    rulereadtime:3,
    canIlogin:0
  }
})
