from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
from dj_rest_auth.registration.serializers import RegisterSerializer
User = get_user_model()



class UserSerializer(serializers.ModelSerializer): ## a
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'age', 'profile_pic')



class ReviewMovieSerializer(serializers.ModelSerializer):
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

    class ReviewSerializer(serializers.ModelSerializer):
        class LikeUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk',)

        like_users = LikeUserSerializer(read_only=True, many=True)
        like_user_count = serializers.IntegerField(
            source='like_users.count', read_only=True
        )
        movie = SimpleMovieSerializer(read_only=True)
        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
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

    class LikedReviewSerializer(serializers.ModelSerializer):
        movie_pk = serializers.IntegerField(source='movie.pk', read_only=True)
        backdrop_path = serializers.CharField(source='movie.backdrop_path', read_only=True)

        class Meta:
            model = Review
            fields = ('title', 'content', 'movie_pk', 'backdrop_path')

    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(
        source='followers.count', read_only=True
    )
    following_count = serializers.IntegerField(
        source='followings.count', read_only=True
    )
    reviews = ReviewSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)
    liked_reviews = LikedReviewSerializer(many=True, read_only=True, source='like_reviews')
    reviews_count = serializers.IntegerField(
        source='reviews.count', read_only=True
    )
    like_count = serializers.IntegerField(default=0)

    class Meta:
        model = User
        fields = '__all__'

# 이미지 변경 필드
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')


# 
class LikeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'like_users')

