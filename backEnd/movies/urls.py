from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('recommended/', views.RecommendedMoviesView.as_view()),
    path('<int:movie_pk>/addlist/', views.add_list),
    path('<int:movie_pk>/reviews/', views.review_list_or_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/',
         views.reviews_get_update_delete),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/',
         views.get_create_comment),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>',
         views.delete_comment),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/like/', views.like_review)
]
