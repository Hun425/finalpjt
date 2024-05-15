from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Article

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'profile_pic')


class ArticleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'pk',
            'title',
        )


# 영화 제목을 줄러오기위한 Serializer
class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path')


class ProfileSerializer(serializers.ModelSerializer):
    class FollowFollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'profile_pic')

    class ArticleSerializer(serializers.ModelSerializer):
        class LikeUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk',)

        like_users = LikeUserSerializer(read_only=True)
        like_user_count = serializers.IntegerField(
            source='like_users.count', read_only=True
        )
        movie = SimpleMovieSerializer(read_only=True)
        user = UserSerializer(read_only=True)

        class Meta:
            model = Article
            fields = '__all__'
            read_only_fields = ('movie',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                'id',
                'title',
                'overview',
                'poster_path',
                'release_date',
                'like_users',
            )

    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(
        source='followers.count', read_only=True
    )
    following_count = serializers.IntegerField(
        source='followings.count', read_only=True
    )
    articles = ArticleSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    articles_count = serializers.IntegerField(
        source='articles.count', read_only=True
    )
    like_count = serializers.IntegerField(default=0)

    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')


class LikeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'user', 'like_users')
