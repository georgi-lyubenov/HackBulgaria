import unittest
import song
from playlist import Playlist


class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = song.Song("Emerald Sword", "Rhapsody", "Fire", 4, 2400, 192)
        self.song2 = song.Song("Highway To Hell", "AC/DC", "Rough And Tough", 3, 2000, 64)
        self.my_playlist = Playlist("my_playlist")
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song2)

    def test_init(self):
        self.assertEqual(self.my_playlist.songs, [self.song, self.song2])
        self.assertEqual(self.my_playlist.name, "my_playlist")

    def test_add(self):
        self.assertEqual([self.song, self.song2], self.my_playlist.songs)

    def test_remove(self):
        self.my_playlist.remove_song(self.song)
        self.assertEqual(self.my_playlist.songs, [self.song2])

    def test_length(self):
        self.assertEqual(self.my_playlist.total_length(), 4400)

    def test_remove_disrated(self):
        self.my_playlist.remove_disrated(3)
        self.assertEqual(self.my_playlist.songs, [self.song])

    def test_remove_bad_quality(self):
        self.my_playlist.remove_bad_quality()
        self.assertEqual(self.my_playlist.songs, [self.song])

    def test_show_artists(self):
        self.assertEqual(self.my_playlist.show_artists(), ["Rhapsody", "AC/DC"])

    def test_str(self):
        self.my_playlist.remove_song(self.song2)
        self.assertEqual(self.my_playlist.str(), ["Rhapsody Emerald Sword 2400"])
if __name__ == '__main__':
    unittest.main()
