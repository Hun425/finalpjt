import os
import requests
from dotenv import load_dotenv
from .models import Movie, Genre, Actor

load_dotenv()

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3'
LANGUAGE = 'ko-KR'  # 언어 설정

def get_or_create_genre(genre_id, genre_name):
    genre, created = Genre.objects.get_or_create(id=genre_id, defaults={'name': genre_name})
    return genre

def get_or_create_actor(actor_name):
    actor, created = Actor.objects.get_or_create(name=actor_name)
    return actor

def fetch_movie_data():
    url = f"{TMDB_API_URL}/movie/popular?api_key={TMDB_API_KEY}&language={LANGUAGE}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for movie_data in data['results']:
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                overview=movie_data.get('overview', ''),
                popularity=movie_data.get('popularity', 0),
                poster_path=movie_data.get('poster_path', ''),
                release_date=movie_data.get('release_date', None),
                runtime=movie_data.get('runtime', 0),
                tagline=movie_data.get('tagline', ''),
                vote_average=movie_data.get('vote_average', 0),
                vote_count=movie_data.get('vote_count', 0),
            )
            if created:
                # Fetch genres for the movie
                genre_ids = movie_data.get('genre_ids', [])
                for genre_id in genre_ids:
                    genre_data_url = f"{TMDB_API_URL}/genre/movie/list?api_key={TMDB_API_KEY}&language={LANGUAGE}"
                    genre_response = requests.get(genre_data_url)
                    if genre_response.status_code == 200:
                        genre_data = genre_response.json()
                        genres = {genre['id']: genre['name'] for genre in genre_data['genres']}
                        genre = get_or_create_genre(genre_id, genres[genre_id])
                        movie.genres.add(genre)

                # Fetch actors for the movie
                movie_id = movie_data['id']
                credits_url = f"{TMDB_API_URL}/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language={LANGUAGE}"
                credits_response = requests.get(credits_url)
                if credits_response.status_code == 200:
                    credits_data = credits_response.json()
                    for actor_data in credits_data.get('cast', [])[:10]:  # Limiting to top 10 actors
                        actor = get_or_create_actor(actor_data['name'])
                        movie.actors.add(actor)

                print(f"Created movie: {movie.title}")
    else:
        print(f"Failed to fetch data: {response.status_code}")
