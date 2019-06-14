<template>
   <div>
       {{msg}}
   </div>
</template>
<script>
    export default{
        name:"Vedit_chapter",
        data(){
            return{
              msg:'编辑章名',
              art_id:this.$route.query.id,
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
</style>