<template>
   <div class="container rowrow">

      <div class="nav-link" v-for="artchapter in artchapters" v-if="art_id==artchapter.article_id"> 
          <router-link  :to="{path:'/look_chapter',query:{id:artchapter.article_id,idd:artchapter.id}}" >
        <!--  <pre>{{artchapter.chapter_name}}</pre>
         <div class="card-body" v-html="item.chapter_content"></div> -->
         <div  v-html="artchapter.chapter_name"></div>
         </router-link>
      </div>
   </div>
</template>
<script>
    export default{
        name:"Vchapter_list",
        data(){
            return{
              //article文章列表页面传递过来的参数 route.query.id给art_id
              art_id:this.$route.query.id,
              artchapters:[]
            }
        },
        computed:{
        },
        mounted(){            
            axios
                .get('http://www.ohlaa.com/api/v1/artchapter/?id='+this.art_id)
                .then(response => (this.artchapters = response.data))
                .catch(function(error){
                    consonle.log(error);
                });
        },


  }
</script>

<style>
.rowrow{
  column-count:2;
  -webkit-column-count:2;
  -moz-column-count:2; 
pre{
    font-family: "微软雅黑";
    white-space: pre-wrap;
    word-wrap: break-word;
}
}


</style>