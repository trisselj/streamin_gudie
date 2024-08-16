# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Defines classes for managing movies and streaming services, allowing users to add movies to a service, remove them, and search for where a movie is available.

# Initializes a movie object with title, genre, year, and director
class Movie:

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self): # Getter for title
        return self._title

    def get_genre(self): # Getter for genre
        return self._genre

    def get_director(self): # Getter for director
        return self._director

    def get_year(self): # Getter for year
        return self._year

# Initializes a StreamingService object with a name and an empty catalogue for storing movies
class StreamingService:

    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self): # Getter for name of streaming service
        return self._name

    def get_catalog(self): # Getter for the catalogue
        return self._catalog

    def add_movie(self, movie): # Adds movie object to the catalog and uses the movie title as the key
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title): # Removes a Movie from the catalog by its title if it exists
        if title in self._catalog:
            del self._catalog[title]
        else:
            print("Movie not found")

# Initializes a StreamingGuide object with an empty list of StreamingServices
class StreamingGuide:

    def __init__(self):
        self._streaming_services = []

    def add_streaming_service(self, service): # Adds a StreamingService object to the list of streaming services
        self._streaming_services.append(service)

    def delete_streaming_service(self, name): # Removes a StreamingService from the list by its name if it exists
        initial_length = len(self._streaming_services)
        self._streaming_services = [service for service in self._streaming_services if service.get_name() != name]
        if len(self._streaming_services) == initial_length:
            print("Streaming Service not found")

    def where_to_watch(self, movie_title): # Search for a movie by title across all streaming services and return a list of services offering the movie
        available_services = []
        movie_info = None
        
        for service in self._streaming_services: # Iterates through each streaming service in the guide
            catalog = service.get_catalog()
            if movie_title in catalog: # Checks if the movie is in the catalog
                movie = catalog[movie_title]
                if not movie_info: # Sets the movie info (title and year) once found
                    movie_info = f"{movie.get_title()} ({movie.get_year()})"
                available_services.append(service.get_name())
        
        if movie_info: # Returns the movie info and the names of available services
            return [movie_info] + available_services
        else:
            print("Movie can't be watched anywhere!")
            return None
