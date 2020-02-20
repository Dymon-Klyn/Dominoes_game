import itertools
import random

class Game:
    def __init__(self):
        self.dominoes = itertools.combinations_with_replacement(range(10), 2)

g = Game()
print(g.dominoes)
