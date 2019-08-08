// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
Vue.config.productionTip = false

import Vuex from 'vuex'
Vue.use(Vuex);

// 如果在模块化构建系统中，请确保在开头调用了 Vue.use(Vuex)
const store = new Vuex.Store({
    state:{
        //这个状态跟每个组件数据属性关联
        //作品列表
        allarticlelist:[],

        //章节列表
        allchapterlist:[],
    },
    mutations:{
        //此方法用于修改state
    }
})




/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
