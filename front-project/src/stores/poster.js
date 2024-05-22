import {defineStore} from 'pinia'
import {ref} from 'vue'



export const usePosterStore = defineStore('poster', () => {

  const poster = ref(
  {
    '범죄도시4' : 'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240425_256%2F17140073560223JK9r_JPEG%2Fmovie_image.jpg',

  '그녀가 죽었다':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240516_147%2F1715830347927Txj0U_JPEG%2Fmovie_image.jpg',

  '혹성탈출: 새로운 시대':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240508_299%2F1715149331590vuPj9_JPEG%2Fmovie_image.jpg',

  '극장판 하이큐!! 쓰레기장의 결전':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240419_201%2F1713491848710ihckT_JPEG%2Fmovie_image.jpg',

  '가필드 더 무비':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240517_153%2F1715928374513w4vVq_JPEG%2Fmovie_image.jpg',

  '이프: 상상의 친구':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240516_149%2F1715850328824UHxLb_JPEG%2Fmovie_image.jpg',

  '악마와의 토크쇼':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240509_31%2F1715235948706HoyK3_JPEG%2Fmovie_image.jpg',


  '퓨리오사: 매드맥스 사가':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240510_58%2F1715314949409XMru0_JPEG%2Fmovie_image.jpg',

  '남은 인생 10년':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240314_148%2F1710404569583YXlii_JPEG%2Fmovie_image.jpg',

  '쇼생크 탈출':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240404_36%2F1712216009593oVdA5_JPEG%2Fmovie_image.jpg',

  '쿵푸팬더4':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240311_85%2F1710136183535z3QfC_JPEG%2Fmovie_image.jpg',

  '챌린저스':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240404_112%2F1712222321184IqPNE_JPEG%2Fmovie_image.jpg',


  '애비게일':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240516_6%2F1715828491642v7chk_JPEG%2Fmovie_image.jpg',

  '청춘 18X2 너에게로 이어지는 길':
  'https://search.pstatic.net/common?quality=75&direct=true&src=https%3A%2F%2Fmovie-phinf.pstatic.net%2F20240429_269%2F1714358475869Os9Yr_JPEG%2Fmovie_image.jpg'
})
  return { poster }
}, {persist:true})
