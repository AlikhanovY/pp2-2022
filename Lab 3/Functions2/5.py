from movies import movies

def get_avg_rat(movies, cat):
    sum = 0
    n_movies = 0
    for movie in movies:
        if movie['category'] == cat:
            sum += movie['imdb']
            n_movies += 1
    return sum / n_movies

print(get_avg_rat(movies, 'Crime'))