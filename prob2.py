
import requests_with_caching , json

def get_movies_from_tastedive(name):
    base_url = 'https://tastedive.com/api/similar'
    data= {'q':name,'limit':5,'type':'movies'}
    jn = json.loads(requests_with_caching.get(base_url, params=data).text)
    return jn

def extract_movie_titles(jn):
    return [movie['Name'] for movie in jn['Similar']['Results']]

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

