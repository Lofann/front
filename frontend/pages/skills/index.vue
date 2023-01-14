<template>

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
    <div class="table-responsive mt-5 mb-5">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="tab in posts.table">
              <th scope="col">{{tab.num}}</th>
              <th scope="col">{{tab.city}}</th>
              <th scope="col">{{tab.solary}}</th>
            </tr>
            </tbody>
        </table>
      </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/skills/`);
    return {
      posts: data[0]
    }
  }
}

</script>
