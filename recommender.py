import requests
from config import TMDB_KEY

def similar(mid):
 url=f'https://api.themoviedb.org/3/movie/{mid}/recommendations?api_key={TMDB_KEY}'
 data=requests.get(url).json()
 return data.get('results',[])[:5]
