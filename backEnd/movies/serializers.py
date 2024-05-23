from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *


User = get_user_model()



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Movie
        fields = ('pk', 'title', 'vote_average', 'poster_path','release_date','certification','backdrop_path','overview',)


class TopMovieListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Movie
        exclude = (
            'popularity',
            'tagline',
        )


# 리뷰 생성 조회
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:

            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            
            model = User
            fields = ('pk','username')

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username', 'profile_pic')

        user = UserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = (
                'pk',
                'user',
                'review',
                'content',
                'created_at',
                'updated_at',
            )
            read_only_fields = ('review',)

    comments = CommentSerializer(many=True,read_only=True) # 필수 포함 아니니깐 read_only=True




    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')


    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', 'profile_path')


    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            
            model = User
            fields = ('pk','username')

    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

            

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(many=True)



    user = UserSerializer(read_only=True)



    class Meta:
        model = Movie
        exclude = (
            'popularity',
            'tagline',
        )
    



# 유저페이지 리뷰 데이터 전용
class UserReviewSerializer(serializers.ModelSerializer):
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
        model = Review
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


# 댓글 리뷰 전용
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk',)

    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk',
            'user',
            'review',
            'content',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('review',)



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')
    
    backdrop_path = serializers.CharField(source='movie.backdrop_path')

    username = serializers.CharField(source='user.username', read_only=True)
    like_user_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    def get_like_user_count(self,obj):
        return obj.like_users.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()