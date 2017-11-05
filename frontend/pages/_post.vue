<template>
  <div class="container">
    <article class="post post-font">
      <header>
        <h2>{{ post.title }}</h2>
        <time>{{ post.created | moment("dddd, MMMM Do YYYY, HH:mm") }}</time>
      </header>
      <div id="content" class="content">
          {{ post.content }}
      </div>
    </article>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  components: {
    moment
  },
  async asyncData ({ app, params }) {
    let { data } = await app.$axios.get(`/posts/${params.post}/`)
    return {
      post: data
    }
  }
}
</script>

<style>
.post-font {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.post {
  padding: 21px 12px 21px 12px;
}
time {
  color: #79828B;
}
header {
  margin: 12px 0 12px;
}
.content {
  margin: 12px 0 12px;
}
</style>
