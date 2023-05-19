from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from django.conf import settings
import requests
import sys
import io


def saveDb():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


    MovieList_URL = "https://api.themoviedb.org/3/movie/popular"
    Genre_URL = "https://api.themoviedb.org/3/genre/movie/list"


    # Genre json으로 저장하기
    genreData = []
    para = {
        "api_key" : settings.SECRET_KEY,
    }

    res = requests.get(Genre_URL, params=para)
    d = res.json()["genres"]

    pk_g = 1
    for y in d:
        dic = {
            "model": "movies.genre",
            "pk" : pk_g,
            'fields' : y,
        }
        genreData.append(dic)

    genreData.save()

    # MovieList json으로 저장하기
    pk = 1
    SaveData = []
    for i in range(1, 6):
        params = {
            "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
            "language" : "ko-KR",
            "page": i,
        }

        r = requests.get(MovieList_URL, params=params)
        data = r.json()['results']
        # print(data)
        for x in data:
            dic = {
                'model': 'movies.movie',
                'pk': pk,
                'fields': {
                    'title': x.get('title'),
                    'release_date' : x.get('release_date'),
                    'popularity' : x.get('popularity'),
                    'vote_count' : x.get('vote_count'),
                    'vote_average' : x.get('vote_average'),
                    'overview' : x.get('overview'),
                    'poster_path' : x.get('poster_path'),
                    'genres' : x.get('genre_ids'),
                    'backdrop_path' : x.get('backdrop_path'),
                }
            }
            SaveData.append(dic)
            pk += 1
    
    SaveData.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    @scheduler.scheduled_job('cron', hour=12,minute=6, name = 'saveDb')
    def auto_check():
        saveDb()
    scheduler.start()