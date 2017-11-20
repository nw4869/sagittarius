<template>
    <div>
        {{ '2017-07-09' | moment('dddd, MMMM Do YYYY') }}
        <!-- Bidirectional data binding（双向数据绑定） -->
        <editor v-model="source" :options="editorOptions"></editor>
        <vue-markdown :source='source'/>
    </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import Editor from '~/components/Editor.vue'

require('codemirror/mode/gfm/gfm.js')

export default {
    components: {
        VueMarkdown,
        Editor
    },
    asyncData (context) {
        return {
            source: '# hello \n world',
            editorOptions: {
            //     mode: 'gfm',
            //     lineNumbers: false,
            //     matchBrackets: true,
            //     lineWrapping: true,
            //     // theme: 'base16-light',
            //     // extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"}
            }
        }
    }
}
</script>
