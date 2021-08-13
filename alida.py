from Pokemon_Game import Pokemon

class Alida(Pokemon): 
   
    def __init__(self):
        self.name = "Alida"
        self.level = 1 
        self.type = "Water"
        self.max_health = 60
        self.curr_health = 60

    def cutie_attack(self, Pokemon):
        damage = 10
        print("Alida used CutiePie Attack!")
        if Pokemon.type == "Fire" or Pokemon.type == "Air": 
            Pokemon.curr_health -= (damage * 2)
            print("It dealt {} damage. It was very effective!".format(damage *2))
            Pokemon.lose_health(damage)
        elif Pokemon.type == "Grass": 
            Pokemon.curr_health -= damage
            print("It dealth {} damage. It was effective!".format(damage))
            Pokemon.lose_health(damage)
        else: 
            Pokemon.curr_health -= (damage / 2)
            print("It dealt {} damage. It wasn't very effective!".format(damage /2))
            Pokemon.lose_health(damage)
            







        
