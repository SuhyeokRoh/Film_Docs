import requests
import json
from django.conf import settings
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


URL = "https://api.themoviedb.org/3/movie/popular"

# API_KEY = settings.TMDB_API_KEY

for i in range(1, 6):
    params = {
        "api_key" : 'e66fa81c4a87396b24dd94a15cc7a8b1',
        "language" : "ko-KR",
        "page": i,
    }

    r = requests.get(URL, params=params)
    data = r.json()['results']
    # print(data)

    file_path = f'./final-pjt-back/movies/fixtures/movie_{i}.json'

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent="\t")