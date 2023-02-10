from movies import movies
for movie in movies:
    if movie['imdb'] > 5.5:
        print(movie['name'])