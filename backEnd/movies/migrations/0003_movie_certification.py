# Generated by Django 4.2.8 on 2024-05-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_adult'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='certification',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
