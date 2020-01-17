import webbrowser

class Video():
    def __init__(self, title, duration ):
        self.title = title
        self.duration = duration

class Movie(Video):
    """" This calls provides pelis"""
    VALID_RATINGS  = ["P" ,"PG", "PG-13", "R"]
    def __init__(self, title, duration, movie_storyline, movies_poster, movie_trailer):
        self.storyline = movie_storyline
        self.poster_image_url = movies_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)

class TVShow(Video):
    "This class provides shows"
    def __init__(self,title, duration):
        self.



