<template>
<div class="container">
<nav class="navbar navbar-expand-lg navbar-light bg-light container">
  <ul class="navbar-nav mr-auto">
    <li v-for='(item,index) in routes' :class="{active:index==currentIndex}" @click='activeHandler(index)'>
      <router-link class="nav-link" :to="{path:'/article_list',query:{pageNum:1}}">{{item.title}}</router-link>
    </li>     
  </ul>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
  <ul class="navbar-nav mr-auto">
  <a class="nav-link" href="/">简介</a>
  <!-- <router-link class="nav-link" :to="/">{{item.title}}</router-link> -->
  </ul>


    <ul class="navbar-nav mr-auto">
        <form class="form-inline mr-auto my-2 my-lg-0" method="get" action="{% url 'learning_logs:search' %}">
          <!-- {{csrf_token}} -->
          <input class="form-control mr-sm-2" type="search" placeholder="搜索" aria-label="Search" name="search_name" required>
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
        </form>
    </ul>

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
                {url:'/article_list',title:'书圈'}
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