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

    var _this=this;
    $.ajax({
      url:'http://127.0.0.1:8000/api/v1/article/',
      methods:'get',
      datatype:'json',
      success:function(data){
        // console.log(data);
       // 使用 JSON.parse() 方法将字符串数据转换为 JavaScript 对象
         _this.$store.state.allarticlelist=JSON.parse(data);
        // console.log(allarticlelist);
      }

    });
    $.ajax({
      url:'http://127.0.0.1:8000/api/v1/artchapter/',
      // methods:'get',
      success:function(data){
        // console.log(data);

        _this.$store.state.allchapterlist=JSON.parse(data);
        
      }

    });

  },
}
</script>

<style>

</style>
