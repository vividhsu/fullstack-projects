"""
media.py -- create Movie class.
"""


class Movie(object):
    """ Summary of class Movie

    Contains the information of movie,
    including title, poster, trailer and overview.

    Attributes:
        title: A string indicating the name of the movie.
        poster_image_url: A string indicating the url of the poster.
        trailer_youtube_url: A string indicating the url of the trailer.
        imdb_url: A string indicating the overview from imdb.
    """
    def __init__(self, movie_title, poster_image, trailer_youtube, review_imdb):
        """
        Inits Movie with parameters movie_title, poster_image,
        trailer_youtube and review_imdb.
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_url = review_imdb


