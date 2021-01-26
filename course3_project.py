import sys 
sys.setExecutionLimit(100000) 
import requests_with_caching
import json

def get_movies_from_tastedive(name_of_movie):
    """ It should take one input parameter, a string that is the name of a movie or music artist.
     The function should return the 5 TasteDive results that are associated with that string; """
    desturl = 'https://tastedive.com/api/similar'
    params = {}
    params['q'] = name_of_movie
    params['type'] = "movies" 
    params['limit'] = 5
    res = requests_with_caching.get(desturl, params)
    resp = res.json()
    return resp

#print(get_movies_from_tastedive("Black Panther").text[:200])
#print(json.dumps(get_movies_from_tastedive("Black Panther"), indent=2)) 
def extract_movie_titles(reslist):
    """a function that extracts just the list of movie titles from a dictionary returned by 
    get_movies_from_tastedive."""
    titles = [d['Name'] for d in reslist['Similar']['Results'] if d['Type']=='movie']
    return titles


def get_related_titles(movie_titles):
    """ It takes a list of movie titles as input. It gets five related movies for each 
    from TasteDive, extracts the titles for all of them, and combines them all into a single list."""
    movie_lst = []
    for title in movie_titles:
        mt_pj = get_movies_from_tastedive(title)
        mt_rl = extract_movie_titles(mt_pj)
        for rt in mt_rl:
            if rt not in movie_lst:
                movie_lst.append(rt)
    return movie_lst


def get_movie_data(movie_title):
    """It takes in one parameter which is a string that should represent the title of a movie you want to search.
     The function should return a dictionary with information about that movie."""
    desturl = 'http://www.omdbapi.com/'
    params = {}
    params['t'] = movie_title
    params['r'] = 'json'
    res = requests_with_caching.get(desturl, params)
    return res.json()


def get_movie_rating(OMDB_dic):
    """It takes an OMDB dictionary result for one movie and extracts the Rotten
     Tomatoes rating as an integer. For example, if given the OMDB dictionary for 
     “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, 
     return 0."""
    rotten_tomato_rating = [d['Value'] for d in OMDB_dic['Ratings'] if d['Source'] == 'Rotten Tomatoes']
    if rotten_tomato_rating != []:
        score = int(rotten_tomato_rating[0][:-1])
        return score
    else:
        return 0



def get_sorted_recommendations(movie_titles):
    """It takes a list of movie titles as an input. It returns a sorted list of 
    related movie titles as output, up to five related movies for each input movie
     title. The movies should be sorted in descending order by their Rotten Tomatoes
      rating, as returned by the get_movie_rating function. Break ties in reverse 
      alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’."""
    related_lst = get_related_titles(movie_titles)
    related_dict = {}
    for t in related_lst:
        related_dict[t] = get_movie_rating(get_movie_data(t))
    rating_lst = sorted(related_dict.keys(), key=lambda k: -related_dict[k])
    return rating_lst





