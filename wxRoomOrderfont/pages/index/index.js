

/**
 * @Author: YJR-1100
 * @Date: 2022-03-21 22:06:52
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-27 20:29:40
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\index\index.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// index.jss

// 获取应用实例
const app = getApp()
import {request} from "../../request/index.js"  
Page({

  /**
   * 页面的初始数据
   */
  data: {
    swiperimage:[],
    noimage:"https://cdn.jsdelivr.net/gh/yjr-1100/Photobag/roomorderimage/202203261650698.jpg",
    classroomlist:[
      {
        "name":"网络错误",
        "adress":"暂无教室信息",
        "imageurl":"https://cdn.jsdelivr.net/gh/yjr-1100/Photobag/roomorderimage/202203261650698.jpg",
        "describe":"请稍后重试"
      }
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    request({url:"/swiper/getswiperimage",method: "get"})
    .then(result=>{
      if(result.data.code==1){
        this.setData({
          swiperimage:result.data.responsedata
        })
      }
      else{
        
        wx.showToast({
          title: '数据库错误',
          icon: 'error',//
          mask:true,
          duration: 800
        })
      }
      
    })
    request({url:"/room/getrooms",method: "get"})
    .then(result=>{
      if(result.data.code == 1){
        this.setData({
          classroomlist:result.data.responsedata
        })
      }
      else{
        wx.showToast({
          icon:"error",
          mask:true,
          title:result.data.msg,
          duration:800
        })
      }
    })
  },
  gotoroomorder:function(e){
    //当前点击的索引
    var index = e.currentTarget.dataset.index;
    console.log(index)
    var that = this
    wx.navigateTo({
      url: `../roomdetail/roomdetail?rid=${that.data.classroomlist[index].rid}`,
      success: function(res) {
        // 通过eventChannel向被打开页面传送数据
        res.eventChannel.emit('classdata', { data:that.data.classroomlist[index] })
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    console.log("indexonReady")
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log("indexonShow")
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    console.log("indexonHide")
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    console.log("onUnload")
    
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