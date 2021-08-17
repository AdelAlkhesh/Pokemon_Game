import random


class Pokemon():

    def __init__(self, name, type, max_health, curr_health):

        self.name = name
        self.level = 1
        self.type = type
        self.max_health = max_health
        self.curr_health = curr_health
        self.knocked_out = False
        self.xp_meter = 0

    #Method that is called when a pokemon takes damage and loses health. 
    def lose_health(self, damage):
        hit_counter = 0
        self.curr_health -= damage
        print("{} lost {} health".format(self.name, damage))
        print("{} is now at {} HP".format(self.name, self.curr_health))
        if self.curr_health <= 0:
            self.knock_out()
        return self.curr_health

    #Method to heal the Pokemon. Will be implemented later through the Potion item. 
    def regain_health(self, heal):
        if self.knocked_out != True:
            if self.curr_health != self.max_health:
                self.curr_health += heal
                print("{} regained {} HP".format(self.name, heal))
                print("{} is now at {} HP".format(self.name, self.curr_health))
                self.xp_gained()
                return self.curr_health
            else:
                print("Your Pokemon is already at Max HP!")
        else:
            print("{} is knocked out and cannot be healed. You must revive it first!")

    #Method called when a pokemon takes too much damage and gets knocked out. Sets the knocked_out value to True, preventing from taking any further action
    def knock_out(self):
        print("{} has been knocked out!".format(self.name))
        self.knocked_out = True

    #Method to revive a knocked out pokemon.
    def revive(self):
        self.curr_health = self.max_health / 2
        print("{} has been revived with half HP!".format(self.name))
        print("{} has {} HP".format(self.name, self.curr_health))
        self.knocked_out = False

    #Method to level up the pokemon. Increments level by 1, increases max health, and sets the current health back to full.
    def level_up(self):
        self.level += 1
        self.max_health +=  round(self.level ** 0.5)
        self.curr_health = self.max_health
        print("{} levels up and is now level {}!".format(self.name, self.level))
        print("{} now has {} Maximum HP!".format(self.name, self.max_health))
        self.xp_meter = 0

    #This method calculates the xp needed to reach the next level, based on the current level.
    def next_level(self, level):
        return round(4*(level ** 3) / 5)

    #This method calculates xp gain. If the xp gained reaches the xp needed to level up, it calls the level up method. 
    def xp_gained(self):
        gain = random.randrange(5,20)
        self.xp_meter += gain
        if self.xp_meter >= self.next_level(self.level):
            self.level_up()
        else: 
            pass
        return self.xp_meter

    #Method for pokemon attacks. Takes into account the type of the attacking pokemon vs the type that it is attacking. Deals damage accordingly. 
    def attack(self, Pokemon, attack, attack_damage):

        if self.knocked_out != True and Pokemon.knocked_out != True:
            print("{} used {} against {}".format(
                self.name, attack, Pokemon.name))

            if (self.type == "Grass" or self.type == "Electric") and (Pokemon.type == "Water"):
                print("The attack dealt {} damage. It was super effective!".format(
                    attack_damage *2))
                Pokemon.lose_health(attack_damage * 2)
                self.xp_gained()
                

            elif (self.type == "Fire" or self.type == "Ice") and (Pokemon.type == "Grass"):
                print("The attack dealt {} damage. It was super effective!".format(
                    attack_damage * 2))
                Pokemon.lose_health(attack_damage * 2)
                self.xp_gained()

            elif (self.type == "Fire") and (Pokemon.type == "Ice"):
                print("The attack dealt {} damage. It was super effective!".format(
                    attack_damage *2))
                Pokemon.lose_health(attack_damage * 2)
                self.xp_gained()
            
            elif (self.type == "Water") and (Pokemon.type == "Fire"):
                print("The attack dealt {} damage. It was super effective!".format(
                    attack_damage *2))
                Pokemon.lose_health(attack_damage * 2)
                self.xp_gained()
                
            elif (self.type == "Normal"):
                print("The attack dealt {} damage. It was effective!".format(
                    attack_damage))
                Pokemon.lose_health(attack_damage)
                self.xp_gained()

            else:
                print("The attack deal {} damage. It was not very effective...".format(attack_damage /2))
                Pokemon.lose_health(attack_damage/2)
                self.xp_gained()

        elif self.knocked_out != True and Pokemon.knocked_out == True:
            print("{} is already knocked out! select another pokemon to attack!".format(
                Pokemon.name))

        else:
            print("{} is knocked out and cannot perform any attacks! Revive it or select another pokemon to attack with.".format(self.name))












