<template>
   <div>
      <div v-for="chapter in chapterlists">       
        <router-link class="nav-link" :to="{path:'/edit_chapter',query:{id:art_id,idd:chapter.id}}" v-if="chapter.article_id==art_id">
          {{chapter.chapter_name}}
        </router-link>
      </div>
   </div>
</template>
<script>
    export default{
        name:"Vchapter_list",
        data(){
            return{
              //art_id为作品id
              art_id:this.$route.query.id,
              
            }
        },
        computed:{
            chapterlists(){
               return this.$store.state.allchapterlist;//
            },
        },
  }
</script>

<style>
</style>