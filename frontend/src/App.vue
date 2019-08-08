<template>
  <div id="app">    
    <Vheader></Vheader>
    <router-view/> 
    <!-- 出口 -->
    <Vfooter></Vfooter>

  </div>
</template>

<script>
//使用import导入组件
import Vheader from "./components/Vheader"
import Vfooter from "./components/Vfooter"
import 'bootstrap/dist/css/bootstrap.min.css'

import $ from 'jquery'

export default {
  name: 'App',
  data(){
    return{

    }
  },
  components:{
    Vheader,
    Vfooter,
  },
  created(){

  },
  mounted(){
    
  },
}
</script>

<style>

</style>
