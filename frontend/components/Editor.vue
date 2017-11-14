<template>
  <textarea></textarea>
</template>

<script>
window.CodeMirror = require('codemirror')
require('codemirror/lib/codemirror.css')
require('codemirror/mode/gfm/gfm.js')
require('codemirror/mode/javascript/javascript.js')
require('codemirror/theme/base16-light.css')

export default {
  props: {
    code: String,
    value: String,
  },
  data: function() {
    return {
      content: ''
    }
  },
  created: function() {
    
  },
  mounted: function() {
    var _this = this
    this.editor = CodeMirror.fromTextArea(this.$el, {
      mode: 'gfm',
      lineNumbers: false,
      matchBrackets: true,
      lineWrapping: true,
      theme: 'base16-light',
      extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"}
    })
    this.editor.setValue(this.code || this.value || this.content)
    this.editor.on('change', function(cm) {
        _this.content = cm.getValue()
        if (!!_this.$emit) {
          _this.$emit('change', _this.content)
          _this.$emit('input', _this.content)
        }
      })
  },
  code: function(newVal, oldVal) {
    var editor_value = this.editor.getValue()
    if (newVal !== editor_value) {
      var scrollInfo = this.editor.getScrollInfo()
      this.editor.setValue(newVal)
      this.content = newVal
      this.editor.scrollTo(scrollInfo.left, scrollInfo.top)
    }
  },
  value: function(newVal, oldVal) {
    var editor_value = this.editor.getValue()
    if (newVal !== editor_value) {
      var scrollInfo = this.editor.getScrollInfo()
      this.editor.setValue(newVal)
      this.content = newVal
      this.editor.scrollTo(scrollInfo.left, scrollInfo.top)
    }
  },

}
</script>
