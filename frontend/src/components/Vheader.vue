<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">文章</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">

    <ul class="navbar-nav mr-auto">
      <li v-for='(item,index) in routes' :class="{active:index==currentIndex}" @click='activeHandler(index)'>
        <router-link class="nav-link" :to="item.url">{{item.title}}</router-link>
      </li>     
    </ul>

    <ul class="navbar-nav mr-auto">
        <form class="form-inline mr-auto my-2 my-lg-0" method="get" action="{% url 'learning_logs:search' %}">
          <!-- {{csrf_token}} -->
          <input class="form-control mr-sm-2" type="search" placeholder="搜索" aria-label="Search" name="search_name" required>
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
        </form>
    </ul>

<!--     <ul class="navbar-nav mr-right">
        {% if user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link active" >您好, {{ user.username }}.</a>
          </li>    
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'users:logout' %}">退出</a>
          </li>
        {% else %}
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'users:register' %}">注册</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'users:login' %}">登录</a>
          </li>
        {% endif %}
    </ul>   -->

  </div>
</nav>
</template>

<script>
    export default{
        name:"Vnote",
        data(){
            return{
                routes:[
                {url:'/',title:'首页'},
                {url:'/note',title:'笔记'}
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