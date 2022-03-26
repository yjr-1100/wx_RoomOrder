

/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 00:00:14
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-03-27 00:04:24
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\pages\roomdetail\roomdetail.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
// pages/roomdetail/roomdetail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    maxlength:256,
    currentlength:0,
    bodyheight:0,
    room:{
      "detailimage":["../../Images/咨询室.jpg","../../Images/会议室.jpg"],
      "name":"咨询室",
      "adress":"科教北501-1",
      "describe":"教学咨询与诊断，教学团队或课程组研讨交流等"
    },
    canbeuserdtime:[
    {
      "usetime":"8:00-9:00",
      "status":0
    },{
      "usetime":"9:00-10:00",
      "status":1
    },{
      "usetime":"10:00-11:00",
      "status":1
    },{
      "usetime":"11:00-12:00",
      "status":0
    },{
      "usetime":"14:00-15:00",
      "status":0
    },{
      "usetime":"15:00-16:00",
      "status":1
    },{
      "usetime":"16:00-17:00",
      "status":0
    },{
      "usetime":"17:00-18:00",
      "status":1
    },{
      "usetime":"19:00-20:00",
      "status":0
    },{
      "usetime":"20:00-21:00",
      "status":0
    }
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    const eventChannel = this.getOpenerEventChannel()
    // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
    eventChannel.on('acceptDataFromOpenerPage', function(data) {
      console.log(data)
      
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
      currentlength:parseInt(e.detail.value.length)
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
          title: '改教室已被借用',
          icon: 'error',//
          mask:true,
          duration: 1000
        })
      }else{
        // 变成选中状态
        this.setData({
          [`canbeuserdtime[${currentindex}].status`]:2
        })
      }
    }
  },
  // 点击立即预约的处理事件
  clickbtn(e){
    console.log(e)
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