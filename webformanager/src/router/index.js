/**
 * @Author: YJR-1100
 * @Date: 2022-04-11 19:52:58
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 20:55:38
 * @FilePath: \webformanager\src\router\index.js
 * @Description:
 * @
 * @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import pathArr from '@/router/pathArr.js'

import Login from '@/views/Mylogin.vue'
import Home from '@/views/Myhome.vue'
import roommanage from '@/views/roommanage.vue'
import roomcheck from '@/views/roomcheck.vue'
import innerperson from '@/views/innerperson.vue'
import wxset from '@/views/wxroomorderset.vue'
import orgset from '@/views/organdmanagerset.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login', name: 'login' },
  // 登录的路由规则
  { path: '/login', component: Login },
  // 后台主页的路由规则
  {
    path: '/home',
    component: Home,
    name: 'home',
    redirect: '/home/check',
    children: [
      { path: 'wxset', component: wxset, name: 'wxset' },
      { path: 'orgmanageset', component: orgset, name: 'orgmanageset' },
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
router.beforeEach(function (to, from, next) {
  if (pathArr.managerpath.indexOf(to.path) !== -1) {
    const manager = localStorage.getItem('manager')
    if (manager) {
      next()
    } else {
      next('/login')
    }
  } else if (pathArr.superpath.indexOf(to.path) !== -1) {
    const manager = JSON.parse(localStorage.getItem('manager'))
    if (manager && manager.m2org === 1) {
      next()
    } else {
      alert('权限不足')
      next('/home')
    }
  } else {
    next()
  }
})

export default router
