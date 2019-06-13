<template>
    <div class="article">
        
        <p>
        <table class="table">
       
            <thead v-if="articles">
                <tr>
                  <th scope="col">文章名</th>
                  <th scope="col">简介</th>
                  <th scope="col">发布人</th>
                  <th scope="col">作者</th>
                  <th scope="col">状态</th>
                  <th scope="col">类型</th>
                  <th scope="col">添加日期</th>
                </tr>
             </thead>
        
        
        <tbody>                     
            <tr v-for="article in articles">
              <th scope="row"><router-link class="nav-link" :to="routes[1].url">{{ article.art_name }}</router-link></th>
              <td>{{article.art_introduction}}</td>
              <td>{{article.user_owner}}</td>
              <td>{{article.art_author}}</td>
              <td>{{article.art_status}}</td>
              <td>{{article.art_type}}</td>
              <td>{{article.art_add_date}}</td>
            </tr>                                       
        </tbody>
      
           <!--  <li>没有文章</li> -->
       
        </table>            
        </p>
            <h3>
                <router-link class="nav-link" :to="routes[0].url">{{routes[0].title}}</router-link>
            </h3>
        </div>


</template>
<script>
    export default{
        name:"Vnote",
        data(){
            return{
              routes:[
              {url:'/new_article',title:'发布'},
              {url:'/look_chapter',title:'发布'},
              ],
             

            }
        },
        computed:{
            articles(){
               return this.$store.state.alllist; 
            }
        }
    }
</script>

<style>
</style>