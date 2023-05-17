from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200)
    # genres = models.ManyToManyField(Genre)
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movielike")
    