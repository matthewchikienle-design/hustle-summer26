import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        
        while True: 
             opponent.take_damage(self.attack())

             if not opponent.is_alive():
                  print(self.name + "won!")
                  break
             
             self.take_damage(opponent.attack())
             if not self.is_alive():
                  print(opponent.name + " won!")

                  break
        

    def add_ability(self, ability):
            self.abilities.append(ability)

    def attack(self): 
         total_damage = 0
         for ability in self.abilities:
              total_damage += ability.attack()
              print(total_damage)
              return total_damage
    
    def add_armor(self, armor):
         self.armors.append(armor)

    def defend(self):
         total_block = 0
         for armor in self.armors:
              total_block += armor.block()
              print(total_block)
              return total_block
         
    def take_damage(self, damage):
         blocked = self.defend()
         actual_damage = max(damage - blocked, 0)
         self.current_health -= actual_damage
         if self.current_health < 0:
              self.current_health = 0
              return actual_damage
         print(self.current_health)
        
         

               
              

         

    
    
        
        
              
         
        


if __name__ =="__main__":
    my_hero = Hero("Spider-man", 150)
    #print(my_hero.name)
    #print(my_hero.current_health)
    #my_opponent = Hero("Captain America", 200)
    #my_hero.battle(my_opponent)
    my_hero.add_ability(Ability("Web Shooter", 25))
    my_hero.add_ability(Ability("Spidey Senses", 10))
    my_hero.add_armor(Armor("Goggles", 8))
    my_hero.add_armor(Armor("Iron Spider Legs", 30))
    my_hero.add_armor(Armor("Socks", 10))

    my_hero.take_damage(40)


    

    
