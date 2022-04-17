<!--
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:55:32
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 22:27:17
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
      <div class="rightlogin">
        <h2>教室预约审核后台登录</h2>
        <!-- 表单部分 -->
        <div class="formlogin">
          <div>
            <label for="username">用户名</label>
            <input type="text" name="username" id="username" v-model.trim="username" placeholder="请输入管理手机号" />
          </div>
          <div>
            <label for="pwd">密码</label>
            <input type="password" name="password" id="pwd" v-model.trim="password" placeholder="请输入登录密码" @keyup.enter="managelogin" />
          </div>
        </div>
        <h4>{{ message }}</h4>
        <!-- 登录按钮 -->
        <button @click="managelogin">登录</button>
      </div>
    </div>
  </div>
</template>

<script>
// import bus from '@/router/EventBus.js'
export default {
  name: 'MyLogin',
  data() {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  beforeDestroy() {
    // 组件销毁前需要解绑事件。否则会出现重复触发事件的问题
    // bus.$off('tooken')
  },
  methods: {
    async managelogin() {
      this.message = ''
      // 手机号正则
      const mPattern = /^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$/
      if (!this.username || !this.password) {
        this.message = '请输入手机号和密码'
      } else if (!mPattern.test(this.username)) {
        this.message = '手机号格式错误'
      } else {
        const postdata = { username: this.username, password: this.password }
        const { data } = await this.$http.post('/manager/managerlogin', postdata).catch((result) => {
          this.$message.error('网络错误')
        })
        // console.log(data)
        if (data.code === 0) {
          this.message = data.msg
          localStorage.removeItem('manager')
        } else {
          // console.log(data.responsedata)
          localStorage.setItem('manager', JSON.stringify(data.responsedata.dictuser))
          // bus.$emit('tooken', data.responsedata.tooken)
          if (data.responsedata.dictuser.m2org === 1) {
            this.$router.push({
              name: 'orgmanageset',
              params: {
                m2org: 1,
                tooken: data.responsedata.tooken
              }
            })
            // this.$router.push('/home/orgmanageset?m2org=1')
          } else {
            this.$router.push({
              name: 'home',
              params: {
                tooken: data.responsedata.tooken
              }
            })
          }
        }
      }
    }
  }
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
    background-size: cover;
    background-position: center;
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
    width: 60%;
    height: 64%;
    background-color: #fff;
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 6px 8px 6px rgba(64, 52, 97, 0.561);
    display: flex;
    justify-content: center;
    // align-items: center;
    .leftimg {
      flex: 5;
      display: flex;
      justify-content: center;
      align-items: center;
      img {
        width: 90%;
        height: 70%;
      }
    }
    .rightlogin {
      flex: 3;
      display: flex;
      flex-direction: column;
      margin-right: 9%;
      padding: 2% 0;
      h2 {
        font-size: 1.8vw;
        font-weight: 600;
        margin-top: 18%;
        height: 10%;
        width: 100%;
      }
      .formlogin {
        height: 40%;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        div {
          display: flex;
          flex-direction: column;
          height: 50%;
          label {
            font-size: 1.2vw;
            font-weight: 500;
            height: 30%;
            margin-bottom: 2%;
          }
          input {
            width: 100%;
            height: 50%;
            padding: 0 10px;
            border: #b8b8b8 0.5px solid;
            border-radius: 5px;
            font-size: 1vw;
            &:focus {
              outline-color: #919abc;
            }
          }
        }
      }
      h4 {
        color: red;
        font-size: 1vw;
      }
      button {
        margin: 20px auto;
        width: 80%;
        height: 10%;
        background-color: #9fa8c8;
        color: #fff;
        font-size: 1.5vw;
        border: none;
        border-radius: 25px;
        &:hover {
          background-color: #919abc;
        }
        &:focus {
          outline: 0;
        }
      }
    }
  }
}
</style>
