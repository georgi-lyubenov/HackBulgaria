from random import randrange
from hero import Hero
from orc import Orc


class Fight():
    def __init__(self, player1, player2):
        if isinstance(player1, Hero) and isinstance(player2, Orc):
            self.player1 = player1
            self.player2 = player2

    def simulate_fight(self):
        def attack(pl1, pl2):
            pl2.health -= pl1.attack()
            if pl2.health <= 0:
                pl2.condition = False
        first = True
        if randrange(100) < 50:
            first = True
        else:
            first = False
        #print(self.player1.name + " will attack first")

        while (self.player1.condition is True and self.player2.condition is True):
            if first is True:
                attack(self.player1, self.player2)
                first = False
            else:
                attack(self.player2, self.player1)
                first = True
        if first is True:
            print("The winner is Crackhag the Orc")
            return True
        else:
            print("The winner is Bron the DragonSlayer")
            return True


