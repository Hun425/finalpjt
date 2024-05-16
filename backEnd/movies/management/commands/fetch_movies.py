from django.core.management.base import BaseCommand
from movies.utils import fetch_movie_data

class Command(BaseCommand):
    help = 'Fetches movies from TMDB API and saves them to the database'

    def handle(self, *args, **kwargs):
        fetch_movie_data()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved movies'))
