from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
    
    username = models.CharField(max_length=150, unique=True)  #변경
    email = models.EmailField(unique=True)  # 추가
    age = models.PositiveIntegerField(default=18)  # 추가
    profile_pic = ProcessedImageField(
        blank=True, 
        upload_to='profile/images',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90},
    )
