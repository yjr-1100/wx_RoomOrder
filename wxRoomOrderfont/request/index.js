/**
 * @Author: YJR-1100
 * @Date: 2022-03-25 21:45:02
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-19 23:46:07
 * @FilePath: \wx_RoomOrder\wxRoomOrderfont\request\index.js
 * @Description: 
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved. 
 */
//同时发送异步请求的次数
let ajaxTimes = 0;
export const request=(params)=>{
    ajaxTimes++;
    //显示加载中的效果
    wx.showLoading({
        title: '加载中',
        mask:true
    })
    const baseUrl = "http://127.0.0.1:5000/api/v1"
    return new Promise((resolve,reject)=>{
        wx.request({
            ...params,
            
            url:baseUrl+params.url,
            data:params.data,
            method: params.method,
            Headers:params.header,
            dataType:"json",
            success:(result)=>{
                resolve(result);
            },
            fail:(err)=>{
                reject(err);
            },
            complete:()=>{
                ajaxTimes--;
                if(ajaxTimes===0){
                    wx.hideLoading(); 
                }
            }
        });
    })
}