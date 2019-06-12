import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/components/Index'
import Vmain from '@/components/Vmain'
import Vnote from '@/components/Vnote'


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
      path: '/note',
      name: 'Vnote',//没有关系
      component: Vnote//一个路由映射一个组件
    }
  ]
})
