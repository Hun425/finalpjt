<template>
    <div>
      <h5>공식 예고편</h5>
      <p>{{ title }}</p>
    </div>
  </template>
  
  <script setup>
   import {ref} from 'vue'
   const props = defineProps({
    title:String,
   })
  </script>
  
  <style scoped>
  
  </style>