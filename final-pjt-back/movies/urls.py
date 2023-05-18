from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/reviews/', views.review_create, name="review_create"),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail, name="review_detail"),
]