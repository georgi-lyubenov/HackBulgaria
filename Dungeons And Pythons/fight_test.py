import unittest
import weapon
import orc
import hero
import fight


class TestFight(unittest.TestCase):

    def setUp(self):
        self.sword = weapon.Weapon("Oathkeeper", 85, 0.1)
        self.axe = weapon.Weapon("Mighty Axe", 30, 0.2)

        self.crackhag_orc = orc.Orc("Crackhag", 120, True, 120, 1.5)
        self.bron_hero = hero.Hero("Bron", 120, "DragonSlayer", True, 120)

        self.crackhag_orc.equip_weapon(self.sword)
        self.bron_hero.equip_weapon(self.axe)
        self.battle = fight.Fight(self.bron_hero, self.crackhag_orc)

    def test_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.crackhag_orc.health, 120)

    def test_fight(self):
        self.assertTrue(self.battle.simulate_fight())

if __name__ == '__main__':
    unittest.main()
