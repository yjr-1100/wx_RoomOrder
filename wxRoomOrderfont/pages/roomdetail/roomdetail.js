

/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 00:00:14
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-24 20:52:50
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
    isinner:0,
    datearray:[],
    dateindex:0,
    //负责人签字的图片 如果不是内部人员需要这个
    imgs: [],
    count: 1,
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
  bindDateChange(e){
    console.log(e)
    this.setData({
      dateindex:e.detail.value
    })
    getroomusedtime(this,this.data.room.rid,this.data.datearray[e.detail.value])
  },
  //下载申请表
  See_download(){
    if(this.data.room.pdfurl){
      wx.showLoading({
        title: '加载中',
        mask:true
    })
      wx.downloadFile({
        url:this.data.room.pdfurl,
        success (res) {
          // 只要服务器有响应数据，就会把响应内容写入文件并进入 success 回调，业务需要自行判断是否下载到了想要的内容
          wx.hideLoading(); 
          if (res.statusCode === 200) {
            console.log(res)
            var filepath = res.tempFilePath
            wx.openDocument({
              filePath: filepath,
              fileType:'pdf',
              showMenu:true
            })
          }else{
            wx.showToast({
                title: "下载失败",
                icon: "error",
                duration: 2000
              })
          }
        }
      })
    }else{
      wx.showToast({
        title: "申请表不存在",
        icon: "none",
        duration: 2000
      })
    }
    
  },
  //上传图片
  bindUpload: function (e) {
      switch (this.data.imgs.length) {
        case 0:
          this.data.count = 3
          break
        case 1:
          this.data.count = 2
          break
        case 2:
          this.data.count = 1
          break
      }
      var that = this
      wx.chooseImage({
        count: that.data.count, // 默认3
        sizeType: ["original", "compressed"], // 可以指定是原图还是压缩图，默认二者都有
        sourceType: ["album", "camera"], // 可以指定来源是相册还是相机，默认二者都有
        success: function (res) {
          // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
          var tempFilePaths = res.tempFilePaths
          for (var i = 0; i < tempFilePaths.length; i++) {
            wx.uploadFile({
              url: 'http://127.0.0.1:5000/api/v1/user/uploadaccessimage',
              filePath: tempFilePaths[i],
              name: "file",
              header: {
                "content-type": "multipart/form-data"
              },
              success: function (res) {
                if (res.statusCode == 200) {
                  wx.showToast({
                    title: "上传成功",
                    icon: "none",
                    duration: 1500
                  })
                  console.log(res.data)
                  that.data.imgs.push(JSON.parse(res.data).responsedata['imgurl'])
                  that.setData({
                    imgs: that.data.imgs
                  })
                }
              },
              fail: function (err) {
                wx.showToast({
                  title: "上传失败",
                  icon: "none",
                  duration: 2000
                })
              },
              complete: function (result) {
                console.log(result.errMsg)
              }
            })
          }
        }
      })
    },
    // 删除图片
deleteImg: function (e) {
  var that = this
  wx.showModal({
    title: "提示",
    content: "是否删除",
    success: function (res) {
      if (res.confirm) {
        for (var i = 0; i < that.data.imgs.length; i++) {
          if (i == e.currentTarget.dataset.index) that.data.imgs.splice(i, 1)
        }
        that.setData({
          imgs: that.data.imgs
        })
      } else if (res.cancel) {
        console.log("用户点击取消")
      }
    }
  })
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var date = new Date()
    var datearray = []
    datearray.push(formatDate(date))
    date = new Date(date.getTime()+1000*60*60*24)
    datearray.push(formatDate(date))
    this.setData({
      datearray
    })
    console.log(options)
    var that = this
    const eventChannel = this.getOpenerEventChannel()
    var user = wx.getStorageSync('userinfo')
      if(user){
        this.setData({
          isinner:user.isinsider
        })
      }
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
        [`room.pdfname`]:data.data.pdfname,
        [`room.pdfurl`]:data.data.pdfurl,
        rcanbeusetimes:data.data.rcanbeusetimes.sort()
      })
      
      // console.log(...data.data.imageurl)
      
      // 得到该教室对应日期已经预约的时间段，开始默认今天
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
    }else if(this.data.isinner!=1&&this.data.imgs.length === 0){
      wx.showToast({
        title: '请上传签字图片',
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
        user_id:user.uid,
        verifyimg:this.data.imgs.join(';'),
        usingdate:this.data.datearray[this.data.dateindex]
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