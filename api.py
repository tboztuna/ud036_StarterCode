import urllib

class TheMovieDb():

    __discover_url = "https://api.themoviedb.org/3/discover/movie"

    def __init__(self, api_key):
        self.__api_key = api_key

    def set_api_key(self, api_key):
        self.__api_key = api_key

    def get_api_key(self):
        return self.__api_key

    def build_discover_url(self):
        url = self.__discover_url + "?api_key=" + self.get_api_key()
        return url

    def get_discover_url(self):
        return self.build_discover_url()

    def discover(self):
        contents = urllib.urlopen(self.get_discover_url())
        return contents.read()