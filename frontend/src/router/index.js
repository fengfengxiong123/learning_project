import Vue from 'vue'
import Router from 'vue-router'

import Vmain from '@/components/Vmain'
import Varticle from '@/components/Varticle'
import Vnew_article from '@/components/Vnew_article'
import Vlook_chapter from '@/components/Vlook_chapter'
import Vedit_chapter from '@/components/Vedit_chapter'

Vue.use(Router)

//抛出
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Vmain',//没有关系
      component: Vmain//一个路由映射一个组件
    },
    {
      path: '/article',
      name: 'Varticle',//没有关系
      component: Varticle//一个路由映射一个组件
    },
    {
      path: '/new_article',
      name: 'Vnew_article',//没有关系
      component: Vnew_article//一个路由映射一个组件
    },
    {
      path: '/look_chapter',
      name: 'Vlook_chapter',//没有关系
      component:Vlook_chapter//一个路由映射一个组件
    },
    {
      path: '/edit_chapter',
      name: 'Vedit_chapter',//没有关系
      component:Vedit_chapter//一个路由映射一个组件
    },
  ]
})
