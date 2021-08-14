import random

class Pokemon():

    def __init__(self, name, type, max_health, curr_health):

        self.name = name
        self.level = random.randrange(1,6)
        self.type = type
        self.max_health = max_health
        self.curr_health = curr_health

    def lose_health(self, damage):
        hit_counter = 0
        self.curr_health -= damage
        print("{} lost {} health".format(self.name, damage))
        print("{} is now at {} HP".format(self.name, self.curr_health))
        if self.curr_health <= 0:
            self.knock_out()
        return self.curr_health

    def regain_health(self, heal):
        if self.curr_health != self.max_health:
            self.curr_health += heal
            print("{} regained {} HP".format(self.name, heal))
            print("{} is now at {} HP".format(self.name, self.curr_health))
            return self.curr_health
        else:
            print("Your Pokemon is already at Max HP!")

    def knock_out(self):
        print("{} has been knocked out!".format(self.name))

    def revive(self):
        self.curr_health = self.max_health / 2
        print("{} has been revived with half HP!".format(self.name))
        print("{} has {} HP".format(self.name, self.curr_health))

    def level_up(self):
        self.level += 1
        self.max_health *= 1.5 * self.level
        self.curr_health = self.max_health
        print("{} levels up and is now level {}!".format(self.name, self.level))
        print("{} now has {} Maximum HP!".format(self.name, self.max_health))





