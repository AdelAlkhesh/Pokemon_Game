
from Pokemon_Type import Pokemon_Type
from Pokemon_Game import Pokemon
import random


class Alida(Pokemon_Type):

    def __init__(self):
        self.name = "Alida"
        self.level = random.randrange(1, 6)
        self.type = "Water"
        self.max_health = 30 * self.level
        self.curr_health = self.max_health
        self.attacks = {"Kith": (10 * 1.5 * self.level), "Hug": (7 *1.5 * self.level), "Cuddle": (12 * 1.5 * self.level)}

    



