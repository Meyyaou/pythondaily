# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Perso():
    
    def __init__(self, name=None, health=100, inventory=None, role=None):
        print("hello new gamer!")
        if name is None:
            name = input("choose your name: ")
        self.name=name
        #print("your name is :", self.name)
        if role is None:
            role=self.create_perso()
        self.role=role 
        #print("you chose to be :", self.role.__class__.__name__)
        self.health=health
        self.inventory=inventory
        #print("your health is initialized to", self.health)
        #self.check_inventory(self.inventory)
        print("are you ready to play? let's start...")
        
     #might add an icon ascii with p/k/s for role at right
    def __str__(self):
        result = f"""
        {'#' * 40}
        # Your name: {self.name}
        # You are: {self.role.__class__.__name__}
        # You have: {self.health} points of health
        # You have: {', '.join(self.inventory) if self.inventory else 'nothing'} in your inventory
        """
    
        if isinstance(self.role, Poet):
            result += f"# Your words are: {', '.join(self.role.words)}\n"
    
        if isinstance(self.role, Knight):
            result += f"# Your power is: {self.role.power}\n"
            result += f"{' '*8}# You have: {self.role.strength} points of strength\n"
            result += f"{' '*8}# Your attacks are: "
            result += ', '.join([a['attack'] for a in self.role.attack]) + "\n"
    
        if isinstance(self.role, Sorcerer):
            result += f"# Your power is: {self.role.power}\n"
        result += f"{' '*8}{'#' * 40}"

        return result
    
    def create_perso(self):
        while True:
            role= input("choose the role you want to play during this adventure: poet, sorcerer or knight? ")
            if role.lower()=="poet":
                return Poet(["sun", "life", "little", "good"])
            elif role.lower()=="knight":
                return Knight([{"points": 10, "attack": "torture"}, {"points": 20, "attack": "knife drop"}])
            elif role.lower()=="sorcerer":
                return Sorcerer()
            else:
                print("there is no place for a", role, "in our world. come back in another garment", self.name, "\n")
            
    def explore(self, place):
        if place.name == "Exola":
            print("you're exploring Exola, discovering various places from this kingdom, there is an ancient shop that sells weapons for old soldiers, a flower boutique and a farmer's depot.")
            kc11=input("write\n 1 if you wanna stop by the antique shop to get yourself the greatest weapon\n 2 if you wanna get romantic and buy a flower for your beloved princess\n or 3 if your stomach is gurling")
            if kc11=="1":
                print("you got yourself a nice new knife")
                #add more complexity TODO
                person.inventory["weapon"]="knife"
                print("knife added to your inventory")
            elif kc11=="2":
                print("you got for your lover a smelly petunia flower")
                #add more complexity TODO
                person.inventory["extra"]="petunia flower"
                print("petunia flower added to your inventory")
            elif kc11=="3":
                print("you bought some veggies and some fishes")
                #add more complexity TODO
                person.inventory["food"]="veggies"
                person.inventory["food2"]="fishes"
                print("veggies and fishes added to your inventory")
            else:
                print("try again !")
        
        
        elif place=="test2":
            pass
    
        elif place=="test3":
            pass
        
    def go_to(place):
        pass
    
    """ def take_treasure(place):
        pass
    
    def put_down_treasure(treasure):
        pass
    """
    def check_inventory(self,inventory):
        if self.inventory is not None:
            print("you have: ", str(self.inventory), "in your inventory")
        else:
            print("Your inventory is empty.")

class Poet(Perso):
    poem=""

    def __init__(self, words):
        #super().__init__(name=None, health=100, inventory=None, role=self)
        self.words=words
        #print("you chose to be a poet")
    
    def write(self, words):
        print("you have these words:", self.words, "\ and you have to write the best louange for the king or else you die")
        print("think wise:")
        poem=input("")
        
        return poem
    
    def evaluation_poem(self, poem):
        if poem is None:
            print("you have not written anything")
        else:
            val=random.randint(1, 100)
            if val>50:
                print("you got the chance, the king loved it")
                print("you're fine, you're now called Jaskier and you sing for the king")
                print("your quest is finished and you'll live a happy romantic life")
            elif val<50:
                print("you are dead")
                self.health=0
                print("you'll write mourning poems about death in the lambs")
                
class Knight(Perso):
    def __init__(self, attack):
        #super().__init__(name=None, health=100, inventory=None, role=self)
        self.strength= 10
        self.attack=attack
        self.power=10
        #print("you chose to be a knight")
        
        
    def combat(self, perso2):
        while self.health>0 or perso2.health>0:
            attacker=max(self.strength, perso2.strength)
            if attacker==self.strength:
                print("you can attack the enemy with", self.power, "power")
                print("choose the attack to make him lose: 1) for", self.attack[0],"\n2) for", self.attack[1],"\nor 3) for", self.attack[2])
                attack_type=input("you chose: ")
                print(attack_type.Upper())
                perso2.health-=self.power
                #self.strength+=self.attack[attack_type][attack]
                #self.power+=self.strength and add a lil calcul TODO
                print("you made him lose:", self.power)
                #print("and you gained", self.attack[attack_type][attack], "power points")
                #perso2.health-=self.attack[attack_type][attack]
                print("your enemy has now decided to attack back! beware")
            if attacker==perso2.strength:
                print("he attacks you using a deadly attack!")
                self.health-=perso2.power
                perso2.power+=perso2.strength
                print("you lose ", perso2.power, " health points")
                print("and your enemy has now ", perso2.power, "power points")
                
        if perso2.health<=0:
            print("you won !")
            print("the quest you had to finish is now done")
            print("you finish your game with :", self.health, "health points\n", self.power, "power points\nand", self.strength," strength points")
            
        if self.health<=0:
            print("you lost...")
            print("come back next time when you're stronger!")
        
   
class Sorcerer(Perso): 
    ingredient=["fire flower", "dragon tooth", "teary cloud", "ancient wooden fragment"]
    def __init__(self):
       # super().__init__(name=None, health=100, inventory=None, role=self)
        self.power=10
        #print("you chose to be a sorcerer")
        
    def find_ingredients(self):
        found=random.choice(ingredient)
        print("you found an ingredient: ",found)
        ramasse=input("do you want to take it?: 0)yes 1)no")
        if ramasse==0:
            #self.inventory.append(found)
            print("you added", found, "to your inventory")
            
    def make_new_potion(self, inventory):
        pass
class Enemy():
    pass
class NPC():
    pass
class Place():
    def __init__(self, name=None, enemy=None, treasure=None, quest=None):
        self.name=name
        self.enemy=enemy
        self.treasure=treasure
        self.quest=quest
        
    def __str__(self):
        return f"You are currently in {self.name}\nThe quest here is: {self.quest}\nTreasure: {self.treasure if self.treasure else 'No treasure'}"
        """ print("you are currently in", self.name)
        print("the quest in here is:", self.quest)
        
        if self.treasure is not None:
            print("the treasure in here is:", self.treasure)"""
        
class Game():
    
    def __init__(self, file="save.json"):
        print("New game")
        self.file=file
        self.load_game()
        
    def __str__():
        pass

    def load_game(self):
        try:
            with open(self.file, "r")as f:
                perso_dict=json.load(f)
                self.perso=Perso(**perso_dict)
        except FileNotFoundError:
            pass
    
    def save_game(self):
        with open(self.file, 'w') as f:
            json.dump(self.perso.__dict__,f)
        
game=Game()
playing=True
person=None
if person is None :
    name=None
    role=None
    health= 100
    strength=10
    inventory={}
    person=Perso(name, health, inventory, role)

while playing:
    print("welcome to our world...")
    print("*"*70)
    print("here you can be anything you want, explore various places, discover new treasures, make potions and live the most vivacious adventures of all time")
    print("*"*70)
    print("first let's see who you are: ")
    choice=input("write\n1 to check your character card\n2 to quit the game")
    
    if choice == "2":
        print("oh how sad, do you really want to leave us and go?")
        choice1=input("think wise, before we break into your computer :)\n yes \nor \nno?")
        if choice1.lower()=="yes":
            print("you suck. bye.")
            playing=False
        elif choice1.lower()=="no":
            print("you really dont know what you want.. pff goodbye anyway")
            playing=False
        else:
            print("what?")
            print("sorry i take this as a yes :)")
            playing=False
    
    elif choice == "1":
        print(person)
        print("hm we've got an interesting character here...\n")
        print("now that you know who you are, you are given a quest to complete.")
        if person.role.__class__.__name__ == 'Knight':
            print("Your quest as a knight is to explore the world, to find an enemy and to combat it.")
            print("your quest starts now")
            place=Place("Exola", "Enemio Enim", None, "COMBAT")
            print(place)
            kc1=input("write\n1 to explore Exola\n2 to check your inventory\n3 to quit the game")
            if kc1=="3":
                playing=False
            elif kc1=="2":
                person.check_inventory(person.inventory)
            elif kc1=="1":
                person.explore(place)
            else:
                print("try again!")
        elif person.role.__class__.__name__ == 'Poet':
            print(f"Your quest as a poet is to explore the world, to collect words and create the most beautiful poem of the universe")
        elif person.role.__class__.__name__ == 'Sorcerer':
            print(f"Your quest as a sorcerer is to explore the world, to discover new ingredients and make the world's most dangerous potion")
        
    else:
        print("try again\n")
    
    
    
