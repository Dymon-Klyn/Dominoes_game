import itertools
import random

class Game:
    def __init__(self):
        self.dominoes = [x for x in itertools.combinations_with_replacement(range(10), 2)]

g = Game()
print(g.dominoes)
