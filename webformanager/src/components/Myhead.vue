<!--
 * @Author: YJR-1100
 * @Date: 2022-04-12 22:59:28
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-16 22:47:27
 * @FilePath: \webformanager\src\components\Myhead.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-headcontant">
    <div class="backimg"></div>
    <img src="@/assets/headlogo.png" alt="" class="leftlogo" />
    <img src="@/assets/title2.png" alt="" class="title" />
    <!-- <span>教室预约管理系统</span> -->
    <button @click="logoutbtn">{{ name }} 退出登录</button>
  </div>
</template>

<script>
export default {
  name: 'yjr-head',
  data() {
    return {
      name: JSON.parse(localStorage.getItem('manager')).mname
    }
  },
  methods: {
    logoutbtn() {
      localStorage.removeItem('manager')
      this.$router.replace('/login')
    }
  }
}
</script>

<style lang="less" scoped>
.yjr-headcontant {
  width: 100%;
  height: 68px;
  position: relative;
  padding: 10px 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 3px 10px#202646;
  .leftlogo {
    height: 100%;
    margin: 0 10px;
  }
  .title {
    height: 100%;
  }
  span {
    margin: 0 10px;
    font-size: 2.5vw;
    font-weight: 600;
    color: #fff;
    // height: 100%;
    display: flex;
    text-align: center;
    align-items: center;
    line-height: 100%;
    display: inline-block;
    word-spacing: 20px;
  }
  .backimg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    // filter: blur(2px);
    // background-image: url('@/assets/headback.jpg');
    background-color: #334154;
    z-index: -1;
  }
  button {
    height: 100%;
    background: none;
    border: none;
    margin: 0 10px;
    font-size: 1.1vw;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: rgb(193, 193, 193);

    &:focus {
      outline: none;
    }
    &:hover {
      color: rgb(154, 154, 154);
    }
  }
}
</style>
