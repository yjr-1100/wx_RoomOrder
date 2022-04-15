/**
 * @Author: YJR-1100
 * @Date: 2022-04-15 13:27:56
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-15 16:31:53
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\innerverify\innerverify.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/innerverify/innerverify.js
const app = getApp()
import {request} from "../../request/index.js"  
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orglist:[],
    selectorgname:"请选择",
    orgid:null

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const that = this
    request({url:"/org/getallorg",method: "get"})
    .then(result=>{
      if(result.data.code==1){
        this.setData({
          orglist:result.data.responsedata
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
    }).then(result=>{
      request({url:"/user/getuserinfo",method: "POST",data:{'uid':options.uid}})
      .then(result=>{
        if(result.data.code==1){
          this.setData({
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
      }).then(result=>{
        if(that.data.userInfo.isinsider != 0){
          that.data.orglist.forEach(e=>{
            if(e.orgid===that.data.userInfo.orgid){
              that.setData({
                selectorgname:e.orgname
              })
            }
          })
          
        }
      })
    })
  },
  bindPickerChange(e){
    let index = e.detail.value
    let orgname = this.data.orglist[index].orgname
    let orgid = this.data.orglist[index].orgid
    this.setData({
      selectorgname:orgname,
      orgid:orgid
    })
  },
  clickbtn(e){
    console.log(e)
    if(!this.data.orgid){
      wx.showToast({
        title: '请选择组织',
        icon: 'error',//
        mask:true,
        duration: 1000
      })
    }else{
      let postdata = {
        uid:this.data.userInfo.uid,
        orgid:this.data.orgid
      }
      request({url:"/user/submitinnerverify",method: "POST",data:postdata})
      .then(result=>{
        if(result.data.code == 1){
          wx.setStorageSync("userinfo",result.data.responsedata)
          this.setData({
            userInfo:result.data.responsedata
          })
        }else{
          wx.showToast({
            title: '申请失败',
            icon: 'error',//
            mask:true,
            duration: 1000
          })
        }
      })
    }
    
  },
  mygetuserinfo(uid){
    request({url:"/user/getuserinfo",method: "POST",data:{'uid':uid}})
    .then(result=>{
      if(result.data.code==1){
        this.setData({
          userInfo:result.data.responsedata
        })
        wx.setStorageSync("userinfo",result.data.responsedata)
        if(result.data.responsedata.isinsider == 0){
          this.setData({
            selectorgname:"请选择",
          })
        }
      }else{
        wx.showToast({
          title: '数据获取失败',
          icon: 'error',//
          mask:true,
          duration: 800
        })
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
    this.mygetuserinfo(this.data.userInfo.uid)
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