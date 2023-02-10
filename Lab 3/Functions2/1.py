from movies import movies


def is_mov(movies ,movie_name):
    curr_movie = dict(())
    for movie in movies:
        if movie["name"] == movie_name:
            curr_movie = movie
    return curr_movie["imdb"] > 5.5


print(is_mov(movies, "Dark Knight"))