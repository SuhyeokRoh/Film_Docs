from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import register_events, DjangoJobStore
from django.conf import settings
import requests
import sys
import io
from .models import Movie, Genre


def saveDb():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


    MovieList_URL = "https://api.themoviedb.org/3/discover/movie"
    Genre_URL = "https://api.themoviedb.org/3/genre/movie/list"

    # Genre json으로 저장하기
    para = {
        "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
    }

    res = requests.get(Genre_URL, params=para)

    d = res.json()["genres"]

    for y in d:
        genre = Genre(id = y['id'], name = y['name'])
        genre.save()
    # print(genreData)

    # MovieList json으로 저장하기

    for i in range(1, 2):
        params = {
            "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
            "language" : "ko-KR",
            "page": i,
        }

        r = requests.get(MovieList_URL, params=params)
        data = r.json()['results']

        for x in data:
            movie = Movie(title = x['title'], release_date = x['release_date'], 
                          popularity = x['popularity'], vote_count = x['vote_count'], 
                          vote_average = x['vote_average'], overview = x['overview'],
                          poster_path = x['poster_path'], 
                          backdrop_path = x['backdrop_path'])
            movie.save()
            for g in x['genre_ids']:
                movie.genres.add(g)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(saveDb, 'cron', hour=15, mivute=25, id="saveDataBase")
    scheduler.start()