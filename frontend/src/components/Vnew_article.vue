<template>
   <div class="Vnew_article">
       {{msg}}
       请输入：<input type="text" name="" v-model="art_nameHander"/>
       请输入：<input type="text" name="" v-model="art_typeHander"/>
       <!-- 请输入：<input type="text" name="" v-model="user_ownerHander"/> -->
       <button class="btn btn-success" @click="addArticle">提交</button>
   </div>
</template>
<script>
    import $ from 'jquery'
    export default{
        name:"Vnew_article",
        data(){
            return{
              msg:'new_article',
              
            }
        },
        methods:{
          addArticle(){
            var _this=this;
            var json={
              art_name:this.art_nameHander,
              art_type:this.art_typeHander,

            }
            console.log(json);
            
            $.ajax({
              url:"http://127.0.0.1:8000/api/v1/article/",
              type:'post',
              data:'json',
              success:function(data){
                
                _this.$store.state.allarticlelist=data;
                console.log(data);
              },
              error:function(err){
                console.log(err);
              }
            })
          }
        },
        computed:{
          art_nameHander:{
            set:function(newValue){
              console.log(newValue)
              this.$store.state.allarticlelist.art_name=newValue;
            },
            get:function(){
              return this.$store.state.allarticlelist.art_name;
            }
          },
          art_typeHander:{
            set:function(newValue){
              console.log(newValue)
              this.$store.state.allarticlelist.art_type=newValue;
            },
            get:function(){
              return this.$store.state.allarticlelist.art_type;
            }
          },
        },
       
    }
</script>

<style>
</style>