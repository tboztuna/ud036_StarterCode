import json
import urllib

class TheMovieDb():
    """This class provides a way to connect to the movie db api
    to get related information about the films
    """

    __discover_url = "https://api.themoviedb.org/3/discover/movie"
    __movie_details_url = "https://api.themoviedb.org/3/movie/"

    def __init__(self, api_key):
        self.__api_key = api_key

    def set_api_key(self, api_key):
        """Sets api key
            Parameters:
                api_key
        """
        self.__api_key = api_key

    def get_api_key(self):
        """Returns api key.
            Returns:
            str: The API Key.
        """
        return self.__api_key

    def build_discover_url(self):
        """Builds and returns discover url.
            Returns:
            str: The discover url.
        """
        url = self.__discover_url + "?api_key=" + self.get_api_key() + "&sort_by=popularity.desc"
        return url

    def build_movie_url(self, movie_id):
        """Builds and returns the movie url.
            Parameters:
                movie_id
            Returns:
            str: The movie url.
        """
        url = self.__movie_details_url + str(movie_id) + "/videos?api_key=" + self.get_api_key()
        return url

    def get_discover_url(self):
        """Returns builded discover url.
            Returns:
            str: The discover url.
        """
        return self.build_discover_url()

    def get_movie_url(self, movie_id):
        """Returns builded movie url.
            Parameters:
                movie_id
            Returns:
            str: The movie url.
        """
        return self.build_movie_url(movie_id)

    def discover(self):
        """Gets randomly generated film data.
            Returns:
            str: json data of movies.
        """
        contents = urllib.urlopen(self.get_discover_url())
        return contents.read()

    def get_movie_details_url(self):
        """Returns movie_details url.
            Returns:
            str: The movie_details url.
        """
        return self.__movie_details_url

    def get_trailer_url(self, movie_id):
        """Returns the trailer url of the movie.
            Parameters:
                movie_id
            Returns:
            str: The trailer url.
        """
        contents = urllib.urlopen(self.get_movie_url(movie_id))
        data = json.loads(contents.read())
        return "https://www.youtube.com/watch?v=" + data["results"][0]["key"]
