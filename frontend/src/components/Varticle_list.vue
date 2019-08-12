<template>
    <div class="container">

        <div style="text-align:center">
          <el-pagination
               background
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="pageNum"
            :page-sizes="[10, 20, 30, 50]"
            :page-size="pageSize"
            layout=" sizes, prev, pager, next, jumper"
            :total="total">
          </el-pagination>
        </div>
        <p>
        <table class="table">
          <thead v-if="tableData">
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
            <tr v-for="item in tableData">

              <th scope="row"><router-link class="nav-link" :to="{path:'/chapter_list',query:{id:item.id}}">{{ item.art_name }}</router-link></th>
              <td>{{item.art_introduction}}</td>
              <!-- <td>{{item.user_owner_username}}</td> -->
              <td>{{item.art_author}}</td>
              <!-- <td>{{item.art_status}}</td> -->
              <!-- <td>{{item.art_type}}</td> -->
              <!-- <td>{{item.art_add_date}}</td> -->
            </tr>                                       
          </tbody>
        </table>            
        </p>
        <div style="text-align:center">
          <el-pagination
               background
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="pageNum"
            :page-sizes="[10, 20, 30, 50]"
            :page-size="pageSize"
            layout=" sizes, prev, pager, next, jumper"
            :total="total">
          </el-pagination>
        </div>

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
              tableData: [],  //请求的数据
              total: 0,      //总数
              pageNum:1,    //当前页
              pageSize:10,  //当前页数据数量
              search_name:'',//搜索名称
            }
        },
        created(){
            this.getUserList()
        },
        methods:{
            handleSizeChange(size){
                this.pageSize=size;
                this.getUserList();
            },
            handleCurrentChange(current){
                this.pageNum=current;
                this.getUserList();
            },
            handleSearchName(name){
                this.search_name=name;
                this.getUserList();
            },
            getUserList(){
                // axios.get('http://127.0.0.1:8000/api/v1/article/?',
                axios.get('http://www.ohlaa.com/api/v1/article/?',
                    {headers:{},
                      params:{
                        pageNum:this.pageNum,
                        pageSize:this.pageSize,
                        search_name:this.search_name
                      }
                    }).then((res)=>{
                      const data =res.data
                      this.tableData=data.data;
                      this.total=data.lens;
                      // console.log(res.data);
                    });
                }
            },
        mounted(){
        },
    }
</script>

<style>
</style>