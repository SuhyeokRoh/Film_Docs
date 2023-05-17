import requests
import json
from django.conf import settings
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


URL = "https://api.themoviedb.org/3/movie/popular"

# API_KEY = settings.TMDB_API_KEY
pk = 1
SaveData = []
for i in range(1, 6):
    params = {
        "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
        "language" : "ko-KR",
        "page": i,
    }

    r = requests.get(URL, params=params)
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
                # 'genres' : x.get('genre_ids'),
                'backdrop_path' : x.get('backdrop_path'),
            }
        }
        SaveData.append(dic)
        pk += 1

file_path = f'./final-pjt-back/movies/fixtures/movie.json'

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(SaveData, file, ensure_ascii=False, indent="\t")