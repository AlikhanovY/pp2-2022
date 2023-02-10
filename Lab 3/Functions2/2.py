from movies import movies

def get_g_mov(movies):
    g_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            g_movies.append(movie["name"])
    return g_movies

print(get_g_mov(movies))