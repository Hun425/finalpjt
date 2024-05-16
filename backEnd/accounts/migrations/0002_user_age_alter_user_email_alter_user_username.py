# Generated by Django 4.2.8 on 2024-05-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
