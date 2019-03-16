import requests_with_caching , json
 
def get_movie_data(movie):
    param = {"t" : movie, 'r' : 'json'}
    url = "http://www.omdbapi.com/"
    result = requests_with_caching.get( url, params =param)
    resultText = (result.text)
    jsonText = json.loads(resultText);
    print(jsonText)
    return jsonText 

    
get_movie_data("Venom")
get_movie_data("Baby Mama")
get_movie_data("Black Panther")