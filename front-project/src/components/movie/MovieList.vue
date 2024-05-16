<template>
    <div>
        <h3>MovieList</h3>
        <!-- 데이터 받은 후에 v-for로 전달하기 -->
        <div class="row row-col-3">
            <MovieListItem v-for="exm in example"/>
        </div>
    </div>
</template>

<script setup>
    import MovieListItem from './MovieListItem.vue';
    import {ref} from 'vue'

    const example = ref([1,2,3,4])


</script>

<style>

</style>