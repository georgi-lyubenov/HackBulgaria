import song
import unittest


class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = song.Song("Emerald Sword", "Rhapsody", "Fire", 4, 2400, 192)

    def test_init(self):
        self.assertEqual(self.song.rating, 4)
        self.assertEqual(self.song.length, 2400)
        self.assertEqual(self.song.artist, "Rhapsody")

    def test_rate(self):
        self.song.rate(3)
        self.assertEqual(self.song.rating, 3)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            self.song.rate(2000)

if __name__ == '__main__':
    unittest.main()
