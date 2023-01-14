<template class>

  <div>
    <h1 class = "text-center mb-5">{{posts.title}}</h1>
  <div>
  <div class="text-center overflow-hidden">
    <div class="my-3 p-3">
      <p class="lead">{{posts.text}}</p>
    </div>
    <img :src = posts.graph style="height: 512px">
  </div>
  </div>
  </div>

</template>
<script>
import axios from "axios";
export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/geography/`);
    return {
      posts: data[0]
    }
  }
}

</script>
