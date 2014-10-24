import hero

import unittest


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 120, "DragonSlayer", True, 120)

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 120)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_hero_known_as(self):
        self.assertEqual("Bron the DragonSlayer", self.bron_hero.known_as())

    def test_hero_get_health(self):
        self.assertEqual(self.bron_hero.get_health(), 120)

    def test_hero_is_alive(self):
        self.assertTrue(True, self.bron_hero.get_health())

    def test_hero_take_damage(self):
        self.bron_hero.take_damage(60)
        self.assertEqual(60, self.bron_hero.get_health())
        self.assertFalse(self.bron_hero.take_damage(130))

    def test_hero_take_healing_dead(self):
        self.bron_hero.condition = False
        self.assertFalse(self.bron_hero.take_healing(20))

    def test_hero_take_healing(self):
        self.bron_hero.health = 60
        self.assertTrue(self.bron_hero.take_healing(40))

    def test_hero_take_healing_max(self):
        self.bron_hero.health = 100
        self.assertTrue(self.bron_hero.take_healing(40))
if __name__ == '__main__':
    unittest.main()
