<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:22:45
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 13:51:59
 * @FilePath: \webformanager\src\components\Myleftnavigator.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-leftnavigatorcontant">
    <ul class="menu">
      <li class="menu-item" v-if="m2org == 1"><router-link to="/home/orgmanageset">组织和管理</router-link></li>
      <li class="menu-item" v-else><router-link to="/home/check">预约审核</router-link></li>
      <li class="menu-item" v-if="m2org == 1"><router-link to="/home/wxset">小程序设置</router-link></li>
      <li class="menu-item" v-else><router-link to="/home/manage">教室管理</router-link></li>
      <li class="menu-item" v-if="m2org != 1"><router-link to="/home/person">成员管理</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'yjr-leftnavigator',
  props: ['m2org']
}
</script>

<style lang="less" scoped>
.yjr-leftnavigatorcontant {
  height: 100%;
  width: 130px !important;
  position: relative;
  background-color: #334154;
  box-shadow: 3px 0 10px#272e55;
  padding: 0;
  ul {
    height: 100%;
    width: 130px !important;
    li {
      width: 100%;
      text-align: center;
      height: 50px;
    }
  }
}
.menu {
  list-style-type: none;
  padding: 10px 0 0 0;
  .menu-item {
    line-height: 50px;
    font-weight: bold;
    font-size: 14px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    &:hover {
      background-color: #2f569f;
      cursor: pointer;
    }
    a {
      display: block;
      color: rgb(255, 255, 255);
      padding: 0 30px;
      &:hover {
        text-decoration: none;
      }
    }
  }
}
.router-link-active {
  background-color: #3a5271;
  box-sizing: border-box;
  position: relative;
  // 伪元素实现路由高亮效果
  &::before {
    content: ' ';
    display: block;
    width: 4px;
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
    background-color: #42b983;
  }
}
</style>
