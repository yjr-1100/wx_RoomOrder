/**
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:52:58
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-13 20:59:03
 * @FilePath: \webformanager\src\main.js
 * @Description:
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import qs from 'qs'

// 导入样式
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/bootstrap.css'
import './index.css'
import './assets/css/iconfont.css'

Vue.use(ElementUI)
axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1'
axios.defaults.timeout = 5000
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
Vue.prototype.$http = axios
Vue.prototype.$qs = qs

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
