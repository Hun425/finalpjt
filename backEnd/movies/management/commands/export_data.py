import json
from django.core.management.base import BaseCommand
from django.core import serializers
from movies.models import Actor, Genre, Movie  # 앱 이름이 'movies' 인 것을 반영합니다.

class Command(BaseCommand):
    help = 'Export data to JSON file'

    def handle(self, *args, **kwargs):
        # 데이터 직렬화
        actors = Actor.objects.all()
        genres = Genre.objects.all()
        movies = Movie.objects.all()

        actors_json = serializers.serialize('json', actors )
        genres_json = serializers.serialize('json', genres )
        movies_json = serializers.serialize('json', movies )

        # JSON 파일로 저장 (UTF-8 인코딩 사용)
        with open('actors.json', 'w', encoding='utf-8') as actors_file:
            actors_file.write(actors_json)

        with open('genres.json', 'w', encoding='utf-8') as genres_file:
            genres_file.write(genres_json)

        with open('movies.json', 'w', encoding='utf-8') as movies_file:
            movies_file.write(movies_json)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))