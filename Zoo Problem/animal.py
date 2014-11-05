from random import randrange
import json


def load_settings(file_name):
        f = open(file_name, "r")
        data = f.read()
        f.close()
        return json.loads(data)


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self.weight = weight

    def eat(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                return animal['food/weight ratio'] * self.weight

    def feed_animal(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                if animal['food type'] == "carnivore":
                    return animal['food/weight ratio'] * self.weight * 4
                elif animal['food type'] == "herbivore":
                    return animal['food/weight ratio'] * self.weight * 2

    def grow(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                self.weight += animal['food/weight ratio'] * self.weight
                if self.weight < animal['average weight']:
                    return False
                return True

    def die(self):
        for animal in load_settings("database.json"):
            if animal['species'] == self.species:
                chance_of_dying = self.age / animal['life_expectancy']
                if randrange(1, 10) <= chance_of_dying * 10:
                    return True
                return False
