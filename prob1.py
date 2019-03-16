import requests_with_caching , json

def get_movies_from_tastedive(name):
    base_url = 'https://tastedive.com/api/similar'
    data= {'q':name,'limit':5,'type':'movies'}
    jn = json.loads(requests_with_caching.get(base_url, params=data).text)
    print(jn)
    return jn

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")