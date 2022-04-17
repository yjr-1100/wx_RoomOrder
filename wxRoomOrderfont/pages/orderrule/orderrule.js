/**
 * @Author: YJR-1100
 * @Date: 2022-03-24 13:39:31
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 23:35:47
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\orderrule\orderrule.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/orderrule/orderrule.js
import {request} from "../../request/index.js"  
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    counttime:0,
    btndisabled:true,
    chboxchecked:false,
    rediodisabled:false,
    isreaded:false,
    rulesitemlist:['预约须知获取失败']
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(option){
    request({url:"/rule/getrule",method: "get"})
    .then(result=>{
      this.setData({
        rulesitemlist : result.data.responsedata.split(';')
      })
    })
    this.setData({
      "counttime":app.globalData.rulereadtime
    })
    console.log(option)
    if(option.isreadedrules == 1){
      this.setData({
        isreaded:true,
        chboxchecked:true,
        rediodisabled:true,
        counttime:""
      })
    }
    else{
      countDown(this,this.data.counttime)
    }
    
    // // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
    // eventChannel.on('acceptDataFromOpenerPage', function(data) {
    //   console.log(data)
    // })
  },
  radioChange:function(e){
    // console.log(e)
    var checked = this.data.chboxchecked;
    this.setData({
      "chboxchecked":!checked
    })
  },
  viewscroll:function (param) { 
    this.setData({
      "isreaded":true
    })
  },
  btnverify:function(e){
    if(this.data.isreaded&&this.data.chboxchecked){
      const eventChannel = this.getOpenerEventChannel()
      
      this.setData({
        rediodisabled:true
      })
      wx.navigateBack({
        delta: 1
      })
      // 发回去
      eventChannel.emit('acceptDataFromOpenedPage', {isreadedrules: '1'});
    }
    else if(!this.data.isreaded){
      // 提示需要把须知滑动到最底下
      wx.showToast({
        title: '您需要将须知阅读至最后一条',
        icon: 'none',
        mask:true,
        duration: 2000//持续的时间
      })
    }else if(!this.data.chboxchecked){
      //提示需要勾选已阅读
      wx.showToast({
        title: '您需要勾选上方的承诺',
        icon: 'none',
        mask:true,
        duration: 2000//持续的时间
      })
    }
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    // countDown(this,this.data.counttime)
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
function countDown(that, count) {
  if (count <= 0) {
    that.setData({
      counttime: count,
      btndisabled:false
    })
    return;
  }
  that.setData({
    counttime: count
  })
  setTimeout(function () {
    count--;
    countDown(that, count);
  }, 1000);
}