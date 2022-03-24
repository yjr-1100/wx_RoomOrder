

/**
 * @Author: YJR-1100
 * @Date: 2022-03-21 22:06:52
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-24 23:59:13
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\index\index.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// index.jss

// 获取应用实例
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    swiperimage:[
      "../../Images/swiper_p1.jpeg",
      "../../Images/swiper_p2.jpeg",
      "../../Images/swiper_p3.jpeg",
      "../../Images/swiper_p4.jpeg"
    ],
    classroomlist:[
      {
        "name":"咨询室",
        "adress":"科教北501-1",
        "imageurl":"../../Images/咨询室.jpg",
        "describe":"教学咨询与诊断，教学团队或课程组研讨交流等"
      },
      {
        "name":"会议室",
        "adress":"科教北501-2",
        "imageurl":"../../Images/会议室.jpg",
        "describe":"中小型会议容纳25左右"
      },
      {
        "name":"互动研讨室-1",
        "adress":"科教北502",
        "imageurl":"../../Images/互动研讨室1.jpg",
        "describe":"讲课比赛、交流研讨、工作坊、教研室活动（教学团队或课程组）、课题申报、集体备课等"
      },
      {
        "name":"互动研讨室-2",
        "adress":"科教北503",
        "imageurl":"../../Images/互动研讨室2.jpg",
        "describe":"讲课比赛、交流研讨、工作坊、教研室活动（教学团队或课程组）、课题申报、集体备课等"
      },
      {
        "name":"微格教室",
        "adress":"科教北508",
        "imageurl":"../../Images/微格教室.jpg",
        "describe":"配有多媒体电脑、交互式大屏及录播设备，供教师进行教学技能训练、讲课比赛训练、工作坊等"
      },
      {
        "name":"开放沙龙室",
        "adress":"科教北504",
        "imageurl":"../../Images/开放沙龙室.jpg",
        "describe":"备有教师教育相关书籍与期刊，供教师阅读与学习，交流教学与读书心得"
      }
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  gotoroomorder:function(e){
    //当前点击的索引
    var index = e.currentTarget.dataset.index;
    console.log(index)
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