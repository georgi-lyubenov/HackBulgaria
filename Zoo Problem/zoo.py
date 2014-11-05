from animal import *
from main import *
from random import randrange


class Zoo:

    def __init__(self, capacity, budget):
        self.animalsCollection = []
        self.capacity = capacity
        self.budget = budget
        self.animalsAfterGestationPeriod = []

    def see_animals(self):
        for animal in self.animalsCollection:
            return (animal.name + " : " + animal.species + ", " + str(animal.age) + ", " + str(animal.weight))

    def move_to_habitat(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)

    def accommodate(self, species, age, name, gender, weight):
        if len(self.animalsCollection) < self.capacity:
            self.new = Animal(species, age, name, gender, weight)
            self.animalsCollection.append(self.new)

    def dayly_incomes(self):
        dayly = 0
        for animal in self.animalsCollection:
            dayly += 60
        return dayly

    def dayly_outcomes(self):
        outcomes = 0
        foodType = ""
        for animal in self.animalsCollection:
            foodType = ""
            for dictionary in load_settings("database.json"):
                if dictionary['species'] == animal.species:
                    foodType = dictionary["food type"]
            if foodType == "carnivore":
                outcomes += 4
            else:
                outcomes += 2
        return outcomes

    def born_animal(self, month):
        for animal in self.animalsCollection:
            for i in range(1, len(self.animalsCollection)):
                if animal.species == self.animalsCollection[i].species and animal.gender != self.animalsCollection[i].gender:
                    for diction in load_settings("database.json"):
                        if diction['species'] == animal.species:
                            if month >= diction['gestation period']:
                                return True
                            else:
                                return False

    def animal_die(self, species, name):
        for animal in self.animalsCollection:
            if animal.species == species and animal.name == name:
                self.animalsCollection.remove(animal)
                break

    def simulate(self, interval_of_time, period):
        self.interval = 0
        if interval_of_time == "months":
            self.interval = period
        elif interval_of_time == "days":
            self.interval = period / 30
        elif interval_of_time == "years":
            self.interval = period * 12
        else:
            print("invalid input")
        #print(self.see_animals())
        for i in range(self.interval):
            for each in self.animalsCollection:
                while each.grow() is False:
                    print("the animal is still growing")

                if each.die() is True:
                    print("There is an animal, which has died")
                    self.animal_die(each.species, each.name)
        print("the animals have grown")
        if self.budget + self.dayly_incomes() - self.dayly_outcomes() > 0:
            print("the zoo does have enough budget to pay for the food")
        if self.born_animal(self.interval) is True:
            print("an animal is going to be born")
        else:
            print("no animal is going to be born")
