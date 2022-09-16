import csv
<<<<<<< HEAD
import os
=======
>>>>>>> templates
from pathlib import Path
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.artist import Artist
from music.domainmodel.track import Track
from music.domainmodel.genre import Genre
from music.domainmodel.review import Review
from music.domainmodel.album import Album
from music.domainmodel.user import User
from music.adapters.csvdatareader import TrackCSVReader

class MemoryRepository(AbstractRepository):
    # Tracks ordered by id which is assumed unique.

    def __init__(self):
        self.__tracks = list()
        self.__tracks_index = dict()
        self.__artists = list()
        self.__genres = list()
        self.__albums = list()
        self.__reviews = list()
        self.__users = list()
    
    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_track(self, track: Track):
        insort_left(self.__tracks, track)
<<<<<<< HEAD
        self.__tracks_index[track.track_id] = track
=======
        self.__tracks_index[track.id] = track
>>>>>>> templates
    
    def get_track(self, id: int) -> Track:
        track = None
        try:
            track = self.__tracks_index[id]
        except KeyError:
            pass # Ignore exception, return None.
            
        return track
    
    def get_tracks_by_artist(self, target_artist: Artist) -> List[Track]:
<<<<<<< HEAD
        matching_tracks = list()

        try:
            for track in self.__tracks:
=======
        target_track = Track(track_id = None, track_title = None)
        target_track.artist = target_artist
        matching_tracks = list()

        try:
            index = self.tracks_index(target_track)
            for track in self.__tracks[index:None]:
>>>>>>> templates
                if track.artist == target_artist:
                    matching_tracks.append(track)
                else:
                    break
        except ValueError:
            # No tracks for specified artist. Simply return an empty list.
            pass

        return matching_tracks
    
<<<<<<< HEAD
=======
    def get_track_ids_for_artist(self, full_name: str):
        # Linear search, to find the first occurence of an artist with the name artist_name.
        track_artist = next((artist for artist in self.__artists if artist.full_name == artist), None)

        # Retrieve the ids of tracks associated with the artist.
        if track_artist is not None:
            track_ids = list()
            for track in self.__tracks:
                if track.track_artist.full_name == full_name:
                    track_ids.append(track.id)
        else:
            # No Album with name full_name, so return an empty list.
            track_ids = list()
        
        return track_ids
    
>>>>>>> templates
    def get_number_of_tracks(self) -> int:
        return len(self.__tracks)

    def get_tracks_by_id(self, id_list):
        # Strip out any ids in id_list that don't respresent Track ids in the repository.

        existing_ids = [id for id in id_list if id in self.__tracks_index]

        # Fetch the tracks.
        tracks = [self.__tracks_index[id] for id in existing_ids]
        return tracks
    
<<<<<<< HEAD
    def get_track_ids_for_artist(self, artist_name: str):
        # Linear search, to find the first occurence of an artist with the name artist_name.
        artist = next((artist for artist in self.__artists if artist.artist_name == artist), None)

        # Retrieve the ids of tracks associated with the artist.
        if artist is not None:
            track_ids = list()
            for track in self.__tracks:
                if track.artist.artist_name == artist_name:
                    track_ids.append(track.id)
        else:
            # No artist with name artist_name, so return an empty list.
            track_ids = list()
        
        return track_ids
    
=======
>>>>>>> templates
    def get_track_ids_for_genre(self, genre_name: str):
        # Linear search, to find the first occurence of a Genre with the name genre_name.
        genre = next((genre for genre in self.__genres if genre.genre_name == genre_name), None)

        # Retrieve the ids of tracks associated with the Genre.
        if genre is not None:
            track_ids = list()
            for track in self.__tracks:
                for genre in track.genres:
                    if genre.genre_name == genre_name:
                        track_ids.append(track.id)
        else:
            # No Genre with name genre_name, so return an empty list.
            track_ids = list()
        
        return track_ids
    
    def get_track_ids_for_album(self, album_name: str):
        # Linear search, to find the first occurence of an Album with the name album_name.
        album = next((album for album in self.__albums if album.album_name == album_name), None)

        # Retrieve the ids of tracks associated with the Album.
        if album is not None:
            track_ids = list()
            for track in self.__tracks:
                if track.album.album_name == album_name:
                    track_ids.append(track.id)
        else:
            # No Album with name album_name, so return an empty list.
            track_ids = list()
        
        return track_ids

<<<<<<< HEAD
    def get_tracks_by_genre(self, target_genre: Genre) -> List[Track]:
        matching_tracks = list()

        try:
            for track in self.__tracks:
                for genre in track.genres:
                    if genre == target_genre:
                        matching_tracks.append(track)
                    else:
                        break
        except ValueError:
            # No tracks for specified genre. Simply return an empty list.
            pass

        return matching_tracks
    
    def get_tracks_by_album(self, target_album: Album) -> List[Track]:
        matching_tracks = list()

        try:
            for track in self.__tracks:
                if track.album == target_album:
                        matching_tracks.append(track)
                else:
                    break
        except ValueError:
            # No tracks for specified album. Simply return an empty list.
            pass

        return matching_tracks

=======
>>>>>>> templates
    def add_genre(self, genre: Genre):
        self.__genres.append(genre)
    
    def get_genres(self) -> List[Genre]:
        return self.__genres
    
    def add_artist(self, artist: Artist):
        self.__artists.append(artist)
    
    def get_artists(self) -> List[Artist]:
        return self.__artists
    
    def add_album(self, album: Album):
        self.__albums.append(album)
    
    def get_albums(self) -> List[Album]:
        return self.__albums
    
<<<<<<< HEAD
    def get_tracks(self) -> List[Track]:
        return self.__tracks
    
    
    def add_review(self, review: Review):
        # Not sure if this is implemented correctly yet (i.e. does Track need this method)
        super().add_review(review)
        self.__reviews.append(review)

    def get_reviews(self):
        return self.__reviews

def populate(data_path: Path, repo: MemoryRepository):
    """ Populates the given repository using data at the given path. """
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    albums_file_name = os.path.join(dirname, 'adapters/data/raw_albums_excerpt.csv')
    tracks_file_name = os.path.join(dirname, 'adapters/data/raw_tracks_excerpt.csv')
    reader = TrackCSVReader(albums_file_name, tracks_file_name)
    reader.read_csv_files()

    for track in reader.dataset_of_tracks:
        repo.add_track(track)

    for artist in reader.dataset_of_artists:
        repo.add_artist(artist)

    for genre in reader.dataset_of_genres:
        repo.add_genre(genre)
    
    for album in reader.dataset_of_albums:
        repo.add_album(album)
    
    #repo.add_tracks(reader.dataset_of_tracks)
    #repo.add_artists(reader.dataset_of_artists)
    #repo.add_genres(reader.dataset_of_genres)
    #repo.add_albums(reader.dataset_of_albums)



=======
    def add_review(self, review: Review):
        # to implement
        pass
    
    def get_reviews(self):
        return self.__reviews
>>>>>>> templates
