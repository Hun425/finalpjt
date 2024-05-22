<script setup>
  import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';
  import Navbar from '@/components/common/Navbar.vue'

  import { useAccountStore } from '@/stores/account';
  const store = useAccountStore()
  store.isDark = true
</script>

<template>
  <div class="main-container">
    <div :style="backgroundStyle" class="background-image"></div>
    <div class="overlay">
      <BoxOfficeList @top-movie-poster="updateBackground"/>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import BoxOfficeList from '@/components/movie/BoxOfficeList.vue';

const topMoviePoster = ref('');
const backgroundStyle = computed(() => ({
  backgroundImage: `url(${topMoviePoster.value})`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
  filter: 'blur(8px)',
  height: '100%',
  width: '100%',
  position: 'absolute',
  top: 0,
  left: 0,
  zIndex: -1,
  opacity: 0.5
}));

const updateBackground = (posterUrl) => {
  topMoviePoster.value = posterUrl;
};
</script>

<style scoped>
.main-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.overlay {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* 어두운 오버레이 */
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
