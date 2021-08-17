from Pokemon_Game import Pokemon
import random

#This is a custom Pokemon class just for testing purposes. Everything here is pretty much placeholder. 
class Alida(Pokemon):

    def __init__(self):
        self.name = "Alida"
        #self.level = random.randrange(1,6)
        self.level = 1
        self.type = "Water"
        self.max_health = 20
        self.curr_health = self.max_health
        self.attack_names = ["Kith", "Hug", "Cuddle"]
        self.attacks = {"Kith": (10 * 1.5 * self.level), "Hug": round((7 *(self.level **0.5))), "Cuddle": (12 * 1.5 * self.level)}
        self.knocked_out = False
        self.xp_meter = 0
    
    def test_method(self):  #Method for testing purposes. Will be removed later.
        water = Pokemon("Water", "Water", 20, 20)
        fire = Pokemon("Fire", "Fire", 20, 20)
        electric = Pokemon("Electric", "Electric", 20, 20)
        ice = Pokemon("Ice", "Ice", 20, 20)
        grass = Pokemon("Grass", "Grass", 20, 20)
        normal = Pokemon("Normal", "Normal", 20, 20)

        print()
        print()
        water.attack(fire, "Test", 10)
        print()
        print()
        water.attack(grass, "Test", 10)
        print()
        print()
        fire.attack(water, "Test", 10)
        print()
        print()
        fire.attack(grass, "Test", 10)
        print()
        print()
        fire.attack(ice, "Test", 10)
        print()
        print()
        grass.attack(fire, "Test", 10)
        print()
        print()
        grass.attack(water, "Test", 10)
        print()
        print()
        ice.attack(water, "Test", 10)
        print()
        print()
        ice.attack(grass, "Test", 10)
        print()
        print()
        electric.attack(water, "Test", 10)
        print()
        print()
        electric.attack(grass, "Test", 10)
        print()
        print()
        normal.attack(fire, "Test", 10)
        print()
        print()
        fire.attack(fire, "Test", 10)
        print()
        print()
        water.attack(water, "Test", 10)











