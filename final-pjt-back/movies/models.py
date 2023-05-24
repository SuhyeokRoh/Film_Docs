from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    backdrop_path_300 = models.CharField(max_length=200, null=True)
    backdrop_path_original = models.CharField(max_length=200, null=True)
    poster_path_500 = models.CharField(max_length=200)
    poster_path_original = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    trailerUrl = models.TextField()
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movielike")
    movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movieDislike")


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_reviews')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comment_movie")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comment_review")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments")
    dislike_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dislike_comments")