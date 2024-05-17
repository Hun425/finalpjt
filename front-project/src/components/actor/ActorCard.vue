<template>
  <div>
    <img class="profile" :src="'https://image.tmdb.org/t/p/w500/'+ actor.profile_path" alt="">
    <p class="actorNm">{{ actor.name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    actor:Object,
  })
</script>

<style scoped>
  .profile {
    height:270px;
    width: 181px;
    border-radius: 10px 10px 0px 0px;
  }

  .actorNm {
    font-size: 20px;
    font-weight: bold;
    margin: 10px 0 0 10px;
  }
</style>