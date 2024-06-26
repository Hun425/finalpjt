from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
# from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, get_list_or_404
import random
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer,ReviewListSerializer
import datetime
from .serializers import (
    MovieListSerializer,
    ReviewSerializer,
    MovieSerializer,
    UserReviewSerializer,
    CommentSerializer,
)
from .models import Movie, Review, Comment,Genre
from django.utils import timezone
from datetime import timedelta

# DB에 있는 모든 영화 리스트 조회

# 모든 영화
# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all().order_by('-release_date')
#         paginator = Paginator(movies, 20)

#         page = request.GET.get('page', 1)
#         page_movies = paginator.get_page(page)

#         serializer = MovieListSerializer(page_movies, many=True)
#         return Response(serializer.data)
# from django.core.paginator import Paginator  // 이 부분이 원래 있었던 코드




# # 모든 영화

# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
        
#         movies = Movie.objects.all().order_by('-release_date')
#         paginator = MoviePagination()
#         result_page = paginator.paginate_queryset(movies, request)
#         serializer = MovieListSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)





class MoviePagination(PageNumberPagination):
    page_size = 20  # 페이지당 항목 수


def get_age_rating(age):
    if age < 12:
        return ["ALL"]
    elif age < 15:
        return ['12',"ALL"]
    elif age < 18:
        return ['12', '15','ALL']
    else:
        return []  # 나이가 18세 이상인 경우 모든 영화 등급을 볼 수 있도록 빈 리스트 반환

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        user = request.user
        age_ratings = get_age_rating(user.age) if user.is_authenticated else []

        # 현재 상영 중인 영화 필터링 여부 확인
        showing_now = request.GET.get('showing_now','0')=='1'

        # 현재 날짜와 한 달 전 날짜 계산
        today = timezone.now().date()
        one_month_ago = today - timedelta(days=30)

        # 영화 쿼리셋 생성
        if showing_now:
            movies = Movie.objects.filter(release_date__range=[one_month_ago, today])
        else:
            movies = Movie.objects.all()


        movies = movies.exclude(genres__name='다큐멘터리')

        # 나이에 따른 관람등급 필터링
        if age_ratings:
            movies = movies.filter(certification__in=age_ratings)

        # 기본 정렬 기준 적용: 평점 순
        movies = movies.order_by('-vote_average')

        # 페이지네이션 처리
        paginator = MoviePagination()
        result_page = paginator.paginate_queryset(movies, request)
        serializer = MovieListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# 영화별 상세 정보 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)




# 로그인한 유저면 영화에 좋아요 요청 가능
@api_view(['POST'])
def like_movie(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 영화 리뷰 생성
@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def review_list():
        reviews = (
            Review.objects.filter(movie_id=movie_pk)
            .annotate(likes_count=Count('like_users'))
            .order_by('-likes_count')
        )
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create_review():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        return create_review()
    elif request.method == 'GET':
        return review_list()


# HTTP method에 따른 리뷰 조회, 리뷰 생성, 리뷰 수정, 리뷰 삭제 기능
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reviews_get_update_delete(request, movie_pk, review_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_rating():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_rating():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)

    def get_review():
        serializer = UserReviewSerializer(review)
        return Response(serializer.data)

    def like_review():
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            review.like_users.add(user)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
    elif request.method == 'GET':
        return get_review()
    elif request.method == 'POST':
        return like_review()


# 댓글 생성 및 조회
@api_view(['GET', 'POST'])
def get_create_comment(request, movie_pk,review_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user)
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 삭제
@api_view(['DELETE'])
def delete_comment(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
        review = get_object_or_404(Review, pk=review_pk)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN
        )


# 인증된 사용자만 리뷰에 좋아요를 누를 수 있음
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_review(request, movie_pk, review_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)




# 레거시 영화 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended_movies_view(request):
    user = request.user
    current_year = datetime.date.today().year
    birth_year = current_year - user.age
    teenage_years_start = birth_year + 10
    teenage_years_end = teenage_years_start + 9
    age_ratings = get_age_rating(user.age) if user.is_authenticated else []
    liked_movies = Movie.objects.filter(
        like_users=user,

    )
    print(f"Liked movies count: {liked_movies.count()}")  # 디버깅 출력

    if liked_movies.count() < 5:
        return Response({"message": "좋아하는 영화를 5개 이상 선택해주세요."}, status=status.HTTP_403_FORBIDDEN)

    favorite_genre = liked_movies.values('genres').annotate(
        genre_count=Count('genres')
    ).order_by('-genre_count').first()
    print(f"Favorite genre: {favorite_genre}")  # 디버깅 출력

    if not favorite_genre:
        return Response({"message": "가장 많이 선택된 장르를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    genre_id = favorite_genre['genres']
    genre = Genre.objects.get(id=genre_id)
    recommended_movies = Movie.objects.filter(
        genres=genre,
        vote_average__gte=8.0,
        release_date__year__gte=teenage_years_start,
        release_date__year__lte=teenage_years_end
    ).distinct()
            # 나이에 따른 관람등급 필터링
    if age_ratings:
        recommended_movies = recommended_movies.filter(certification__in=age_ratings)
    if user.age <= 19:
        recommended_movies = recommended_movies.filter(adult=False)

    recommended_movies = random.sample(list(recommended_movies), min(10, recommended_movies.count()))
    paginator = MoviePagination()
    page = paginator.paginate_queryset(recommended_movies, request)
    if page is not None:
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(serializer.data)



import logging
logger = logging.getLogger(__name__)
import os
import openai
from dotenv import load_dotenv
from django.http import JsonResponse
from .models import Movie
from .serializers import MovieListSerializer

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 불러오기
openai.api_key = os.getenv('OPENAI_API_KEY')

if openai.api_key is None:
    raise ValueError("No OPENAI_API_KEY found in environment variables.")

def get_movies_from_db():
    return Movie.objects.all()



from .hangul_utils import chosungIncludes


def levenshtein_distance(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def find_similar_movies(movie_name, movies, top_n=10):
    movie_name = movie_name.replace(" ", "")
    similar_movies = []
    for movie in movies:
        movie_title = movie.title.replace(" ", "")
        distance = levenshtein_distance(movie_name.lower(), movie_title.lower())
        similarity = 1 / (1 + distance)
        if movie_name.lower() == movie_title.lower():
            similarity += 2
        # if any(char.isdigit() for char in movie.title):
        #     similarity += 0.1
        if movie_name.lower() in movie_title.lower():
            similarity += 1
        if chosungIncludes(movie_title, movie_name):
            similarity += 1
        if similarity >= 0.7:
            similar_movies.append((similarity, movie))
    similar_movies.sort(key=lambda x: x[0], reverse=True)
    return [(movie, similarity) for similarity, movie in similar_movies[:top_n]]


def gpt_movies(request):
    movie_name = request.GET.get('movie_name', '')
    movies = Movie.objects.all()
    if movie_name:
        similar_movies = find_similar_movies(movie_name, movies)
        serialized_movies = []
        for movie, similarity in similar_movies:
            serialized_movie = MovieListSerializer(movie, context={'request': request}).data
            serialized_movie['similarity'] = similarity
            serialized_movies.append(serialized_movie)
        return JsonResponse({'similar_movies': serialized_movies})
    return JsonResponse({'similar_movies': []})





## 유사한 유저를 기반으로 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from .models import UserRatings
def user_based_recommend(user_id):
    # 사용자-아이템 행렬 생성
    user_movie_ratings = pd.pivot_table(UserRatings.objects.all().values('user_id', 'movie_id', 'rating'), 
                                        values='rating', 
                                        index='user_id', 
                                        columns='movie_id')
    user_movie_ratings = user_movie_ratings.fillna(0)
    
    # 코사인 유사도 계산
    user_similarity = cosine_similarity(user_movie_ratings)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_ratings.index, columns=user_movie_ratings.index)
    
    # 현재 사용자와 비슷한 사용자들 찾기
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:6]
    
    # 비슷한 사용자들이 좋아하는 영화 추천
    similar_users_ratings = user_movie_ratings.loc[similar_users]
    recommended_movies = similar_users_ratings.mean().sort_values(ascending=False).index
    
    return Movie.objects.filter(id__in=recommended_movies[:10])

@api_view(['GET'])
def all_review(request):
    reviews = Review.objects.all()

    if request.user.is_authenticated:
        user_age = request.user.age
        age_ratings = get_age_rating(user_age)

        # 필터링된 리뷰 리스트
        filtered_reviews = []

        # 각 리뷰에 대해 영화의 나이 제한을 확인하고 필터링
        for review in reviews:
            movie = review.movie  # 리뷰에 연결된 영화 객체를 가져옴
            if movie.certification in age_ratings:
                filtered_reviews.append(review)

        reviews = filtered_reviews

    # 시리얼라이즈된 리뷰 반환
    serializers = ReviewListSerializer(reviews, many=True)
    return Response(serializers.data)