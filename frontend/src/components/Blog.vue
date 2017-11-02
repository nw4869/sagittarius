<template>
  <main role="main" class="blog">
    <div class="blog-title"><h2>{{title}}</h2></div>
  	<article class="post-list" v-for="post in posts" :key="post.title">
  	  <!--<a :href="post.url" class="post-list-item">{{ post.title }}</a>-->
      <router-link :to="{ name: 'post', params: { id: post.id }}" class="post-list-item">{{ post.title }}</router-link>
  	</article>
  </main>


</template>

<script>
export default {
  name: 'blog',
  data () {
    return {
      title: 'Sagittarius',
      posts: []
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      this.$http.get('/api/posts/').then(function (response) {
        console.log(response.data.results)
        this.posts = response.data.results
      })
    }
  }
}
</script>

<style scoped>
.blog {
  padding: 32px 12px 32px 12px;
}

.blog-title {
  margin-bottom: 32px;
}
.post-list {
  margin-bottom: 8px;
}

.post-list-item{
  color: #428bca;
}
</style>
