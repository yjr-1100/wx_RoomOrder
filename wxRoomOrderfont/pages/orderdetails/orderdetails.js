/**
 * @Author: YJR-1100
 * @Date: 2022-04-15 17:49:07
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-18 21:41:26
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\orderdetails\orderdetails.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/orderdetails/orderdetails.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order: {
      "oid": 30,
      "uphonenum": "13980808086",
      "schoolid": "1111111",
      "username": "yjr1100",
      "ordertime": "2022-04-15 17:37:00",
      "roomname": "会议室",
      "address": "科教北501-2",
      "roomusage": "测试借用教室",
      "usingtime": "2022-04-15 9:00-10:00",
      "status": 0,
      "ochecktime": "2022-04-15 17:37:00",
      "checkername": "杨嘉睿",
      "rejectreasion": "测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝测试拒绝",
      "userinner": 1
    },
    zhankai:true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var that = this
    const eventChannel = this.getOpenerEventChannel()
    // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
    eventChannel.on('orderdata', function(data) {
      console.log(data)
      that.setData({
        order:data.data
      })
      if(data.data.autograph){
        that.setData({
          [`order.autograph`]:data.data.autograph.split(';')
        })
      }
      
    })
  },
  clickzhankai(){
    this.setData({
      zhankai:!this.data.zhankai
    })
  },
  imgYu(event){
    console.log(event)
  var src = event.currentTarget.dataset.src;//获取data-src
  var imgList = event.currentTarget.dataset.list;//获取data-list
  //图片预览
  wx.previewImage({
  current: src, // 当前显示图片的http链接
  urls: imgList // 需要预览的图片http链接列表
  })},
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