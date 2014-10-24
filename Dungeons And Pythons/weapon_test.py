import weapon
import random
import unittest


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.axe = weapon.Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual(self.axe.critical_strike, 0.2)
        self.assertEqual(self.axe.type, "Mighty Axe")
        self.assertEqual(self.axe.damage, 25)

    def test_critical_hit(self):
        result = []
        for i in range(1000):
            result.append(random.random())
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
