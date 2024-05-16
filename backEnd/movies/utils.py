import os
import requests
from datetime import datetime
from django.conf import settings
from .models import Movie, Genre, Actor
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3'
LANGUAGE = 'ko-KR'

def get_or_create_genre(genre_id, genre_name):
    genre, created = Genre.objects.get_or_create(id=genre_id, defaults={'name': genre_name})
    return genre

def get_or_create_actor(actor_id, actor_name, profile_path):
    actor, created = Actor.objects.get_or_create(
        id=actor_id,
        defaults={
            'name': actor_name,
            'profile_path': profile_path
        }
    )
    return actor

def fetch_movie_details(movie_id):
    url = f"{TMDB_API_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language={LANGUAGE}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_movie_data(num_movies=10000):
    movies_per_page = 20  # TMDB API의 한 페이지당 기본 결과 수
    total_pages = (num_movies - 1) // movies_per_page + 1  # 필요한 페이지 수 계산

    movie_count = 0
    for page in range(1, total_pages + 1):
        url = f"{TMDB_API_URL}/movie/popular?api_key={TMDB_API_KEY}&language={LANGUAGE}&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie_data in data['results']:
                if movie_count >= num_movies:
                    return  # 요청한 영화 수를 충족하면 함수 종료
                
                if 'overview' not in movie_data or not movie_data['overview']:
                    print(f"Skipping movie without overview: {movie_data.get('title', 'Unknown')}")
                    continue
                
                detailed_info = fetch_movie_details(movie_data['id'])
                if detailed_info:
                    movie, created = Movie.objects.get_or_create(
                        id=movie_data['id'],
                        defaults={
                            'title': movie_data['title'],
                            'overview': movie_data['overview'],
                            'popularity': movie_data['popularity'],
                            'poster_path': movie_data.get('poster_path'),
                            'release_date': movie_data.get('release_date'),
                            'runtime': detailed_info.get('runtime'),
                            'tagline': detailed_info.get('tagline', ''),
                            'vote_average': movie_data.get('vote_average', 0),
                            'vote_count': movie_data.get('vote_count', 0),
                        }
                    )
                    for genre_data in detailed_info['genres']:
                        genre = get_or_create_genre(genre_data['id'], genre_data['name'])
                        movie.genres.add(genre)

                    credits_url = f"{TMDB_API_URL}/movie/{movie_data['id']}/credits?api_key={TMDB_API_KEY}&language={LANGUAGE}"
                    credits_response = requests.get(credits_url)
                    if credits_response.status_code == 200:
                        credits_data = credits_response.json()
                        for actor_data in credits_data['cast'][:10]:  # 상위 10명의 배우만 추가
                            actor = get_or_create_actor(actor_data['id'], actor_data['name'], actor_data.get('profile_path'))
                            movie.actors.add(actor)

                    print(f"Created or updated movie: {movie.title}")
                    movie_count += 1
        else:
            print(f"Failed to fetch data: {response.status_code}")
