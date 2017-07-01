import webbrowser

class Movie():
    def __init__(self, title, poster_url, youtube_trailer_url):
        self.title = title
        self.poster_url = poster_url
        self.youtube_trailer_url = youtube_trailer_url

    def get_title(self):
        return self.title

    def get_poster_url(self):
        return self.title

    def get_youtube_trailer_url(self):
        return self.youtube_trailer_url

    def show_title(self):
        print self.get_title()

    def show_poster(self):
        webbrowser.open(self.get_poster_url())

    def show_trailer(self):
        webbrowser.open(self.get_youtube_trailer_url())
