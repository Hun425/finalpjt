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
from .serializers import MovieSerializer
import datetime
from .serializers import (
    MovieListSerializer,
    ReviewSerializer,
    MovieSerializer,
    UserReviewSerializer,
    CommentSerializer,
)
from .models import Movie, Review, Comment,Genre


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
from rest_framework.pagination import PageNumberPagination

class MoviePagination(PageNumberPagination):
    page_size = 20


# 모든 영화

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-release_date')
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




# user가 좋아요 누른 영화 목록 조회
@api_view(['POST'])
def add_list(request, movie_pk):
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
def review_list_or_create(request, movie_pk):
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





# 영화 레거시 로직 추천 방법
# 
class RecommendedMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        current_year = datetime.date.today().year
        birth_year = current_year - user.age
        teenage_years_start = birth_year + 10
        teenage_years_end = teenage_years_start + 9

        # 10대에 나온 영화 중 사용자가 좋아요를 누른 영화 쿼리
        liked_movies = Movie.objects.filter(
            like_users=user,
            release_date__year__gte=teenage_years_start,
            release_date__year__lte=teenage_years_end
        )

        # 사용자 나이가 10살 이하인 경우 최근 1년 동안 개봉한 영화 추천
        if user.age <= 10:
            one_year_ago = datetime.date.today() - datetime.timedelta(days=365)
            recent_movies = Movie.objects.filter(
                release_date__gte=one_year_ago,
                release_date__lte=datetime.date.today()
            ).order_by('-release_date')

            # 랜덤으로 10개 선택
            recent_movies = random.sample(list(recent_movies), min(10, recent_movies.count()))
            
            serializer = MovieSerializer(recent_movies, many=True)
            return Response(serializer.data)
        if liked_movies.count() < 5:
            return Response({"message": "좋아하는 영화를 5개 이상 선택해주세요."},status=status.HTTP_403_FORBIDDEN)
        
        # 사용자가 좋아요를 누른 영화 중 가장 많이 선택된 장르
        favorite_genre = liked_movies.values('genres').annotate(
            genre_count=Count('genres')
        ).order_by('-genre_count').first()

        if favorite_genre:
            genre_id = favorite_genre['genres']
            genre = Genre.objects.get(id=genre_id)
            recommended_movies = Movie.objects.filter(
                genres=genre,
                vote_average__gte=8.0
            ).distinct()
            if user.age <= 19:
                recommended_movies = recommended_movies.filter(adult=False)
            
            # 랜덤으로 20개 선택
                recommended_movies = random.sample(list(recommended_movies), min(20, recommended_movies.count()))

                serializer = MovieSerializer(recommended_movies, many=True)
                return Response(serializer.data)
            # 랜덤으로 20개 선택
            recommended_movies = random.sample(list(recommended_movies), min(10, recommended_movies.count()))

            serializer = MovieSerializer(recommended_movies, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "좋아하는 영화를 5개 이상 선택해주세요."},status=status.HTTP_403_FORBIDDEN)
