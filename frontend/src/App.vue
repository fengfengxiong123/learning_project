<template>
  <div id="app">
    <Vheader></Vheader>

    <router-view/> 
    <!-- 出口 -->
    <Vfooter></Vfooter>

  </div>
</template>

<script>
import Vheader from "./components/Vheader"
import Vfooter from "./components/Vfooter"
import 'bootstrap/dist/css/bootstrap.min.css'

import $ from 'jquery'
export default {
  name: 'App',
  components:{
    Vheader,
    Vfooter,
  },
  created(){

  },
  mounted(){

    var _this=this;
    $.ajax({
      url:'http://127.0.0.1:8000/api/article/',
      methods:'get',
      success:function(data){
        console.log(data);

        _this.$store.state.alllist=data;
        // console.log(_this);
      }

    })
  },
}
</script>

<style>

</style>
