import random


class Weapon(object):
    def __init__(self, type, damage, critical_strike):
        self.type = type
        self.damage = damage
        self.critical_strike = critical_strike

    def critical_hit(self):
        hit = random.random()
        if hit <= self.critital_strike:
            return True
        return False
