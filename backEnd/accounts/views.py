from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import (ReviewMovieSerializer,
                          ProfileSerializer, ProfileUpdateSerializer)
from movies.models import Movie

User = get_user_model()


# 유저 상세정보 조회 로직
@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    reviews = ProfileSerializer(user)

    return Response(reviews.data)


# 내가 글쓴 리뷰들 중에 총 좋아요 수 조회
@api_view(['GET'])
def like_num_of_review(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    reviews = ProfileSerializer(user)
    like_count = 0
    for data in reviews.data['reviews']:
        like_count += data['like_user_count']

    print(like_count)
    return Response(like_count)


# 프로필 페이지에 보여줄 무비 데이터
@api_view(['GET'])
def review_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewMovieSerializer(movie)
    return Response(serializer.data)

# 팔로우 기능 아직 사용안함
# @api_view(['POST'])
# def follow(request, user_pk):
#     profile_user = get_object_or_404(get_user_model(), pk=user_pk)
#     me = request.user
#     if me != profile_user:
#         if me.followings.filter(pk=profile_user.pk).exists():
#             me.followings.remove(profile_user)
#         else:
#             me.followings.add(profile_user)

#     serializer = ProfileSerializer(profile_user)
#     return Response(serializer.data)


# 사용자 정보(이미지) 수정
@api_view(['POST', 'PUT'])
def update_profile(request, user_pk):
    profile_user = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if request.method == 'PUT':
        if me == profile_user:
            serializer = ProfileUpdateSerializer(
                instance=request.user, data=request.data
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'POST':
        if me == profile_user:
            serializer = ProfileUpdateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 회원 탈퇴 로직
@api_view(['DELETE'])
def delete_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    me = request.user
    if me == user:
        user.delete()
        return Response({"message": "회원 탈퇴 완료"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "올바른 접근이 아닙니다"}, status=status.HTTP_403_FORBIDDEN)
    


