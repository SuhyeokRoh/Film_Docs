import requests
import json
from django.conf import settings
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


MovieList_URL = "https://api.themoviedb.org/3/movie/popular"
Genre_URL = "https://api.themoviedb.org/3/genre/movie/list"


# Genre json으로 저장하기
genreData = []
para = {
    "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
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
    
file_p = f'./final-pjt-back/movies/fixtures/genres.json'

with open(file_p, 'w', encoding='utf-8') as file:
    json.dump(genreData, file, ensure_ascii=False, indent="\t")


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

file_path = f'./final-pjt-back/movies/fixtures/movie.json'

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(SaveData, file, ensure_ascii=False, indent="\t")