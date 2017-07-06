import api
import json
import media
import fresh_tomatoes

the_movie_db = api.TheMovieDb("55ed321f0e57e3983da866087cb460f6")
contents = json.loads(the_movie_db.discover())

movies = list()
for item in contents["results"]:
    movie_id = item["id"]
    movie_trailer_url = the_movie_db.get_trailer_url(movie_id)
    movie_title = item["title"][:20] if len(
        item["title"]) < 20 else item["title"][:20] + "..."
    movie_object = media.Movie(
        movie_title, item["poster_path"], movie_trailer_url)
    movies.append(movie_object)

fresh_tomatoes.open_movies_page(movies)
