from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/like/', views.movie_like, name="movie_like"),
    path('<int:movie_pk>/reviews/', views.reviewList, name="reviewList"),
    path('<int:movie_pk>/reviews/create/', views.review_create, name="review_create"),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail, name="review_detail"),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.review_update, name="review_update"),
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.review_like, name="review_like"),
    path('<int:movie_pk>/reviews/<int:review_pk>/dislike/', views.review_dislike, name="review_dislike"),
]