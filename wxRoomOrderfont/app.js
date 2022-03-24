/**
 * @Author: YJR-1100
 * @Date: 2022-03-21 22:06:52
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-24 16:29:05
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\app.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    // 登录
    // wx.login({
    //   success (res) {
    //     if (res.code) {
    //       //发起网络请求
    //       console.log(res.code);
    //       wx.request({
    //         url: 'http://127.0.0.1:5000/api/v1/getopenid',
    //         data: {
    //           code: res.code
    //         },
    //         dataType:"json",
    //         success(res){
    //           var openid = res.data.openid
    //           wx.setStorageSync('openid',openid)
    //         }
    //       })
    //     } else {
    //       console.log('登录失败！' + res.errMsg)
    //     }
    //   }
    // })
  },
  globalData: {
    userInfo: null,
    rulereadtime:3
  }
})
