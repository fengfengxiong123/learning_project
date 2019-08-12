<template>
<div>
  <div v-for="item in chaptercontent">
    <div class="container">
        <div class="card">
          <!-- 用v-html输出文章内容 -->
            <div class="card-body" v-html="item.chapter_content"></div>
        </div>
    </div>
  </div>
</div>
</template>
<script>
    export default{
        name:"Vlook_chapter",
        data(){
            return{
              msg:'编辑章',
              art_id:this.$route.query.id,
              chap_idd:this.$route.query.idd,
              chaptercontent:'',
            }
        },
        mounted(){            
            axios
                .get('http://www.ohlaa.com/api/v1/chaptercontent/?id='+this.art_id+'&'+'idd='+this.chap_idd)
                // .get('http://127.0.0.1:8000/api/v1/chaptercontent/?id='+this.art_id+'&'+'idd='+this.chap_idd)
                .then(response => (this.chaptercontent = response.data))
                .catch(function(error){
                    consonle.log(error);
                });
        },

        computed:{
        },
       
    }
</script>

<style>
div.card-body{
  padding-bottom:5%;
  word-wrap: break-word;
}
</style>