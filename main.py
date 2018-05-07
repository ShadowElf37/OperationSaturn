import random
from time import sleep
from people import *
from lib import *
from loader import *


class World:
    def __init__(self):
        self.people = []
        self.relationships = []

    def get_person(self, name):
        return [p for p in self.people if p.name == name][0]

    def get_rel(self, name1, name2):
        try:
            return [r for r in self.relationships if name1 == r.people[0].name and name2 == r.people[1].name][0]
        except IndexError:
            r = Relationship(self.get_person(name1), self.get_person(name2))
            self.relationships.append(r)
            self.get_person(name1).relationships.append(r)
            self.get_person(name2).relationships.append(r)
            return r


class Location:
    def __init__(self, size):
        self.people = {}
        self.size = size

    def add_people(self, *p):
        for pp in p:
            self.people[pp] = (random.randint(0, self.size), random.randint(0, self.size))

    def remove_person(self, p: Person):
        self.people.pop(p)

    def tick(self):
        for p1 in self.people:
            p2 = random.choice(list(self.people.keys()))
            r = p1.get_relationship(p2)
            dist = distance(self.people[p1], self.people[p2])
            v = (dist * r.innovation) - 1


class Conversation:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rel = p1.get_relationship(p2)

    def have(self):
        ...


if __name__ == '__main__':
    people = load_people()
    load_relationships(people)
    loc = Location(30)
    loc.add_people(*people)
    print(loc.people)
    while True:
        loc.tick()
        sleep(1)