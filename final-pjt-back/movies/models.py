from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Production(models.Model):
    name = models.CharField(max_length=100)
    logo_path = models.TextField(null=True)
    original_country = models.CharField(max_length=100, null=True)
    
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True)
    birthday = models.DateTimeField()
    deathday = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    place_of_birth = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    profile_path = models.TextField(null=True)


class Movie(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    backdrop_path_original = models.TextField(null=True)
    poster_path_original = models.TextField(max_length=200)
    trailerUrl = models.TextField()
    budget = models.IntegerField(null=True)
    revenue = models.IntegerField(null=True)
    runtime = models.IntegerField(null=True)
    homepage = models.TextField(null=True)
    genres = models.ManyToManyField(Genre)
    production_companies = models.ManyToManyField(Production, related_name="movie_companies")
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movielike")
    movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movieDislike")
    actor = models.ManyToManyField(Actor, related_name="movie_actor")


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
