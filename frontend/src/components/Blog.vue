<template>
  <div class="blog container">
  	<div class="list-group" v-for="post in posts">
  	  <a href="#" class="list-group-item list-group-item-action text-left">{{ post.title }}</a>
  	</div>
  </div>


</template>

<script>
export default {
  name: 'blog',
  data () {
    return {
      title: 'Blog App',
      posts: []
    }
  },
  mounted: function () {
    this.$http.get('https://jsonplaceholder.typicode.com/posts').then(function (response) {
      console.log(response.data)
      this.posts = response.data
    })
  }
}
</script>

<style scoped>
  
</style>