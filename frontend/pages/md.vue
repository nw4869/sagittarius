<template>
    <div>
        {{ '2017-07-09' | moment('dddd, MMMM Do YYYY') }}
        <!-- Bidirectional data binding（双向数据绑定） -->
        <codemirror v-model="source" :options="editorOptions"></codemirror>
        <vue-markdown :source='source'/>
    </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import { codemirror } from 'vue-codemirror'

require('codemirror/mode/gfm/gfm.js')

export default {
    components: {
        VueMarkdown,
        codemirror
    },
    asyncData (context) {
        return {
            source: '# hello \n world',
            editorOptions: {
                mode: 'gfm',
                lineNumbers: false,
                matchBrackets: true,
                lineWrapping: true,
                // theme: 'base16-light',
                // extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"}
            }
        }
    }
}
</script>
