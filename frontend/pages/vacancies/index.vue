<template>

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
