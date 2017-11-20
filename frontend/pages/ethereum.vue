<template>
    <div>
        <button id="ethSignButton" @click="ethSign">eth_sign</button>
        <button id="personalSignButton" @click="personalSign">personal_sign</button>
        <button id="personalRecoverTest" @click="personalRecover">personal_ecRecover</button>
        <button id="ethjsPersonalSignButton">ethjs personal sign</button>
        <button id="signTypedDataButton">sign typed data</button>
    </div>
</template>

<script>
// var ethUtil = require('ethereumjs-util')
// var sigUtil = require('eth-sig-util')


export default {
  methods: {
    ethSign: function () {
    },

    personalSign: function () {
    },

    personalRecover: function() {

    }
  }
}
</script>
