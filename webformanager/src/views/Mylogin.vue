<!--
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:55:32
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-11 20:58:35
 * @FilePath: \webformanager\src\views\Mylogin.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-logincontainer">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="login-box">
      <div class="leftimg">
        <img src="@/assets/loginleftimg2.png" alt="" />
      </div>
      <div class="rightlogin"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyLogin'
}
</script>

<style lang="less" scoped>
.yjr-logincontainer {
  width: 100%;
  height: 100%;
  position: relative;
  .backimg {
    height: 100%;
    filter: blur(2px);
    width: 100%;
    background-image: url('@/assets/loginbackimg4.jpg');
    background-size: 100% 100%;
    background-repeat: no-repeat;
  }
  .backmask {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(235, 235, 235, 0.4);
  }
  .login-box {
    width: 65rem;
    height: 35rem;
    background-color: #fff;
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: 45%;
    transform: translate(-50%, -50%);
    box-shadow: 5px 8px 6px rgba(45, 36, 70, 0.561);
    display: flex;
    justify-content: center;
    align-items: center;
    .leftimg {
      flex: 4;
      display: flex;
      justify-content: center;
      img {
        width: 90%;
      }
    }
    .rightlogin {
      flex: 3;
    }
  }
}
</style>
