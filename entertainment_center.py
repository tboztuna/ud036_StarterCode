import api
import json
import media
import fresh_tomatoes

# Get TheMovieDb instance with an API Key
the_movie_db = api.TheMovieDb("YOUR_API_KEY")

# Get the content of movies
contents = json.loads(the_movie_db.discover())

# Create an empty list for movies
movies = list()

for item in contents["results"]:
    # Get current movie id
    movie_id = item["id"]
    # Get the movie url with another API call
    movie_trailer_url = the_movie_db.get_trailer_url(movie_id)
    # Get the first 20 character of the movie name
    movie_title = item["title"][:20] if len(
        item["title"]) < 20 else item["title"][:20] + "..."
    # Create a movie object with collected data
    movie_object = media.Movie(
        movie_title, item["poster_path"], movie_trailer_url)
    # Add the movie to movies list
    movies.append(movie_object)

fresh_tomatoes.open_movies_page(movies)
