/**
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:52:58
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-16 22:29:39
 * @FilePath: \webformanager\src\router\index.js
 * @Description:
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
// import pathArr from '@/router/pathArr.js'

import Login from '@/views/Mylogin.vue'
import Home from '@/views/Myhome.vue'
import roommanage from '@/views/roommanage.vue'
import roomcheck from '@/views/roomcheck.vue'
import innerperson from '@/views/innerperson.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  // 登录的路由规则
  { path: '/login', component: Login },
  // 后台主页的路由规则
  {
    path: '/home',
    component: Home,
    redirect: '/home/check',
    children: [
      { path: 'manage', component: roommanage },
      { path: 'check', component: roomcheck },
      { path: 'person', component: innerperson }
      // 用户详情页的路由规则
      // { path: 'userinfo/:id', component: UserDetail, props: true }
    ]
  }
]

const router = new VueRouter({
  routes
})

// 全局前置守卫
// router.beforeEach(function (to, from, next) {
//   if (pathArr.indexOf(to.path) !== -1) {
//     const manager = localStorage.getItem('manager')
//     if (manager) {
//       next()
//     } else {
//       next('/login')
//     }
//   } else {
//     next()
//   }
// })

export default router
