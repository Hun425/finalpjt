<!-- 주요 내용을 담을 페이지 -->
<template>
    <div v-show='actors' class="mainInfo">
        <div class="block">
            <p class="intro">소개</p>
            <p class="overview">{{ props.overview }}</p>
        </div>
        <div>
            <p class="intro">출현진</p>
            <ActorCard v-for="actor in actors" :key='actor.name' :actor='actor'/>
            <!-- <Swiper :actors="props.actors"/> -->
        </div>
    </div>
</template>

<script setup>
import ActorCard from '../actor/ActorCard.vue';
import {ref} from 'vue'
//  import Swiper from '@/components/common/Swiper.vue'
 const overview = ref('')
 const actors = ref([])

 const props = defineProps({
    actors:Array,
    overview:String
 })
 overview.value = props.overview
 actors.value = props.actors
</script>

<style scoped>
    .mainInfo {
        width:900px;
        margin: 50px auto
    }
    .block {
        margin: 0 0 50px 0px ;
    }
    .intro {
        margin: 0 0 15px 0;
        font-weight: bold;
        font-size: 18px;
    }
    .overview {
        font-size: 16px;
    }
</style>