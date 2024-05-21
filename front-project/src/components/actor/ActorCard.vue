<template>
  <div class="card">
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
  .card {
    border: 1px solid rgb(239, 239, 239);
    border-radius: 10px;
    box-shadow: 1px 3px 1px 1px rgb(234, 234, 234);
  }
  .profile {
    height :180px;
    width : 120px;
    border-radius: 10px 10px 0px 0px;
  }

  .actorNm {
    width:120px;
    padding: 8px 0;
    font-size: 12px;
    font-weight: bold;
  }
</style>