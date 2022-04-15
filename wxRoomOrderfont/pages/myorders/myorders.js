/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 17:21:08
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-15 21:40:18
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\myorders\myorders.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/myorders/myorders.js
const app = getApp()
import {request} from "../../request/index.js"  
import {formatTime,formatDate} from "../../utils/util.js"
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
    }
  ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var that = this
    this.setData({
      options
    })
    getmyorders(this,options)
  },
  showdetailoforder(e){
    console.log(e)
    wx.navigateTo({
      url: `../orderdetails/orderdetails`,
      success: function(res) {
        // 通过eventChannel向被打开页面传送数据
        res.eventChannel.emit('orderdata', { data:e.currentTarget.dataset.item })
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
    getmyorders(this,this.data.options)
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


function getmyorders(that,options){
  request({url:"/orderitems/getmyorders",method:"POST",data:options})
    .then(result=>{
      console.log(result)
      if(result.data.code==1){
        // console.log(result.data.responsedata)
        that.setData({
          orderlist:result.data.responsedata.sort(
            (a,b)=>{
              var ay = a.ordertime.split(' ')[0]
              var by = b.ordertime.split(' ')[0]
              var at = a.ordertime.split(' ')[1]
              var bt = b.ordertime.split(' ')[1]
              if(ay<by) return 1
              else if (ay>by) return -1
              else{
                if(at.length<bt.length) return 1
                else return at>bt?-1:1
              }
            }
          )
        })
      }else{
        wx.showToast({
          title: '预约拉取失败',
          icon: 'error',//
          mask:true,
          duration: 800
        })
      }
    },err=>{
      wx.showToast({
        title: '网络错误',
        icon: 'error',//
        mask:true,
        duration: 800
      })
    })
}