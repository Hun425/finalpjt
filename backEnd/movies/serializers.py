from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *


User = get_user_model()



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Movie
        fields = ('pk', 'title', 'vote_average', 'poster_path','release_date')


class TopMovieListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Movie
        exclude = (
            'popularity',
            'tagline',
        )


# 평점
class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:

            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username', 'profile_pic')
        class Meta:
            model = Comment
            fields = (
                'pk',
                'user',
                
                'article',
                'content',
                'created_at',
                'updated_at',
            )
            read_only_fields = ('article',)
    comments = CommentSerializer(many=True)



    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie',)


# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', 'profile_path')




            

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    articles = ArticleSerializer(many=True)



    user = UserSerializer(read_only=True)



    class Meta:
        model = Movie
        exclude = (
            'popularity',
            'tagline',
        )
    


# 날씨 기반 추천 장르 영화
class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'release_date')


class UserArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Article
        fields = (
            'pk',
            'user',
            'movie',
            'title',
            'content',
            'rate',
            'like_users',
            'created_at',
            'updated_at',
            'like_user_count',
        )


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk',)

    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk',
            'user',
            'article',
            'content',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('article',)
