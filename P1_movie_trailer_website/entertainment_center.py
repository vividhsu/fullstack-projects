"""
entertainment_center.py -- Build movie trailer website.
"""

import media
import fresh_tomatoes
import json

def create_movies():
    """Create movies list from movies.json file.

    Collects all movies' information from movies.json file.
    Creates movie instance by calling media.Movie class.
    Adds all movie objects to movies list.

    Returns:
        A list containing all movies.
    """
    movies = []
    try:
        with open('movies.json') as data_file:
            data = json.load(data_file)
        for info in data.values():
            movies.append(media.Movie(info["title"], info["poster"], info["trailer"], info["overview"]))
    except IOError, err:
        print "Can't open file: ", err
    return movies

if __name__ == "__main__":
    """Build movie website.
        Creates movies list by calling create_movies method.
        Builds movie website by calling open_movies_page method.
    """
    MOVIES = create_movies()
    if MOVIES:
        fresh_tomatoes.open_movies_page(MOVIES)
