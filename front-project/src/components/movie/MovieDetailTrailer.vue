<template>
  <div>
    <div v-if="videoId" class="trailer-container">
      <p class="trailer-text">공식 예고편</p>
      <!-- <iframe class="movietrailer"
        :src="'https://www.youtube.com/embed/' + videoId"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe> -->
        <!-- 밑에는 css 적용용!! -->
      <iframe class="movie-trailer"
        :src="'https://www.youtube.com/embed/' + videoId"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
    <div v-else-if="searched && !videoId">
      <p>영상이 없습니다</p>
    </div>
  </div>
</template>
  
<script setup>
   import {ref} from 'vue'
   import axios from 'axios';
   const props = defineProps({
    title:String,
   })
  //  const videoId = ref(null);  테스트 끝나고 실제로 돌릴때는 수정하기!!
  // const searched = ref(false);
  // const videoId = ref("Fyo6plo4WdY");
  const videoId = ref("");

  const searched = ref(true);
  const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY

  const searchVideo = () => {
    // console.log(import.meta.env.VITE_YOUTUBE_API_KEY)
    axios({
      method:'get',
      url:'https://www.googleapis.com/youtube/v3/search',
      params: {
        key: youtubeKey,
        part: 'snippet',
        type: 'video',
        q: `영화 ${props.title} 공식 예고편`,
        maxResults:1
      }
    })
    .then(response => {
      const videos = response.data.items;
      if (videos.length > 0) {
        videoId.value = videos[0].id.videoId;
        console.log(videoId.value)
      } else {
        videoId.value = null;
      }
      searched.value = true;
    })
    .catch(error => {
      console.error('Error fetching videos:', error);
      videoId.value = null;
      searched.value = true;
    });
  };
  searchVideo()



</script>
  
<style scoped>
  .trailer-container {
    margin: 0 auto;
    width:800px;
    height:450px;
    margin-bottom: 100px;
  }

  .trailer-text {
    font-weight: bold;
    font-size: 24px;
    text-align: center;
    margin: 30px 0;
  }
  .movie-trailer {
    width: 100%;
    height: 100%;
  }
</style>