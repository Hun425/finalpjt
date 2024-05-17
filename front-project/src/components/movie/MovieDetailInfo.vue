<!-- 주요 내용을 담을 페이지 -->
<template>
    <div class="mainInfo">
        <div>
            <p class="intro">소개</p>
            <p class="overview">{{ props.overview }}</p>
        </div>
        <div>
            <p class="intro">출현진</p>
            <Swiper :actors="props.actors"/>
        </div>
    </div>
</template>

<script setup>
 import Swiper from '@/components/common/Swiper.vue'
 import { ref } from 'vue'
 const props = defineProps({
    actors:Array,
    overview:String
 })
 console.log(props.overview)
</script>

<style scoped>
    .mainInfo {
        width:900px;
        margin: 50px auto
    }
    .intro {
        font-weight: bold;
        font-size: 24px;
    }
    .overview {
        font-size: 16px;
    }
</style>