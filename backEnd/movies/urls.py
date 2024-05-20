from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('recommended/', views.RecommendedMoviesView.as_view()),
    path('<int:movie_pk>/addlist/', views.add_list),
    path('<int:movie_pk>/articles/', views.article_list_or_create),
    path('<int:movie_pk>/articles/<int:article_pk>/',
         views.articles_get_or_update_or_delete),
    path('<int:movie_pk>/articles/<int:article_pk>/comments/',
         views.get_create_comment),
    path('<int:movie_pk>/articles/<int:article_pk>/comments/<int:comment_pk>/',
         views.delete_comment),
    path('<int:movie_pk>/articles/<int:article_pk>/comments/like/', views.like_article),
    path('api/recommend/',views.recommend_movies)
]
