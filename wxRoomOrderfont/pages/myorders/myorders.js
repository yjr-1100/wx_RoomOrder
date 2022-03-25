

/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 17:21:08
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-25 19:43:08
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\myorders\myorders.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/myorders/myorders.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    /*
    # -1 未审核
    # 0  不通过
    # 1  通过
    */
    orderlist:[{
      status:-1,
      roomname:"会议室",
      usingtime:"2022-12-13 8:00-9:00",
      ordertime:"2022-12-12 04:23",
      address:"科教北501-2"
    },
    {
      status:0,
      roomname:"会议室",
      usingtime:"2022-12-13 18:00-19:00",
      ordertime:"2022-12-12 04:23",
      address:"科教北501-2"
    },
    {
      status:1,
      roomname:"会议室",
      usingtime:"2022-12-13 18:00-19:00",
      ordertime:"2022-12-12 04:23",
      address:"科教北501-2"
    }
  ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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