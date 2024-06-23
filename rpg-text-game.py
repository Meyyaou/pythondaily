# press Python 3 code in this online editor and run it.
import random

class Perso:
    
    def __init__(self, name=None, health=100, inventory=None, role=None, silent=False):
        if not silent:
            print("hello new gamer!")
            if name is None:
                name = input("choose your name: ")
        self.name = name
        self.health = health
        if inventory is None:
            inventory = {}
        self.inventory = inventory
        if role is None:
            role = self.create_perso()
        self.role = role
        if not silent:
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
                return Knight([{"points": 10, "attack": "torture"}, {"points": 20, "attack": "knife drop"}], 10, 10)
            elif role.lower()=="sorcerer":
                return Sorcerer()
            else:
                print("there is no place for a", role, "in our world. come back in another garment", self.name, "\n")
            
    def explore(self, place):
        if place.name == "Exola":
            print("you're exploring Exola, discovering various places from this kingdom, there is an ancient shop that sells weapons for old soldiers, a flower boutique and a farmer's depot.")
            kc11=input("press\n 1 if you wanna stop by the antique shop to get yourself the greatest weapon\n 2 if you wanna get romantic and buy a flower for your beloved princess\n or 3 if your stomach is gurling")
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
        
        
        elif place=="Belova":#todo implement this
            pass
    
        elif place=="Mordor":#todo implement this
            pass
        
    def go_to(place):
        pass
    
    """ def take_treasure(place):
        pass
    
    def put_down_treasure(treasure):
        pass
    """
    def check_inventory(self,inventory):
        if self.inventory:
            print("you have: ", str(self.inventory), "in your inventory")
        else:
            print("Your inventory is empty.")

class Poet(Perso):
    poem=""

    def __init__(self, words, name=None, health=100, inventory=None):
        super().__init__(name, health, inventory, role=self, silent=True)
        self.words=words
        #print("you chose to be a poet")
    
    def search_for_words(self, place):
        #ToDO addd more complexity here too
        print("you found no words")

    def press(self, words):
        print("you have these words:", self.words, "\n and you have to press the best louange for the king or else you die")
        print("think wise:")
        poem=input("")
        
        return poem
            
    def check_words(self, poem):
        poem_words=poem.split(" ")
        for word in poem_words:
           if word.lower() not in [w.lower() for w in self.words]:
                print("you used words beyond your power ")
                return False
        return True
        
        
    def evaluate_poem(self, poem):
        if poem is None or not self.check_words(poem):
            val = 0
        else:
            val = random.randint(1, 100)
        if val>50:
            print("by chance, the king loved it")
            print("you're fine, you're now called Jaskier and you sing for the king")
            print("your quest is finished and you'll live a happy romantic life")
        elif val<50:
            print("the king decides that you'll soon be sentenced to death")
            print("you are dead")
            self.health=0
            print("you'll press mourning poems about death in the lambs")
                
class Knight(Perso):
    def __init__(self, attack, strength, power, name=None, health=100, inventory=None):
        super().__init__(name, health, inventory, role=self, silent=True)
        self.strength= 10
        self.attack=attack
        self.power=10

    def find_enemy(self,perso2):
        pass
    
    def combat(self, enemy):
        while self.health > 0 and enemy.health > 0:
            attacker = max(self.strength, enemy.strength)
            if attacker == self.strength:
                print("you can attack the enemy with", self.power, "power")
                print("choose the attack to make him lose: 1) for", self.attack[0]["attack"], "\n2) for", self.attack[1]["attack"])
                attack_type = input("you chose: ")
                if attack_type == "1":
                    damage = self.attack[0]["points"]
                    enemy.health -= damage
                elif attack_type == "2":
                    damage = self.attack[1]["points"]
                    enemy.health -= damage
                print("you made him lose:", damage)
                
            else:
                attack_type = random.choice(enemy.attack)
                print("he chose: ", attack_type)
                damage = attack_type["points"]
                self.health -= damage
                print(f"Enemy attacked with {attack_type['attack']} causing {damage} damage.")
                print(f"Your health is now {self.health}.")
            if random.random() > 0.5:
                self.strength += 10
                print(f"Your strength increased to {self.strength}.")
            else:
                enemy.strength += 15
                print(f"Enemy strength increased to {enemy.strength}.")

        if enemy.health <= 0:
            print("your enemy is dead")
            print("you won !")
            print("the quest you had to finish is now done")
            print("you finish your game with :", self.health, "health points\n", self.power, "power points\nand", self.strength, " strength points")
    
        if self.health <= 0:
            print("you lost...")
            print("come back next time when you're stronger!")

   
class Sorcerer(Perso): 
    #reaaalyy need to gérer le sorcerer ! TODO
    
    def __init__(self, name=None, health=100, inventory=None):
        super().__init__(name, health, inventory, role=self, silent=True)
        self.power=10
        #print("you chose to be a sorcerer")
    
    def find_ingredients(self):
        ingredient=["fire flower", "dragon tooth", "teary cloud", "ancient wooden fragment"]
        found=random.choice(ingredient)
        print("you found an ingredient: ",found)
        ramasse=input("do you want to take it?: 0)yes 1)no")
        if ramasse==0:
            self.inventory["ingredient"]=found
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
    #TODO find a way to stop from relooping each time before ending game?
    print("welcome to our world...")
    print("*"*70)
    print("here you can be anything you want, explore various places, discover new treasures, make potions and live the most vivacious adventures of all time")
    print("*"*70)
    print("first let's see who you are: ")
    choice=input("press\n1 to see your character\n2 to quit the game")
    
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
            enemy=Knight([{"points": 5, "attack": "punch"}, {"points": 15, "attack": "sword strike"}], 20, 20, "Enemio Enim", 100, {"weapon":"Katana"}, )
            print(place)
            kc1=input("press\n1 to explore Exola\n2 to check your inventory\n3 to find your enemy\n4 to quit the game")
            if kc1=="4":
                playing=False
            elif kc1=="2":
                person.check_inventory(person.inventory)
            elif kc1=="1":
                person.explore(place)
            elif kc1=="3":
                print("you found your biggest enemy", enemy.name.upper(), "...")
                #add more complexity here TODO
                #might even add a method of finding the enemy etc TODO
                print("he was waiting for you, to finally kill you...")
                person.role.combat(enemy)
            else:
                print("try again!")
        elif person.role.__class__.__name__ == 'Poet':
            print(f"Your quest as a poet is to explore the world, to collect words and create the most beautiful poem of the universe")
            place=Place("Belova", None, "Love", "POEM")
            print(place)
            pc1= input("now sweet little poet, what do you want to do ? press\n1 to explore Belova\n2 to search for words\n3 to check your inventory\n4 to quit the game")
            if pc1=="4":
                playing= False
            elif pc1=="1":
                person.explore(place)
            elif pc1=="2":
                person.role.search_for_words(place)
                pc11=input("do you want to press a poem?\n1 to start\n2to die because of your inexistant muse ")
                if pc11=="1":
                    writing=person.role.press(person.role.words)
                    print("the king found your poem and wants you to play it for him. NOW")
                    print("the king listens intensively...")
                    if writing is not None:
                        person.role.evaluate_poem(writing)
                elif pc11=="2":
                    print("you died miserably...")
                    print("poor little tortured poet")
                    playing=False
                else:
                    print("come again.-no that's what she said are tolerated")
            elif pc1=="3":
                person.check_inventory(person.inventory)
            else:
                print("hm i don't think i get it")
        elif person.role.__class__.__name__ == 'Sorcerer':
            print(f"Your quest as a sorcerer is to explore the world, to discover new ingredients and make the world's most dangerous potion")
            place=Place("Mordor", None, "Infinity Stone", "MAGIC")
            print(place)
            sc1=input("oh great sorcerer ! what would enchante your mind today?\n1 to explore Mordor\n2 to search for the missing ingredients for your potion\n3 to create a new secret potion\n4 to check your inventory\n 5 or to quit game")
            if sc1=="5":
                print("pouf, he disappeared")
                playing=False
            elif sc1=="1":
                person.role.explore(place)
            elif sc1=="2":
                person.role.find_ingredients()
            elif sc1=="3":
                person.role.make_new_potion(person.inventory)
            elif sc1=="4":
                person.check_inventory(person.inventory)
            else:
                print("huh?")
    else:
        print("try again\n")
    
    
    
