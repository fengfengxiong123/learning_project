<template>
   <div >
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
            var json={
              art_name:this.art_nameHander,
              art_type:this.art_typeHander,
              user_owner:'admin',
              user_id:'1',

              
              
              art_introduction: "admin",
              
              art_name_used: "",
              art_status: "完结",
              
              
              
              
            }
            console.log(json);
            var _this=this;
            $.ajax({
              url:"http://127.0.0.1:8000/api/v1/article_list/",
              type:'post',
              data:json,
              success:function(data){
                console.log(data);
                _this.$store.state.allarticlelist=data;
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
              // console.log(newValue)
              this.$store.state.note.art_name=newValue;
            },
            get:function(){
              return this.$store.state.note.art_name;
            }
          },
          art_typeHander:{
            set:function(newValue){
              // console.log(newValue)
              this.$store.state.note.art_type=newValue;
            },
            get:function(){
              return this.$store.state.note.art_type;
            }
          },
          // user_ownerHander:{
          //   set:function(newValue){
          //     // console.log(newValue)
          //     this.$store.state.note.user_owner=newValue;
          //   },
          //   get:function(){
          //     return this.$store.state.note.user_owner;
          //   }
          // },
        },
       
    }
</script>

<style>
</style>