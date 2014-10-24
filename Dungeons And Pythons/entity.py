class Entity(object):
    def __init__(self, name, health, condition, max_health, weapon):
        self.name = name
        self.health = health
        self.max_health = health
        if self.health >= 0:
            self.condition = True
        else:
            self.condition = False
        self.weapon = weapon

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.condition

    def take_damage(self, damage_points):
        if self.health > damage_points:
            self.health = self.health - damage_points
        else:
            self.health = 0
            self.condition = False

    def take_healing(self, healing_points):
        if self.condition is False:
            return False
        else:
            if self.health + healing_points <= self.max_health:
                self.health = self.health + healing_points
                return True
            else:
                self.health = self.max_health
                return True

    def has_weapon(self):
        if self.weapon is None:
            return False
        return True

    def equip_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        if self.weapon is None:
            return 0
        return self.weapon.damage

