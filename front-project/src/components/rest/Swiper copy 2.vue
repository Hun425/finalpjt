<template>
  <div class="containers">
    <swiper
      :slidesPerView="4"
      :spaceBetween="57"
      :freeMode="true"
      :pagination="{
        clickable: true,
        el: '.swiper-pagination'  // Add this line to specify the pagination element
      }"
      :modules="modules"
      class="mySwiper"
    >
      <swiper-slide class="card" v-for="actor in actors" :key="actor.name">
        <ActorCard :actor="actor" />
      </swiper-slide>
      <div class="swiper-pagination"></div>  <!-- Ensure this div is included for pagination -->
    </swiper>
  </div>
</template>

<script setup>
import ActorCard from '@/components/actor/ActorCard.vue';
import { ref } from 'vue';
const props = defineProps({
  actors: Array,
});
</script>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/free-mode';
import 'swiper/css/pagination';
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

/* Ensure the pagination bullets are styled properly */
.swiper-pagination {
  bottom: 10px;  /* Adjust the position as needed */
}

.swiper-pagination-bullet {
  background: #007aff;  /* Change color as needed */
}
</style>


