from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, condition, max_health, berserk_factor):
        Entity.__init__(self, name, health, condition, max_health, None)
        self.name = name
        self.health = health
        self.max_health = max_health
        self.__set_selfberserk_factor(berserk_factor)
        if self.health >= 0:
            self.condition = True
        else:
            self.condition = False

    def __set_selfberserk_factor(self, berserk_factor):
        if berserk_factor > 1 and berserk_factor < 2:
            self.berserk_factor = berserk_factor
        else:
            raise ValueError

    def attack(self):
        if self.weapon is None:
            return 0
        return self.weapon.damage * self.berserk_factor


