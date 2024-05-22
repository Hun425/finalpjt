import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const usePosterStore = defineStore('poster', () => {
  const poster = ref({});
  const backdrop = ref({});

  const fetchPoster = async (movieName) => {
    try {
      const response = await axios.get(`movies/gpt/search/`, {
        params: { movie_name: movieName }
      });
      if (response.data.similar_movies && response.data.similar_movies.length > 0) {
        const movie = response.data.similar_movies[0];
        const imageUrl = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
        const backdropUrl = `https://image.tmdb.org/t/p/w1280${movie.backdrop_path}`;
        poster.value[movieName] = imageUrl;
        backdrop.value[movieName] = backdropUrl;
      } else {
        console.error('No movie found with the name:', movieName);
      }
    } catch (error) {
      console.error('Error fetching poster:', error);
    }
  };

  return { poster, backdrop, fetchPoster };
}, { persist: true });
