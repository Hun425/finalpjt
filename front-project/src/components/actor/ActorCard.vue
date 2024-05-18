<template>
  <div>
    <img class="profile" :src="'https://image.tmdb.org/t/p/w500/'+ actor.profile_path" alt="">
    <p class="actorNm">{{ actor.name }}</p>
  </div>
</template>

<script setup>
  const props = defineProps({
    actor:Object,
  })
  // console.log(props)
</script>

<style scoped>
  .profile {
    height:180px;
    width: 120px;
    border-radius: 10px 10px 0px 0px;
  }

  .actorNm {
    width:120px;
    font-size: 16px;
    font-weight: bold;
  }
</style>