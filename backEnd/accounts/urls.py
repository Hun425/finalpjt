from django.urls import path
from . import views


app_name = 'profile'
urlpatterns = [
    path('<int:user_pk>/', views.profile),
    path('<int:user_pk>/like/', views.like_num_of_review),
    # path('<int:user_pk>/follow/', views.follow),
    path('<int:movie_pk>/review/', views.review_movie),
    path('<int:user_pk>/update/', views.update_profile),
    path('<int:user_pk>/delete/',views.delete_profile),
]
