<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:35:23
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-13 20:26:29
 * @FilePath: \webformanager\src\views\roommanage.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-roommanagecontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="roomlists">
      <div class="roomitem" v-for="(item, index) in roomlist" :key="item.rid" @click="showdetails(item.rid, index)">
        <img :src="item.imageurl[0]" alt="" class="roomimg" :id="'roomimg' + item.rid" />
        <label :for="'roomimg' + item.rid">{{ item.name }}</label>
      </div>
    </div>
    <!-- 添加教室的按钮 -->
    <div class="addbtn">
      <p class="iconfont icon-shizijiahao3"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-roommanage',
  data() {
    return {
      roomlist: []
    }
  },
  created() {
    // 发送请求得到该管理者管理的所有教室
    this.getallroom(2)
  },
  methods: {
    async getallroom(orgid) {
      const { data } = await this.$http.get('/room/getrooms', {
        params: { orgid: orgid }
      })
      this.roomlist = data.responsedata
    },
    showdetails(rid, index) {
      console.log(rid)
      console.log(index)
    }
  }
}
</script>

<style lang="less" scoped>
.yjr-roommanagecontant {
  height: 100%;
  width: 100%;
  position: relative;
  .backmask {
    position: absolute;
    z-index: -98;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
  }
  .backimg {
    position: absolute;
    z-index: -99;
    height: 100%;
    width: 100%;
    background-image: url('@/assets/loginbackimg2.jpg');
    background-size: 100% 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(2px);
  }
  .roomlists {
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .roomitem {
      display: flex;
      flex-direction: column;
      height: 220px;
      width: 350px;
      background-color: rgba(255, 255, 255, 0.7);
      margin: 10px;
      .roomimg {
        flex: 5;
        display: block;
        height: 190px;
        width: 100%;
      }
      label {
        flex: 2;
        display: block;
        font-size: 1vw;
        text-align: center;
        font-weight: 400;
      }
      &:hover {
        color: #4a567a;
        cursor: pointer;
        label {
          cursor: pointer;
        }
      }
    }
  }
  .addbtn {
    position: fixed;
    bottom: 40px;
    right: 40px;
    background-color: #54648f;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-content: center;
    text-align: center;
    box-shadow: 0 0 15px #616e81;
    p {
      display: block;
      width: 60px;
      height: 60px;
      line-height: 60px;
      border-radius: 50%;
      margin: 0;
      color: #cccdce;
      font-size: 35px;
    }
    &:hover {
      cursor: pointer;
      background-color: #4e67ad;
      p {
        cursor: pointer;
        color: #fff;
      }
    }
  }
}
</style>
