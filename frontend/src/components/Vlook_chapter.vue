<template>
<div>
  <div v-for="chapterlist in chapterlists" >
    <div v-if="chapterlist.id==art_idd" > 
    
        <div class="container">
            <div class="card">
              <!-- 用v-html输出文章内容 -->
                <div class="card-body" v-html="chapterlist.chapter_content">
                </div>
            </div>
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
              // art_id:this.$route.query.id,
              art_idd:this.$route.query.idd,
            }
        },
        computed:{
            chapterlists(){
               return this.$store.state.allchapterlist;
            },
            articlelists(){
               return this.$store.state.allarticlelist;
            },
        },
       
    }
</script>

<style>
div.card-body{
  padding-bottom:5%;
  word-wrap: break-word;
}
</style>