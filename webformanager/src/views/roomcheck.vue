<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:31:23
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-14 00:13:46
 * @FilePath: \webformanager\src\views\roomcheck.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-roomcheckcontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
  </div>
</template>

<script>
export default {
  name: 'yjr-roomcheck'
}
</script>

<style lang="less" scoped>
.yjr-roomcheckcontant {
  height: 100%;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
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
    background-image: url('@/assets/loginbackimg.jpg');
    background-size: 100% 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(2px);
  }
}
</style>
