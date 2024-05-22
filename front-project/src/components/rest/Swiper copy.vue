<!-- 
<template>
  <div class="slide">
    <swiper
    :pagination="{  type: 'fraction',}"
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
  // npm i swiper 필요!!
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
 <template>
  <div class="containers">

    <swiper
    :slidesPerView="4"
    :spaceBetween="57"
    :freeMode="true"
    :pagination="{
      clickable: true,
    }"
    :modules="modules"
    class="mySwiper"
    >
    <swiper-slide class="card" v-for="actor in actors" :key="actor.name">
      <ActorCard :actor="actor"/>
    </swiper-slide>
    <!-- <div class="swiper-pagination swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal">
      <span v-for="actor in actors" class="swiper-pagination-bullet"></span>
    </div> -->
  
  </swiper>
</div>
</template>
<script setup>
  import ActorCard from '@/components/actor/ActorCard.vue'
  import { ref } from 'vue'
  const props = defineProps({
    actors:Array,
  })
</script>
<script>

  
  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  import 'swiper/css/free-mode';
  import 'swiper/css/pagination';


  // import required modules
  import { FreeMode, Pagination } from 'swiper/modules';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [FreeMode, Pagination],
      };
    },
  };
</script>
<style>
.card {
  height: 350px;
  border-radius: 10px;
}

.containers {
  position: relative;
  height: 100%;
}

.swiper {
  width: 100%;
  height: 100%;
}

/* .swiper-slide {
  Center slide text vertically
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
} */
</style>