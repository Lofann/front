<template>
<div >
  <h1 class = "text-center mb-5">Вакансии</h1>
<div class= "row" >
  <div v-for="post in posts" :key ="post.id" class="col-md-4" >
    <div class="card mb-4 shadow-sm">
    <div class="card-body">
    <h5 class="card-title">{{post.name}}</h5>
    <p class="card-text">Опубликовано: {{ post.published_at }} <br/> </p>
    <a :href="post.apply_alternate_url" class="btn btn-primary">Перейти</a>
  </div>
</div>
</div>
</div>
</div>
</template>



<!--

-->

<script>
  import axios from "axios";
export default {

  async asyncData(ctx) {
    const { data } = await axios.get(`https://api.hh.ru/vacancies`, { params:{
            'text': 'team lead',
            'specializaxtion': 1,
            'page': 1,
            'per_page': 10,
          }
  });
    return {
      posts: data.items
    }
  }
}


</script>
