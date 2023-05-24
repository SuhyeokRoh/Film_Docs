from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('recommend/', views.movie_recommend, name="movie_recommend"),
    path('main/', views.movie_release_list, name="movie_release_list"),
    path('choice/', views.movie_choice, name="movie_choice"),
    path('search/', views.movie_search, name="movie_search"),
    
    path('worldcup/', views.movie_worldcup, name="movie_worldcup"),
    path('worldcup/<int:worldcup_pk>/', views.worldcup_detail, name='worldcup_detail'),
    path('worldcup/custom/', views.create_worldcup, name='create_worldcup'),
    
    
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/like/', views.movie_like, name="movie_like"),
    path('<int:movie_pk>/dislike/', views.movie_dislike, name="movie_dislike"),
    
    path('<int:movie_pk>/reviews/', views.reviewList, name="reviewList"),
    path('<int:movie_pk>/reviews/create/', views.review_create, name="review_create"),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail, name="review_detail"),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.review_update, name="review_update"),
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.review_like, name="review_like"),
    path('<int:movie_pk>/reviews/<int:review_pk>/dislike/', views.review_dislike, name="review_dislike"),
    
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/', views.commentList, name="commentList"),
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/create/', views.comment_create, name="comment_create"),
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_detail, name="comment_detail"),
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/<int:comment_pk>/update/', views.comment_update, name="comment_update"),
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/<int:comment_pk>/like/', views.comment_like, name="comment_like"),
    path('<int:movie_pk>/reviews/<int:review_pk>/comment/<int:comment_pk>/dislike/', views.comment_dislike, name="comment_dislike"),
    
    path('<int:actor_pk>/actor/', views.actorDetail, name="actorDetail"),
]