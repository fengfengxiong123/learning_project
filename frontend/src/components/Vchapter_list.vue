<template>
   <div class="container rowrow">

      <div class="nav-link" v-for="artchapter in artchapters" v-if="art_id==artchapter.article_id"> 
          <router-link  :to="{path:'/look_chapter',query:{id:artchapter.article_id,idd:artchapter.id}}" >
         {{artchapter.chapter_name}}
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
              
            }
        },
        computed:{
            artchapters(){
               return this.$store.state.allchapterlist;
            },
        },
  }
</script>

<style>
.rowrow{
  column-count:2;
  -webkit-column-count:2;
  -moz-column-count:2; 
}


</style>