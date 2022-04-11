<!--
 * @Author: YJR-1100
 * @Date: 2022-04-11 14:42:52
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-11 20:00:54
 * @FilePath: \webformanager\src\App.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="main">
    <!-- <h1>APP跟组件</h1> -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="less" scoped>
.main {
  width: 100%;
  height: 100%;
}
</style>
