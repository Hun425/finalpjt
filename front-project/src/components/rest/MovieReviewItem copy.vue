<template>
  <div>
    <div class="review">
      <div>
        <div class="profile-box">
          <img class="profile-img" :src="`http://localhost:8000${review.user.profile_pic}`" alt="Profile Picture">
          <p class="">{{ review.user.username }}</p>
        </div>
        <div>
          <p>{{ review.title }}</p>
          <p>{{ review.created_at }}</p>
        </div>
        <div>
      </div>
        <p>{{ isLike ? '❤️':'🤍'}}</p>
      </div>
    </div>
      {{ review }}

      <!-- 수정버튼 누르기 전 -->
      <div v-if="!isUpdate" style="border: 1px solid blue; padding:5px;">
        <p>리뷰 ID :  {{ review.id }}</p>
        <h4 > 제목 : {{ review.title }}</h4>
        <hr>
        <div style="display:flex;">
          <div>
            <p>내용 : {{ review.content }}</p>
            <p>좋아요 수 : {{ review.like_user_count }}</p>
            <div style="color:red">{{ review.like_users }}</div>
            <button @click="likeBtn"><strong>좋아요 버튼</strong></button>
          </div>
          <div style="padding-left:50px;">
            <button v-if="store.userData.username == review.user.username" @click="deleteReview">삭제</button>
            <button v-if="store.userData.username == review.user.username" @click="useUpdate">수정</button>
          </div>
        </div>
      </div>

      <!-- 수정버튼 누른 후 -->
      <div v-else style="border: 1px solid blue; padding:5px;">
        <form @submit.prevent = "updateReview(moviepk,review.id)">
          <div>
            <label for="title">Title : </label>
            <input type="text" v-model.trim="title" id="title">
          </div>
          <div>
            <label for="content">Content : </label>
            <div>
              <textarea class="update-area" v-model.trim="content" id="content"></textarea>
            </div>
          </div>
          <div>
            <label for="rate">Rate:</label>
            <input type="number" v-model="rate" id="rate" min="0" max="10" required />
          </div>
          <input type="submit">
        </form>
      </div>

      <!-- 댓글 목록 -->
      <!--                      1) 전체 댓글                2) 리뷰               3) 영화 id-->
      <MovieReviewCommentList :comments="review.comments" :reviewpk="review.id" :moviepk="moviepk" />
      <hr>
      <!-- <div style="color:blue">{{ review }}</div> -->
  </div>


</template>

<script setup>
  import MovieReviewCommentList from '@/components/movie/MovieReviewCommentList.vue'
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/account';
  import axios from 'axios'
  import Swal from 'sweetalert2';
  import router from '@/router';

  
  const store = useAccountStore()
  const review = ref(null)
  const isLike = ref(false)
  const isUpdate = ref(false)
  const title = ref(null)
  const content = ref(null)
  const rate = ref(null)
  const props = defineProps({
    review:Object,
    moviepk:Number,
    index:Number,
  })

  review.value = props.review
  


  // 리뷰 수정
  // 1) 수정 form 활성화
  const useUpdate = function () {
    isUpdate.value = true // 수정하기위한 form 열기
    title.value = props.review.title
    content.value = props.review.content
    rate.value = props.review.rate
  }

  // 2) 수정요청보내기 -> 수정 데이터로 변경
  const updateReview = function (moviepk, reviewpk) {
    if (title.value === '' || content.value === '') {
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '제목과 내용에는 1자 이상 작성되어야합니다.',
        confirmButtonText: '확인'
      });
      return 0;
    }
    axios({
      method:'put',
      url:`/movies/${props.moviepk}/reviews/${reviewpk}/`,
      data: {
        title:title.value,
        content:content.value,
        rate:rate.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then(res => {
      isUpdate.value = false // 수정form 닫기
      review.value = res.data[0] // review 데이터 수정하기

    })
    .catch(err => {
      console.log(err)
      Swal.fire({
        icon: 'error',
        title: 'ERROR',
        text: '오류가 발생했습니다.',
        confirmButtonText: '확인'
      });
      return 0;
    })
  }

 
  // 3) 리뷰삭제 emit.ver
  const emit = defineEmits(["deleteReview"])

  function deleteReview () {
    emit("deleteReview",props.review.id)
  }

  // 4) 좋아요 수행

  // 내가 좋아요 눌렀는지 확인하기!!
    isLike.value = computed(() => {
      return review.value.like_users.some(user => user.username === store.userData.username)})
    console.log('isLike',isLike.value)

  const likeBtn = function () {
    if (!store.isLogin) {
      router.push({name:'account'})
      return 0
    }

    axios({
      method:'post',
      url:`/movies/${props.moviepk}/reviews/${review.value.id}/comments/like/`,
      headers:{
        Authorization:`Token ${store.token}`
      },
    })
    .then(res => {
      review.value = res.data

      console.log('좋아요성공')
    })
    .catch(err => {
      console.log('error 발생', err)
    })
  }
  


  // 리뷰 삭제
  // moviepk는 삭제요청시 url에 필요!!
  // const deleteReview = function (moviepk, reviewpk) {
  //   axios({
  //     method:'delete',
  //     url:`/movies/${moviepk}/reviews/${reviewpk}/`,
  //     headers: {
  //       Authorization: `Token ${store.token}`
  //     },
  //   })
  //   .then(res => {
  //     review.value = null
  //   })
  //   .catch(err => console.log(err))
  // }

</script>

<style scoped>
  .review {
    margin: 20px;
    padding: 10px;
    width:700px;
    border: 1px solid rgb(193, 193, 193);
    border-radius: 10px;
    box-shadow: 1px;
    display: flex;
    position: relative
  }
  .profile-box {
    margin-right: 10px;
    width: 80px;
    height: 100px;
    text-align: center;
    font-size: 13px;
  }
  .profile-img {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 70%;
  }

  .update-area {
      width: 400px;
      height:300px;
      resize: none;  /* 크기 제한하기 */
    }

</style>