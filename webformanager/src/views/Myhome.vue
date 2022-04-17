<!--
 * @Author: YJR-1100
 * @Date: 2022-04-11 17:50:51
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 16:47:37
 * @FilePath: \webformanager\src\views\Myhome.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->

<template>
  <div class="yjr-homecontant">
    <!-- 头部 -->
    <myhead></myhead>
    <!-- body -->
    <div class="mainbody">
      <!-- 左侧边栏 -->
      <navigator :m2org="m2org"></navigator>
      <!-- 右边主体 -->
      <div class="right-main-body">
        <router-view :tooken="tooken" :datatooken="datatooken"></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import myhead from '@/components/Myhead.vue'
import navigator from '@/components/Myleftnavigator.vue'
// import bus from '@/router/EventBus.js'
export default {
  name: 'yjr-home',
  data() {
    return {
      m2org: null,
      tooken: null,
      datatooken: 'MTY1MDE4OTA4MC4xMTk2Mzc1OjIwNGQyZTkyZTdiNmFjMjUwYjE0MDJiNjNlOGIyMmU0YmVjZTIzZGU='
    }
  },
  created() {
    this.m2org = this.$route.params.m2org
    this.tooken = this.$route.params.tooken
    this.datatooken = this.$route.params.tooken.replace('M', 'Teings').replace('1', 'OjIwN')
  },
  // 注册组件
  components: {
    myhead,
    navigator
  }
}
</script>

<style lang="less" scoped>
.yjr-homecontant {
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  .mainbody {
    flex: 1;
    display: flex;
    flex-direction: row;
    position: relative;
    .right-main-body {
      flex: 1;
      position: relative;
    }
  }
}
</style>
