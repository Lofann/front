<template class>

    <div>

    <h1>{{posts.title}}</h1>

    <div>
    <div class="bg-light me-md-3 pt-3 px-3 pt-md-5 px-md-5 text-center overflow-hidden">
      <img :src = posts.image style="height: 512px">
      <div class="my-3 p-3">
        <p class="lead">{{posts.text}}</p>
      </div>

    </div>
  </div>
    </div>

</template>

<script>

import axios from "axios";
export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/home/`);
    return {
      posts: data[0]
    }
  }
}




</script>
