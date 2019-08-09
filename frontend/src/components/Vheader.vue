<template>
<div class="container">

  <nav class="navbar navbar-expand-lg navbar-light bg-light container">

    <div class="col">
      <a class="nav-link" href="/">主站</a>
    </div>
    <div class="col">
      <ul class="navbar-nav mr-auto">
        <li v-for='(item,index) in routes' :class="{active:index==currentIndex}" @click='activeHandler(index)'>
          <router-link class="nav-link" :to="{path:'/article_list',query:{pageNum:1}}">{{item.title}}</router-link>
        </li>     
      </ul>
    </div>
    <div class="col">
      <form class="form-inline mr-auto my-2 my-lg-0">
        <!-- {{csrf_token}} -->
        <input class="form-control  col" type="search" placeholder="" aria-label="Search" name="search_name" required>
        <button class="btn btn-outline-success my-1 my-sm-2 col" style="float:right" type="submit">搜</button>
      </form>
    </div>

  </nav>

</div>
</template>

<script>
    export default{
        name:"Vheader",
        data(){
            return{
                routes:[
                // {url:'/animation',title:'动漫'},
                {url:'/article_list',title:'古文'}
                ],
                currentIndex:0
            }
        },
        methods:{
            activeHandler(index){
                this.currentIndex=index;
            }
        },
        created(){
            // console.log(111)
            for(var i = 0;i < this.routes.length;i++){
                if(this.routes[i].url ==this.$route.path){
                    this.currentIndex=i;
                    return;
                }
            }
        }
    }
</script>

<style>
</style>