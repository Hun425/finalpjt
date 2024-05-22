<template>
  <div>
    <swiper
    :slidesPerView="6"
    :spaceBetween="10"
    :centeredSlides="false"
    :pagination="{
      clickable: true,
    }"
      :modules="[Pagination]"
      class="mySwiper"
      >
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <MovieCard :movie="movie"/>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import MovieCard from '../MovieCard.vue';
import 'swiper/css';
import 'swiper/css/pagination';
import { Pagination } from 'swiper/modules';

// Define props
defineProps({
  movies: Array,
});
</script>

<style scoped>

.swiper {
  width: 100%;
  height: 250px;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 200px;
  object-fit: cover;
}

</style>
