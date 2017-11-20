module.exports = {
  mode: 'spa',
  /*
  ** Headers of the page
  */
  head: {
    title: 'Sagittarius',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'Sagittarius', name: 'Sagittarius', content: 'Sagittarius A*' }
    ],
    link: [
      // { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#428bca' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      const babelLoader = config.module.rules.find((rule) => rule.loader === 'babel-loader')
      babelLoader.exclude = /node_modules\/(?![eth-sig-util])/

      }
    },
    vendor: ['axios'],
    publicPath: '/static/'
  },

  plugins: [
    '~/plugins/moment'
  ],

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/bootstrap-vue'
  ],

  axios: {
    // proxyHeaders: false
  }
}
