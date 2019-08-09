<template>
    <div class="container">
   <h3>
          <router-link class="nav-link" :to="{path:'/article_list',query:{pageNum:2,pageSize:1}}">xiayiye</router-link>
        </h3>{{total_count}}{{previous_url}}{{next_url}}
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
              total_count:[], //总数          
              pagenum_id:this.$route.query.pageNum,//第n页
              pagesize_id:this.$route.query.pageSize,//第n页显示数量

            }
        },
        mounted(){
          axios
            // .get('http://www.ohlaa.com/api/v1/article/?page='+this.pagenum_id+'&size='+this.pagesize_id)
            .get('http://127.0.0.1:8000/api/v1/article/?page='+this.pagenum_id+'&size='+this.pagesize_id)
            .then(response => (this.articles = response.data.results,this.total_count = response.data.count))
            .catch(function (error) { // 请求失败处理
              console.log(error);
            });

        },
    }
</script>

<style>
</style>