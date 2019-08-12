<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
<!--                   <div class="card-header">
                    哦啦-_-创造者平台
                  </div> -->
                  <div class="card-body">
                    
                    <!-- <router-link class="btn btn-primary" :to="{path:'/article_list',query:{pageNum:1}}">去学习</router-link> -->
                    <div style="float:right">
                    <router-link class="btn btn-primary" :to="{path:'/article_list'}">去看</router-link>
                    </div>
                    <div>《西游记》、《三国演义》、《水浒传》、《红楼梦》、《论语》、《道德经》、古典文学、古代小说、名著</div>

                  </div>
                  <div class="card-body">
                    <h6 class="card-title">先学习，后娱乐！</h6>
                  </div>
                </div>
            </div>
        </div>
       <div>
            <div class="py-3 bg-white fixed-bottom">
                <div class="container">
                    <p class="m-0 text-center text-dark">Copyright &copy; www.ohlaa.com 2019
                    </p>
                </div>
            </div>
        </div>
    </div>

</template>
<script>
    export default{
        name:"Vmain",
        data(){
            return{
            }
        },


    }
</script>

<style>
</style>