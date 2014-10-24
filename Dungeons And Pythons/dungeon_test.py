from dungeon import Dungeon

import unittest
import hero
import orc


class DungeonTest(unittest.TestCase):
    def setUp(self):
        self.crackhag_orc = orc.Orc("Crackhag", 120, True, 120, 1.5)
        self.bron_hero = hero.Hero("Bron", 120, "DragonSlayer", True, 120)
        self.map = Dungeon("dungeon.txt")

    def test_spawn(self):
        #print map
        #self.assertTrue(self.map.print_map())
        #changes content of the file
        self.assertTrue(self.map.spawn(self.bron_hero.name, self.bron_hero))
        #print new map
        self.assertTrue(self.map.print_map())
        self.assertTrue(self.map.spawn(self.crackhag_orc.name, self.crackhag_orc))
        #self.assertTrue(self.map.print_map())
        #self.assertTrue(self.map.move(self.bron_hero.name, "right"))
        self.assertTrue(self.map.print_map())


if __name__ == '__main__':
    unittest.main()
