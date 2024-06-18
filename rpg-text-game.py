# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Perso():
    
    def __init__(self, name, role, health, strength, inventory):
        print("hello new gamer!")
        name=input("choose your name: ")
        self.name=name
        print("your name is :", self.name)
        role= input("choose the role you want to play during this adventure: poet, sorcerer or knight? ")
        if role=="knight" or role=="poet" or role=="sorcerer":
            self.role=role 
            print("you chose to be :", self.role)
        else:
            print("there is no place for a", role, "in our world. come back in another garment", self.name)
        self.health=100
        self.strength=10
        self.inventory=None
        print("your health is initialized to", self.health, "strength to", self.strength, "and in your inventory, you have:", self.inventory)
        print("are you ready to play? let's start...")
        
    
    def __str__(self):
        #might add an icon ascii with p/k/s for role at right
        print("#"*40)
        print("# Your name:", self.name, "#".rjust(23-len(self.name)))  
        print("# You are :", self.role, "#".rjust(23-len(self.role)))
        print("# You have :", self.health, "points of health", "#".rjust(6))
        print("# You have :", self.strength, "points of strength", "#".rjust(5))
        if self.inventory is None:
            print("# You have nothing in your inventory", "#".rjust(3))
        else: 
            print("# You have :", self.inventory, "in your inventory", "#".rjust(30-len(self.inventory)))
        print("#"*40)
        
    def explore(place):
        pass
    
    def combat(perso1, perso2):
        pass
    
    def take_treasure(place):
        pass
    
    def go_to(place):
        pass
    
    def put_down_treasure(treasure):
        pass
    
    def check_inventory(inventory):
        pass
    
class Place():
    def __init__(self, name, enemy, treasure, quest):
        self.name=name
        self.enemy=enemy
        self.treasure=treasure
        self.quest=quest
        
    def __str__():
        pass
    
class Game():
    
    def __init__(self, starting_point, ending_point):
        print("New game")
        self.starting_point=None
        self.ending_point=None
        
    def __str__():
        pass

    def load_game(self):
        pass
    
    def save_game(self):
        pass
    
    
#game=Game()
name=""
role=""
health= 100
strength=10
inventory={}
person=Perso(name, role, health, strength, inventory)
print(person)
