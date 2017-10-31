import Vue from 'vue'
import Router from 'vue-router'
import Blog from '@/components/Blog'
import Post from '@/components/Post'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'blog',
      component: Blog
    },
    {
      path: '/:id',
      name: 'post',
      component: Post
    }
  ]
})
