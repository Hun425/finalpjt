<template>
    <div class="profile-pic-container mb-4 text-center">
      <img src="" alt="No Image" />
    </div>
    <div>
      <button @click="changeProfilePic">프로필 사진 변경</button>
    </div>
</template>

<script setup>
    import { ref } from 'vue'

    const props = defineProps({
        userpk:Number,
        userPic:String,
    })
    const userProfilePic = ref(null)
    userProfilePic.value = props.userPic

    const selectedFile = ref(null)


    const changeProfilePic = () => {
        const input = document.createElement('input')
        input.type = 'file'
        input.accept = 'image/*'
        input.onchange = (e) => {
            selectedFile.value = e.target.files[0]
            uploadProfilePic()
        }
        input.click()
        }

    const uploadProfilePic = () => {
        const formData = new FormData()
        formData.append('profile_pic', selectedFile.value)

        profilePicEdit(props.user.id, formData)
            .then((response) => {
            if (response && response.data) {
                props.user.profile_pic = response.data.profile_pic
            } else {
                props.user.profile_pic = URL.createObjectURL(selectedFile.value)
            }
            })
            .catch((error) => {
            console.error(error)
            })
        }
        const profilePicEdit = (userPk, payload) => {
            const token = window.localStorage.getItem("token");

            return axios
                .put(`${API_URL}/profile/${userPk}/update/`, payload, {
                headers: {
                    "Content-Type": "multipart/form-data",
                    Authorization: `Token ${token}`,
                },
                })
                .then((response) => {
                return response;
                })
                .catch((error) => {
                console.error("API 요청 중 에러가 발생했습니다:", error);
                throw error;
                });
            };



</script>

<style scoped>

</style>