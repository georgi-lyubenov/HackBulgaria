class Song(object):
    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, new_rating):
        self.rating = new_rating
        if self.rating not in {0, 1, 2, 3, 4, 5}:
            raise ValueError



