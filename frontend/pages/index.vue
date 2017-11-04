<template>
  <div class="container">
    <main class="main main-font">
      <h2 class="title">Sagittarius</h2>
      <post-list :posts="posts"/>
    </main>
  </div>
</template>

<script>
import PostList from '~/components/PostList.vue'

export default {
  components: {
    PostList
  },
  async asyncData ({ app }) {
    let { data } = await app.$axios.get('/api/posts/')
    return {
      posts: data.results
    }
  }
}
</script>

<style>
.main-font {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main {
  padding: 32px 12px 32px;
}
.title {
  margin-bottom: 32px;
}
</style>
