
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

import requests_with_caching , json
 
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
    

get_movie_rating(get_movie_data("Deadpool 2"))


