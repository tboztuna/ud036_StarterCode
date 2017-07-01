import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_title(self):
        """Shows title of the movie.

        Returns:
            str: The movie's title.
        """
        print self.title

    def show_poster(self):
        """Opens the poster of the film in a web browser."""
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        """Opens the trailer of the film in a web browser."""
        webbrowser.open(self.trailer_youtube_url)
