from movies import movies

def get_avg(movies):
    sum = 0
    n_movies = len(movies)
    for movie in movies:
        sum += movie["imdb"]
    return sum/n_movies

print(get_avg(movies))