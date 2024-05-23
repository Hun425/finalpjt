<template>
    <div>안녕안여</div>
    <div class="container">
      <div class="carousel" :style="carouselStyle">
        <div
          class="card"
          v-for="(movie, index) in movies"
          :key="movie.id"
          :class="{ selected: selectedCard === index }"
          @click="selectCard(index)">
          <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" class="poster" />
          <div class="info">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.overview }}</p>
            <p>Rating: {{ movie.vote_average }}</p>
            <p>Release Date: {{ movie.release_date }}</p>
            <div class="actors">
              <span v-for="actor in movie.actors" :key="actor.pk">{{ actor.name }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
    
  <script setup>
  import { ref, computed } from 'vue'
  import axios from 'axios'
  
  const movies = ref([])
  const selectedCard = ref(4);
  const fetchMovies = (page = 1) => {
    axios.get('/movies/', { params: { page } })
        .then(res => {
        movies.value = res.data.results
        // totalPages.value = Math.ceil(res.data.count / 20)
        // currentPage.value = page
        })
        .catch(err => console.log(err))
    }
    fetchMovies()
  
  const selectCard = (index) => {
    selectedCard.value = index;
  };
  
  const carouselStyle = computed(() => {
    const offset = selectedCard.value * -20 + 50;
    return {
      transform: `translateX(${offset}%)`,
    };
  });
  </script>
    
  <style scoped>
  .container {
    width: 1440px;
    height: 500px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .carousel {
    display: flex;
    transition: transform 0.5s ease;
  }
  
  .card {
    flex: 0 0 20%;
    transition: transform 0.5s ease;
    margin: 0 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    transform: scale(0.8);
  }
  
  .card.selected {
    transform: scale(1);
  }
  
  .poster {
    width: 100%;
    height: auto;
    border-radius: 10px;
  }
  
  .info {
    text-align: left;
    padding: 10px;
  }
  
  .actors {
    display: flex;
    flex-wrap: wrap;
  }
  
  .actors span {
    margin-right: 5px;
    font-size: 0.9em;
  }
  </style>
  
<!-- 
//   const getMovieData = () => {
    //     console.log(store.token)
    //     axios({
    //         method:"get",
    //         url:"http://127.0.0.1:8000/movies/recommended/",
    //         headers: {
    //         Authorization: `Token ${store.token}`
    //     },
    //     })
    //     .then(res => {
    //         movies.value = res.data
    //         console.log(movies.value)
    //     })
    //     .catch(err=> console.log(err))
    //   }
    //   getMovieData() -->