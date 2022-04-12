<!--
 * @Author: YJR-1100
 * @Date: 2022-04-11 17:50:51
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-12 23:03:26
 * @FilePath: \webformanager\src\views\Myhome.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->

<template>
  <div class="yjr-homecontant">
    <!-- 头部 -->
    <myhead></myhead>
    <!-- 左侧边栏 -->
    <!-- 右边主体 -->
  </div>
</template>

<script>
import myhead from '@/components/Myhead.vue'
export default {
  name: 'yjr-home',
  // 注册组件
  components: {
    myhead
  }
}
</script>

<style lang="less" scoped></style>
