<template>
  <article class="post">
    <header>
      <h2>{{ post.title }}</h2>
      <time>{{ post.created | moment("dddd, MMMM Do YYYY, HH:mm") }}</time>
    </header>
    <div id="content" class="content">
        {{ post.content }}
    </div>
  </article>
</template>

<script>
  export default {
    name: 'post',
    data () {
      return {
        post: {
//          title: 'Hello World',
//          content: 'Hahahahaha.',
//          crated: '2017-10-31'
        }
      }
    },
    created () {
      this.fetchData()
    },
    methods: {
      fetchData () {
        this.$http.get('/api/posts/' + this.$route.params.id + '/').then(function (response) {
//          console.log(response.data)
          this.post = response.data
        })
      }
    }

  }
</script>

<style>
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
