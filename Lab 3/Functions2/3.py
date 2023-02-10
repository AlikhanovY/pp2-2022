from movies import movies

def get_mov( movies, category):
    movies_list = []
    for movie in movies:
        if movie['category'] == category:
            movies_list.append(movie)
    return movies_list

print(get_mov(movies, "Thriller"))
