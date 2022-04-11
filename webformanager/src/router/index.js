/**
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:52:58
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-11 19:57:24
 * @FilePath: \webformanager\src\router\index.js
 * @Description:
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
 */
import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '@/views/Mylogin.vue'
import Home from '@/views/Myhome.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  // 登录的路由规则
  { path: '/login', component: Login },
  // 后台主页的路由规则
  {
    path: '/home',
    component: Home,
    redirect: '/home/users'
    // children: [
    //   { path: 'users', component: Users },
    //   { path: 'rights', component: Rights },
    //   { path: 'goods', component: Goods },
    //   { path: 'orders', component: Orders },
    //   { path: 'settings', component: Settings },
    //   // 用户详情页的路由规则
    //   { path: 'userinfo/:id', component: UserDetail, props: true }
    // ]
  }
]

const router = new VueRouter({
  routes
})

export default router
