

/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 00:00:14
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-15 17:34:08
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\roomdetail\roomdetail.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/roomdetail/roomdetail.js
const app = getApp()

import {request} from "../../request/index.js"  
import {formatTime,formatDate} from "../../utils/util.js"
Page({

  /**
   * 页面的初始数据
   */
  data: {
    maxlength:256,
    currentlength:0,
    bodyheight:0,
    roomusage:"",
    autograph:"",//负责人签字的图片 如果不是内部人员需要这个
    chosedtime:"",
    room:{
      "detailimage":["../../Images/咨询室.jpg","../../Images/会议室.jpg"],
      "name":"咨询室",
      "adress":"科教北501-1",
      "describe":"教学咨询与诊断，教学团队或课程组研讨交流等"
    },
    canbeuserdtime:[
    {
      "bgintime":"8:00",
      "endtime":"9:00",
      "status":0
    }
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var that = this
    const eventChannel = this.getOpenerEventChannel()
    // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
    eventChannel.on('classdata', function(data) {
      console.log(data)
      that.setData({
        [`room.detailimage`]:data.data.imageurl.filter((x) => x !== ''),
        [`room.name`]:data.data.name,
        [`room.adress`]:data.data.adress,
        [`room.describe`]:data.data.describe,
        [`room.rid`]:data.data.rid,
        [`room.orgid`]:data.data.orgid,
        rcanbeusetimes:data.data.rcanbeusetimes
      })
      // console.log(...data.data.imageurl)

      // 得到该教室今天已经预约的时间段
      getroomusedtime(that,data.data.rid,formatDate(new Date()))
      
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

    //点击轮播图放大预览
  handlePrevewImage(e){
    // 构造要预览的图片数组
    const urls = this.data.room.detailimage;
    console.log(urls)
    const {index} = e.currentTarget.dataset
    console.log(index);
    wx.previewImage({
      current: urls[index],
      urls: urls
    });
  },
  // 输入字符统计
  useredfoinput(e){
    console.log(e)
    this.setData({
      currentlength:parseInt(e.detail.value.length),
      roomusage:`${e.detail.value}`
    })
  },
  chosetime(e){
    var currentindex = e.currentTarget.dataset.index;
    // console.log(currentindex)
    for(var i = 0;i<this.data.canbeuserdtime.length;i++){
      if(this.data.canbeuserdtime[i].status==2){
        this.setData({
          [`canbeuserdtime[${i}].status`]:0
        })

      }
      if(this.data.canbeuserdtime[currentindex].status==1){
        //提示不可选
        wx.showToast({
          title: '该教室已被借用',
          icon: 'error',//
          mask:true,
          duration: 1000
        })
      }else{
        // 变成选中状态
        this.setData({
          [`canbeuserdtime[${currentindex}].status`]:2,
          chosedtime:this.data.canbeuserdtime[currentindex].bgintime+'-'+this.data.canbeuserdtime[currentindex].endtime
        })
      }
    }
  },
  // 点击立即预约的处理事件
  clickbtn(e){
    var that = this
    console.log(e)
    var user = wx.getStorageSync('userinfo')
    if(!user){
      wx.showModal({
        title: '提示',
        content: '您需要登录并完善个人信息',
        mask:true,
        success (res) {
          if (res.confirm) {
            //点击确定后跳到tabbar登录页面
            wx.switchTab({
              url: '/pages/user/user'
            })
          }
        }
      })
    }else if(!user.schoolid&&
      !user.uname&&
      !user.uphonenum&&
      !user.profassionclass){
        wx.showModal({
          title: '提示',
          content: '请完善个人信息',
          mask:true,
          success (res) {
            if (res.confirm) {
              //点击确定后跳到tabbar登录页面
              wx.switchTab({
                url: '/pages/user/user'
              })
            }
          }
        })
    }else if(user.isreadedrules == 0){
      wx.showModal({
        title: '提示',
        content: '请阅读借阅须知',
        mask:true,
        success (res) {
          if (res.confirm) {
            //点击确定后跳到tabbar登录页面
            wx.switchTab({
              url: '/pages/user/user'
            })
          }
        }
      })
    }
    else if(!this.data.roomusage){//检查教室用途没有有内容
      wx.showToast({
        title: '请填写教室用途',
        icon: 'error',//
        mask:true,
        duration: 800
      })
    }else if(!this.data.chosedtime){
      wx.showToast({
        title: '请选择使用时间',
        icon: 'error',//
        mask:true,
        duration: 800
      })
    }
    else{
      // 得到数据
      var data = {
        roomusage:this.data.roomusage,
        room_id:this.data.room.rid,
        room2orgid:this.data.room.orgid,
        usingtime:this.data.chosedtime,
        user_id:user.uid
      }
      console.log(data)
      // 发送请求
      request({url:"/orderitems/makeorder",method:"POST",data:data})
      .then(result=>{
        console.log(result)
        if(result.data.code==1){
          wx.showModal({
            title: '提示',
            content: '申请成功，请在我的预约中查看审核结果',
            mask:true,
            success (res) {
              if (res.confirm) {
                //跳到我的预约
                console.log(wx.getStorageSync('userInfo'))
                wx.redirectTo({
                  url: `../myorders/myorders?uid=${user.uid}`
                })
              }
            },fail(){
              wx.navigateBack({
                delta:1
              })
            }
          })
        }else{
          wx.showToast({
            title: '网络错误',
            icon: 'error',//
            mask:true,
            duration: 800
          })
        }
      })
    }
    
    
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    const that = this
    const obj=wx.createSelectorQuery();
    obj.select(".classinfo").boundingClientRect()
    obj.exec(function(res){
      that.setData({
        "bodyheight":res[0].height*100/wx.getSystemInfoSync().screenWidth-18+"vw"
      })
      // console.log(wx.getSystemInfoSync().screenWidth)
    })
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
    getroomusedtime(this,this.data.room.rid,formatDate(new Date()))

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
//formatDate(new Date())
function getroomusedtime(that,rid,date){
  request({url:"/orderitems/roomusertoday",method:"GET",data:{rid:rid,date:date}})
  .then(result=>{
    var usedtimelist = []
    var canbeuserdtime = []
    console.log(result)
    if(result.data.code==1){
      usedtimelist = result.data.responsedata.sort(
        (a,b)=>{
          if(a.length<b.length) return -1
          else return a<b?-1:1
        }
      )
      that.setData({
        usedtimelist:usedtimelist
      })
    } 
    else{
      wx.showModal({
        title: '提示',
        content: '可用时间获取失败请刷新重试',
        success (res) {
          if (res.confirm) {
            getroomusedtime(that,rid,date)
          } else if (res.cancel) {
            wx.navigateBack({
              delta: 1
            })
          }
        }
      })
    }
    let j=0
    for(let i = 0;i<that.data.rcanbeusetimes.length;i++){
      if(that.data.rcanbeusetimes[i]){
        if(j<usedtimelist.length&&that.data.rcanbeusetimes[i]==usedtimelist[j]){
          canbeuserdtime.push({
            "bgintime":that.data.rcanbeusetimes[i].split('-')[0],
            "endtime":that.data.rcanbeusetimes[i].split('-')[1],
            "status":1
          })
          j++
        }
        else{
          canbeuserdtime.push({
            "bgintime":that.data.rcanbeusetimes[i].split('-')[0],
            "endtime":that.data.rcanbeusetimes[i].split('-')[1],
            "status":0
          })
        }
      }
    }
    that.setData({
      canbeuserdtime
    })
  })
}