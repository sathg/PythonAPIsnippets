
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

import requests_with_caching , json

def get_movies_from_tastedive(name):
    base_url = 'https://tastedive.com/api/similar'
    data= {'q':name,'limit':5,'type':'movies'}
    jn = json.loads(requests_with_caching.get(base_url, params=data).text)
    return jn


# def get_movies_from_tastedive(title):
#     endpoint = 'https://tastedive.com/api/similar'
#     param = {}
#     param['q'] = title
#     param['limit'] = 5
#     param['type'] = 'movies'

#     this_page_cache = requests_with_caching.get(endpoint, params=param)
#     return json.loads(this_page_cache.text)


def extract_movie_titles(jn):
    return [movie['Name'] for movie in jn['Similar']['Results']]

def get_related_titles(ls):
    outls = []
    for i in ls:
        outls.extend(extract_movie_titles(get_movies_from_tastedive(i)))
    return list(set(outls))

 
def get_movie_data(movie):
    param = {"t" : movie, 'r' : 'json'}
    url = "http://www.omdbapi.com/"
    result = requests_with_caching.get( url, params =param)
    resultText = (result.text)
    jsonText = json.loads(resultText);
    return jsonText 

def get_movie_rating(jsonText):
    for mov in jsonText["Ratings"]:
        if mov['Source'] == 'Rotten Tomatoes':
            return int(mov['Value'].replace("%",""))
    return 0


def get_sorted_recommendations(lsn):
    outRes = []
    for j in get_related_titles(lsn):
        outRes.append([get_movie_rating(get_movie_data(j)), j])
    return [ y[1] for y in sorted(outRes, key=lambda x: (x[0], x[1]))[::-1]]


get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
