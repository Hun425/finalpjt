<template>
    <div class="mainText">전체 영화</div>
    <div>
        <MovieList />
    </div>
  </template>
  
  <script setup>
    import MovieList from '@/components/movie/MovieList.vue'
    
  </script>
  
  <style scoped>
    .mainText {
      margin: 30px 0;
      font-weight: bold;
      font-size: 24px;
      text-align: center;
    }
  </style>
  
  <!-- 
  <template>
    <div class="slide">
      <swiper
      :pagination="{
        type: 'fraction',
      }"
      :navigation="true"
      :modules="modules"
      class="mySwiper"
      >
      <swiper-slide>
          <img src="@/assets/common.jpg" alt="">
      </swiper-slide>
      <swiper-slide>Slide 2</swiper-slide><swiper-slide>Slide 3</swiper-slide>
      <swiper-slide>Slide 4</swiper-slide><swiper-slide>Slide 5</swiper-slide>
      <swiper-slide>Slide 6</swiper-slide><swiper-slide>Slide 7</swiper-slide>
      <swiper-slide>Slide 8</swiper-slide><swiper-slide>Slide 9</swiper-slide>
    </swiper>
  </div>
  </template>
  <script>
    // Import Swiper Vue.js components
    import { Swiper, SwiperSlide } from 'swiper/vue';
  
    // Import Swiper styles
    import 'swiper/css';
  
    import 'swiper/css/pagination';
    import 'swiper/css/navigation';
  
    // import required modules
    import { Pagination, Navigation } from 'swiper/modules';
  
    export default {
      components: {
        Swiper,
        SwiperSlide,
      },
      setup() {
        return {
          modules: [Pagination, Navigation],
        };
      },
    };
  </script>
  
  <style>
  
  .slide {
    position: relative;
    height: 260px;
    width:800px;
  
  }
  
  /* body {
    background: #eee;
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    font-size: 14px;
    color: #000;
    margin: 0;
    padding: 0;
  } */
  
  .swiper {
    width: 100%;
    height: 100%;
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
    height: 100%;
    object-fit: cover;
  }
  
  </style>
  
   -->
  