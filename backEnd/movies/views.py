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
from .serializers import (
    MovieListSerializer,
    ArticleSerializer,
    MovieSerializer,
    MovieGenreSerializer,
    UserArticleSerializer,
    CommentSerializer,
)
from .models import Movie, Article, Comment


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


# 각 영화별 디테일 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)


# 해당하는 장르 찾기
@api_view(['GET'])
def recommended(request, genre_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieGenreSerializer(movies, many=True)

        comedyGenre = [
            5,
            13,
            68,
            71,
            75,
            90,
            96,
            99,
            100,
            107,
            109,
            114,
            115,
            137,
            153,
            164,
            177,
            194,
            219,
            239,
            243,
            245,
            248,
            252,
            262,
            284,
            287,
            290,
            292,
            306,
            310,
            321,
            338,
            342,
            350,
            378,
            392,
            401,
            433,
            439,
            452,
            455,
            458,
            464,
            480,
            492,
            496,
            508,
            509,
            512,
        ]
        actionGenre = [
            667,
            668,
            670,
            676,
            679,
            681,
            682,
            691,
            698,
            699,
            700,
            707,
            708,
            709,
            710,
            714,
            744,
            752,
            754,
            755,
            787,
            792,
            834,
            839,
            841,
            847,
            849,
            855,
            860,
            861,
            865,
            869,
            871,
            877,
            916,
            924,
            929,
            934,
            941,
            942,
            943,
            944,
            949,
            954,
            955,
            956,
            961,
            984,
            992,
            1051,
        ]
        thrillerGenre = [
            155,
            55,
            59,
            63,
            77,
            78,
            82,
            83,
            93,
            104,
            111,
            116,
            117,
            150,
            161,
            163,
            169,
            170,
            179,
            180,
            182,
            184,
            186,
            187,
            189,
            192,
            213,
            214,
            218,
            223,
            231,
            234,
            241,
            242,
            251,
            267,
            274,
            275,
            277,
            280,
            281,
            288,
            296,
            298,
            299,
            302,
            303,
            319,
            320,
            322,
        ]
        adventureGenre = [
            18,
            22,
            58,
            62,
            74,
            79,
            85,
            87,
            89,
            95,
            97,
            98,
            105,
            106,
            118,
            120,
            121,
            122,
            134,
            146,
            152,
            154,
            157,
            165,
            168,
            172,
            173,
            174,
            175,
            193,
            196,
            199,
            200,
            201,
            217,
            244,
            246,
            253,
            254,
            285,
            329,
            330,
            331,
            332,
            395,
            411,
            421,
            435,
            468,
        ]

        # 공포
        if genre_pk == 27:
            serializer = genre_serach(serializer.data, thrillerGenre)
        # 코미디
        if genre_pk == 35:
            serializer = genre_serach(serializer.data, comedyGenre)
        # 모험
        if genre_pk == 12:
            serializer = genre_serach(serializer.data, adventureGenre)
        # 액션
        if genre_pk == 28:
            serializer = genre_serach(serializer.data, actionGenre)
        return Response(serializer)


def genre_serach(lst, genre):
    fetch_data = []

    for data in lst:
        if data['pk'] in genre:
            tmp = {
                'pk': 0,
                'title': '',
                'overview': '',
                'poster_path': '',
                'release_date': '',
            }
            tmp['pk'] = data['pk']
            tmp['title'] = data['title']
            tmp['overview'] = data['overview']
            tmp['poster_path'] = data['poster_path']
            tmp['release_date'] = data['release_date']
            fetch_data.append(tmp)

    return fetch_data


# user가 저장한 한 목록
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


# 영화 평론 생성
@api_view(['GET', 'POST'])
def article_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def article_list():
        articles = (
            Article.objects.filter(movie_id=movie_pk)
            .annotate(likes_count=Count('like_users'))
            .order_by('-likes_count')
        )
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        return create_article()
    elif request.method == 'GET':
        return article_list()


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def articles_get_or_update_or_delete(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    def update_rating():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                articles = movie.articles.all()
                serializer = ArticleSerializer(articles, many=True)
                return Response(serializer.data)

    def delete_rating():
        if request.user == article.user:
            article.delete()
            articles = movie.articles.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    def get_article():
        serializer = UserArticleSerializer(article)
        return Response(serializer.data)

    def like_article():
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            article.like_users.add(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
    elif request.method == 'GET':
        return get_article()
    elif request.method == 'POST':
        return like_article()


@api_view(['GET', 'POST'])
def get_create_comment(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_comment(request, movie_pk, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)





from django.db.models import Count, Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Genre
from .serializers import MovieSerializer
import random
import datetime

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
            return Response({"message": "좋아하는 영화를 5개 이상 선택해주세요."})
        
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
            return Response({"message": "좋아하는 영화를 5개 이상 선택해주세요."})