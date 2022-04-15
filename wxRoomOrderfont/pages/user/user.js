

/**
 * @Author: YJR-1100
 * @Date: 2022-03-21 23:17:31
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-15 16:35:12
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\user\user.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */

// pages/user/user.js
const app = getApp()
import {request} from "../../request/index.js"  
Page({

  /**
   * 页面的初始数据
   */
  data: {
    canloginbtnuse:false,
    userInfo: {},
    hasUserInfo: false,
    canIUseGetUserProfile: false,
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log("111")
    if(!this.data.hasUserInfo){
      wx.removeStorageSync("userinfo")
    }
  },
  getUserProfile(e) {
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
    // 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    if(app.globalData.canIlogin==0){
      this.setData({
        canloginbtnuse:true
      })
      wx.showModal({
        title: '提示',
        content: '网络错误请清理后台后重试',
        mask:true,
        success (res) {
          if (res.confirm) {
            console.log('用户点击确定')
          } else if (res.cancel) {
            console.log('用户点击取消')
          }
        }
      })
    }else{
      wx.getUserProfile({
        desc: '用于完善用户资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
        success: (res) => {
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
          var data={
            openid:wx.getStorageSync('openid'),
            ...res.userInfo
          }
          request({url:"/user/updateuser",method: "post",data:data})
          .then(result=>{
            // console.log(result)
            if(result.data.code==1){
              this.setData({
                userInfo:result.data.responsedata
              })
              wx.setStorageSync("userinfo",result.data.responsedata)
            }
            else{
              wx.showToast({
                title: 'no openid',
                icon: 'error',//
                mask:true,
                duration: 800
              })
            }
            
          })
        }
      })
    }
    
  },

  showorderrules(){
    var that = this;
    wx.navigateTo({
      url: `../orderrule/orderrule?isreadedrules=${this.data.userInfo.isreadedrules}`,
      events: {
        // 为指定事件添加一个监听器，获取被打开页面传送到当前页面的数据
        acceptDataFromOpenedPage: function(data) {
          console.log(data)
          if(data.isreadedrules==1){
            request({url:"/user/modifyreaded",method:"post",data:{'openid':that.data.userInfo.uopenid}})
            .then(result=>{
              if(result.data.code==1){
                that.setData({
                  userInfo:result.data.responsedata
                })
                wx.setStorageSync("userinfo",result.data.responsedata)
              }else{
                wx.showToast({
                  title: '写入数据库失败',
                  icon: 'error',//
                  mask:true,
                  duration: 800
                })
              }
              
            })
          }
        }
      },
      success: function(res) {
        // 通过eventChannel向被打开页面传送数据
        res.eventChannel.emit('acceptDataFromOpenerPage', { data: 'user发过去的' })
      }
    })
  },
  //我的预约
  myorders(e){
    wx.navigateTo({
      url: `../myorders/myorders?uid=${this.data.userInfo.uid}`
    })
  },
  // 身份认证
  identityverify(e){
    wx.navigateTo({
      url: `../innerverify/innerverify?uid=${this.data.userInfo.uid}`
    })
  },
  // 我的信息编写
  editmyinfo(){
    var that = this;
    wx.navigateTo({
      url: `../edituserinfo/edituserinfo?isbasaceinfo=${this.data.userInfo.isbasaceinfo}&&openid=${this.data.userInfo.uopenid}`,
      events: {
        // 为指定事件添加一个监听器，获取被打开页面传送到当前页面的数据
        acceptDataFromOpenedPage: function(data) {
          console.log(data)
          if(data.isbasaceinfo==1){
            request({url:"/user/edituserinfo",method:"post",data:{'openid':that.data.userInfo.uopenid,...data.userinfo,'isbasaceinfo':data.isbasaceinfo}})
            .then(result=>{
              if(result.data.status){
                that.setData({
                  userInfo:result.data.responsedata
                })
                wx.setStorageSync("userinfo",result.data.responsedata)
              }else{
                wx.showToast({
                  title: '更新失败',
                  icon: 'error',//
                  mask:true,
                  duration: 800
                })
              }
            })
          }
          
        }
      },
      success: function(res) {
        // 通过eventChannel向被打开页面传送数据
        res.eventChannel.emit('acceptDataFromOpenerPage', { data: 'user发过去的' })
      }
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    console.log("111")
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    // 页面切换 之间切换会输出
    console.log("222")
    this.setData({
      userInfo:wx.getStorageSync("userinfo")
    })
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    // tablebaar 之间切换会输出
    console.log("333")
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    console.log("444")
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
      request({url:"/user/getuserinfo",method: "POST",data:{'uid':this.data.userInfo.uid}})
      .then(result=>{
        if(result.data.code==1){
          this.setData({
            userInfo:result.data.responsedata
          })
          wx.setStorageSync("userinfo",result.data.responsedata)
        }else{
          wx.showToast({
            title: '刷新失败',
            icon: 'error',//
            mask:true,
            duration: 800
          })
        }
      })
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})