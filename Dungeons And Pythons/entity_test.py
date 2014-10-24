import entity
import weapon
import unittest


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.creature = entity.Entity("Astral", 120, True, 120, None)

    def test_hero_init(self):
        self.assertEqual(self.creature.name, "Astral")
        self.assertEqual(self.creature.health, 120)

    def test_hero_get_health(self):
        self.assertEqual(self.creature.get_health(), 120)

    def test_hero_is_alive(self):
        self.assertTrue(True, self.creature.get_health())

    def test_hero_take_damage(self):
        self.creature.take_damage(60)
        self.assertEqual(60, self.creature.get_health())
        self.assertFalse(self.creature.take_damage(130))

    def test_hero_take_healing_dead(self):
        self.creature.condition = False
        self.assertFalse(self.creature.take_healing(20))

    def test_hero_take_healing(self):
        self.creature.health = 60
        self.assertTrue(self.creature.take_healing(40))

    def test_hero_take_healing_max(self):
        self.creature.health = 100
        self.assertTrue(self.creature.take_healing(40))

    def test_has_weapon(self):
        self.assertFalse(self.creature.has_weapon())

    def test_equip_weapon(self):
        self.creature.equip_weapon("sword")
        self.assertTrue(self.creature.has_weapon())
        self.assertEqual(self.creature.weapon, "sword")

    def test_attack(self):
        self.assertEqual(self.creature.attack(), 0)
        self.axe = weapon.Weapon("Mighty Axe", 25, 0.2)
        self.creature.equip_weapon(self.axe)
        self.assertEqual(self.creature.attack(), 25)

if __name__ == '__main__':
    unittest.main()
