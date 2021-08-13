class Pokemon(): 
    

   
   def __init__(self, name, level, type,max_health, curr_health):
     
       self.name = name 
       self.level = level 
       self.type = type 
       self.max_health = max_health
       self.curr_health = curr_health


   def lose_health(self,damage): 
       self.curr_health -= damage
       print("Your pokemon lost {amount} health".format( amount = damage))
       print("Your pokemon is now at {amount} HP".format(amount = self.curr_health))
       if self.curr_health <= 0: 
           self.knock_out()
       return self.curr_health
  
    
   def regain_health(self, heal):
       if self.curr_health != self.max_health:
            self.curr_health += heal
            print("Your Pokemon regained {} HP".format(heal))
            print("Your pokemon is now at {} HP".format(self.curr_health))
            return self.curr_health
       else: 
           print("Your Pokemon is already at Max HP!")

   def knock_out(self):

       print("Oh no! Your Pokemon has been knocked the fuck out!")



   def revive(self):
       self.curr_health = self.max_health / 2
       print("Your Pokemon has been revived with half HP!")
       print("Your Pokemon has {} HP".format(self.curr_health))
       



shen = Pokemon("Shen", 12, "Fire", 400, 400)
shen.lose_health(30)
shen.regain_health(20)
shen.knock_out()
shen.revive()
shen.lose_health(200)
    


   


    
