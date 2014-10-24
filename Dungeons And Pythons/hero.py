from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nichname, condition, max_health):
        self.name = name
        self.health = health
        self.nickname = nichname
        if self.health >= 0:
            self.condition = True
        else:
            self.condition = False
        self.max_health = health

    def known_as(self):
        return self.name + " the " + self.nickname

