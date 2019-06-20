<template>
   <div>

      <div v-for="artchapter in artchapters">       

        <router-link class="nav-link" :to="{path:'/edit_chapter',query:{id:artchapter.article_id,idd:artchapter.id}}" v-if="art_id==artchapter.article_id">

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
</style>