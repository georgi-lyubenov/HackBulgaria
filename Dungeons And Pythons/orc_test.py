import orc
import unittest
import weapon


class OrcTest(unittest.TestCase):

    def setUp(self):
        self.crackhag_orc = orc.Orc("CrackHag", 120, True, 120, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.crackhag_orc.name, "CrackHag")
        self.assertEqual(self.crackhag_orc.health, 120)

    def test_orc_get_health(self):
        self.assertEqual(self.crackhag_orc.get_health(), 120)

    def test_orc_is_alive(self):
        self.assertTrue(True, self.crackhag_orc.get_health())

    def test_orc_take_damage(self):
        self.crackhag_orc.take_damage(60)
        self.assertEqual(60, self.crackhag_orc.get_health())
        self.assertFalse(self.crackhag_orc.take_damage(130))

    def test_orc_take_healing_dead(self):
        self.crackhag_orc.condition = False
        self.assertFalse(self.crackhag_orc.take_healing(20))

    def test_orc_take_healing(self):
        self.crackhag_orc.health = 60
        self.assertTrue(self.crackhag_orc.take_healing(40))

    def test_orc_take_healing_max(self):
        self.crackhag_orc.health = 100
        self.assertTrue(self.crackhag_orc.take_healing(40))

    def test_orc_attack(self):
        self.assertEqual(self.crackhag_orc.attack(), 0)
        self.axe = weapon.Weapon("Mighty Axe", 25, 0.2)
        self.crackhag_orc.equip_weapon(self.axe)
        self.assertEqual(self.crackhag_orc.attack(), 25 * 1.5)
if __name__ == '__main__':
    unittest.main()
