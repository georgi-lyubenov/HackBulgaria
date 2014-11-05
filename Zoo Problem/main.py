import json

from zoo import *


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


def main():
    settings = load_settings("database.json")
    zoo = Zoo(45, 1000)
    zoo.accommodate("Lion", 2, "Ivan", "male", 100)
    zoo.accommodate("Lion", 2, "Ivanka", "female", 110)
    zoo.accommodate("Zebra", 1, "Penka", "female", 90)
    #zoo.accommodate("Tiger", 5, "Rocky", "male", 130)
    #zoo.accommodate("Tiger", 5, "Mariq", "female", 120)
    #print(zoo.dayly_outcomes())
    #zoo.animal_die("Zebra", "Penka")
    #zoo.see_animals()
    #print(zoo.born_animal(36))
    #zoo.see_animals()
    zoo.simulate("years", 3)

if __name__ == '__main__':
    main()
