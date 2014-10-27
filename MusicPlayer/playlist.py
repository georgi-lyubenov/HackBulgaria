from song import Song
import json

song1 = {"title": "Emerald Sword", "artists": "Rhapsody of Fire"}
song2 = {"title": "Highway to Hell", "artists": "AC/DC"}
album = {"name": "album name", "songs": [song1, song2]}


class Playlist(Song):
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        while song in self.songs:
            self.songs.remove(song)

    def total_length(self):
        result = 0
        for songs in self.songs:
            result += songs.length
        return result

    def remove_disrated(self, number):
        for song in self.songs:
            if song.rating <= number:
                self.songs.remove(song)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate <= 64:
                self.songs.remove(song)

    def show_artists(self):
        result = []
        for song in self.songs:
            result.append(song.artist)
        return result

    def str(self):
        result = []
        for song in self.songs:
            result.append(song.artist + " " + song.title + " " + str(song.length))
        return result

    def save(self, file_name):
        f = open(file_name, "w")
        json.dump(album, f)
        f.close()

    def load(self, file_name):
        f = open(file_name, "r")
        data = f.read()
        jsondata = json.loads(data)
        for row in jsondata['songs']:
            print(row['title'])
        f.close()

#my_playlist = Playlist("my_playlist")
#my_playlist.save("playlist.json")
#my_playlist.load("playlist.json")
