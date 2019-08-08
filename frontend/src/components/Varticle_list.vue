<template>
    <div class="container">
<!--    <h3>
          <router-link  :to="routes[0].url">{{routes[0].title}}</router-link>
        </h3> -->
        <p>
        <table class="table">
          <thead v-if="articles">
            <tr>
              <th scope="col">文章名</th>
              <th scope="col">简介</th>
              <!-- <th scope="col">发布人</th> -->
              <th scope="col">作者</th>
              <!-- <th scope="col">状态</th> -->
              <!-- <th scope="col">类型</th> -->
              <!-- <th scope="col">日期</th> -->
            </tr>
          </thead>    
          <tbody>    
            <tr v-for="article in articles">

              <th scope="row"><router-link class="nav-link" :to="{path:'/chapter_list',query:{id:article.id}}">{{ article.art_name }}</router-link></th>
              <td>{{article.art_introduction}}</td>
              <!-- <td>{{article.user_owner_username}}</td> -->
              <td>{{article.art_author}}</td>
              <!-- <td>{{article.art_status}}</td> -->
              <!-- <td>{{article.art_type}}</td> -->
              <!-- <td>{{article.art_add_date}}</td> -->
            </tr>                                       
          </tbody>
        </table>            
        </p>


        </div>
</template>

<script>
    export default{
        name:"Varticle_list",
        data(){
            return{
              routes:[
              {url:'/new_article',title:'发布'},
              {url:'/look_chapter',title:'发布'},
              ],
              articles:[],              
              id:this.$route.query.pageNum,
            }
        },
        mounted(){
          axios
            .get('http://127.0.0.1:8000/api/v1/article/?page='+this.id)
            .then(response => (this.articles = response.data.results))
            .catch(function (error) { // 请求失败处理
              console.log(error);
            });
        },
    }
</script>

<style>
</style>