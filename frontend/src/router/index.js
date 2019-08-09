import Vue from 'vue'
import Router from 'vue-router'

import Vmain from '@/components/Vmain'
import Varticle_list from '@/components/Varticle_list'
import Vnew_article from '@/components/Vnew_article'
import Vchapter_list from '@/components/Vchapter_list'
import Vlook_chapter from '@/components/Vlook_chapter'

Vue.use(Router)

//抛出
export default new Router({
  routes: [
    {//主页
      path: '/',
      name: 'Vmain',//没有关系
      component: Vmain,//一个路由映射一个组件
    },

    {//链接作品列表
      path: '/article_list',
      name: 'Varticle_list',
      component: Varticle_list,
    },
    {//链接新建作品页面
      path: '/new_article',
      name: 'Vnew_article',
      component: Vnew_article
    },
    { //链接到章名列表
      path: '/chapter_list',
      name: 'Vchapter_list',
      component:Vchapter_list
    },
    {//链接到章名编辑页面
      path: '/look_chapter',
      name: 'Vlook_chapter',
      component:Vlook_chapter
    },
  ]
})
