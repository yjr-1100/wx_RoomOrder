/**
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:52:58
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-11 20:01:36
 * @FilePath: \webformanager\src\main.js
 * @Description:
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'

// 导入样式
import './assets/css/bootstrap.css'
import './index.css'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
