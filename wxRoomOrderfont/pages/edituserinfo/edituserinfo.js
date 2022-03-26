/**
 * @Author: YJR-1100
 * @Date: 2022-03-26 20:12:07
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-26 23:32:25
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\edituserinfo\edituserinfo.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/edituserinfo/edituserinfo.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    editedisabled:false,
    userinfo:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var user = wx.getStorageSync('userinfo')
    console.log(user)
    if(options.isbasaceinfo==1){
      this.setData({
        editedisabled:true,
        [`userinfo.schoolid`]:user.schoolid,
        [`userinfo.uname`]:user.uname,
        [`userinfo.profassionclass`]:user.profassionclass,
        [`userinfo.uphonenum`]:user.uphonenum
      })
    }
  },
  checkphone(e){
    // 正则检查手机号是否合法
    // var reg = getRegExp("^(\+?0?86\-?)?1[3456789]\d{9}$")
    if(!/^(\+?0?86\-?)?1[3456789]\d{9}$/.test(e.detail.value)){
      wx.showToast({
        title: '手机号格式错误',
        icon: 'error',//
        mask:true,
        duration: 1000
      })
    }else{
      this.setData({
        [`userinfo.${e.currentTarget.id}`]:`${e.detail.value}`
      })
    }
  },
  setuserinfo(e){
    this.setData({
      [`userinfo.${e.currentTarget.id}`]:`${e.detail.value}`
    })
  },
  commitinfo(){
    const eventChannel = this.getOpenerEventChannel()
    var that = this
    wx.showModal({
      title: '提示',
      content: '一年只可修改一次个人信息，请确认无误后提交',
      success (res) {
        that.setData({
          editedisabled:true
        })
        if (res.confirm) {
          eventChannel.emit('acceptDataFromOpenedPage', {isbasaceinfo: '1',userinfo:that.data.userinfo});
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

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