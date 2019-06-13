<template>
   <div >
              <router-link class="nav-link" :to="routes[0].url">{{routes[0].title}}</router-link>
   </div>
</template>
<script>
    export default{
        name:"Vlook_chapter",
        data(){
            return{
             
              routes:[
                {url:'/edit_chapter',title:'章名'},
              ],
            }
        },
       
    }
</script>

<style>
</style>