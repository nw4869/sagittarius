<template>
  <div class="post-list">
    <article class="post-list-item" v-for="post in posts" :key="post.title">
      <router-link :to="{ name: 'post', params: { post: post.id }}" class="post-list-item-link">{{ post.title }}</router-link >
    </article>
  </div>
</template>

<script>
export default {
  props: ['posts']
}
</script>

<style>
.post-list-item {
  margin-bottom: 8px;
}
.post-list-item-link {
  color: #428bca;
}
</style>

