
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])



import requests_with_caching , json

def get_movies_from_tastedive(name):
    base_url = 'https://tastedive.com/api/similar'
    data= {'q':name,'limit':5,'type':'movies'}
    jn = json.loads(requests_with_caching.get(base_url, params=data).text)
    return jn

def extract_movie_titles(jn):
    return [movie['Name'] for movie in jn['Similar']['Results']]

def get_related_titles(ls):
    outls = []
    for i in ls:
        outls.extend(extract_movie_titles(get_movies_from_tastedive(i)))
    return list(set(outls))

get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])