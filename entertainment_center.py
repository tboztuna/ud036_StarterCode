import api
import json
import media
import fresh_tomatoes

the_movie_db = api.TheMovieDb("55ed321f0e57e3983da866087cb460f6")
contents = json.loads(the_movie_db.discover())
print contents
movies = list()

for item in contents["results"]:
    movie_instance = media.Movie(item["title"], item["poster_path"], "")
    movies.append(movie_instance)

fresh_tomatoes.open_movies_page(movies)
