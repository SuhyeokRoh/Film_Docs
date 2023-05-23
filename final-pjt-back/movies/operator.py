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

    for i in range(1, 6):
        params = {
            "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
            "language" : "ko-KR",
            "page": i,
        }

        r = requests.get(MovieList_URL, params=params)
        data = r.json()['results']

        for x in data:
            try:
                id = x.get('id')
                prms = {
                    "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
                }
                movieTrailerUrl = f"https://api.themoviedb.org/3/movie/{id}/videos"

                res = requests.get(movieTrailerUrl, params=prms)
                key = res.json()['results']
                trailer_key = key[0].get('key')
                trailerUrl = f"https://www.youtube.com/embed/{trailer_key}?autoplay=1&mute=1&loop=1&playlist={trailer_key}"

                if x.get('release_date') == None:
                    release_date = '1999-12-31'
                else:
                    release_date = x.get('release_date')
                
                poster_path = f"https://image.tmdb.org/t/p/w500/{x.get('poster_path')}"
                backdrop_path = f"https://image.tmdb.org/t/p/w300/{x.get('backdrop_path')}"

                movie = Movie(movie_id = id, title = x.get('title'), release_date = release_date, 
                            popularity = x.get('popularity'), vote_count = x.get('vote_count'), 
                            vote_average = x.get('vote_average'), overview = x.get('overview'),
                            poster_path = poster_path, backdrop_path = backdrop_path,
                            trailerUrl = trailerUrl,)
                    
                movie.validate_unique()
                movie.save()
                for g in x.get('genre_ids'):
                    movie.genres.add(g)
            except:
                continue
            


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(saveDb, 'cron', hour=16, minute=0, id="saveDataBase")
    scheduler.add_job(saveDb, 'interval', seconds=30, id="saveDataBase")
    scheduler.start()