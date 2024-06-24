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
        if place.name=="Exola":
            print("You are exploring Exola, a vibrant kingdom with various interesting spots: an antique shop for old weapons, a flower boutique, and a farmer's market.")
            kc11 = input("press\n 1 to visit the antique shop and acquire a weapon\n 2 to buy a romantic flower for your beloved\n 3 to grab some food from the market")
            if kc11 == "1":
                print("you bought a shiny new knife.")
                self.inventory["weapon"] = "knife"
                print("knife added to your inventory.")
            elif kc11 == "2":
                print("you bought a fragrant petunia flower for your beloved.")
                self.inventory["extra"] = "petunia flower"
                print("petunia flower added to your inventory.")
            elif kc11 == "3":
                print("you bought some fresh veggies and fish.")
                self.inventory["food"] = []
                self.inventory["food"].append("veggies")
                self.inventory["food"].append("fish")
                print("veggies and fish added to your inventory.")
            else:
                print("Invalid choice, try again!")
            
        
        elif place.name=="Belova":
            print("you explore Belova, an enchanted place filled with magnificent scenes of life. You see lovers holding hands, children playing in gardens, and artists painting masterpieces")
            pc11 = input("press\n1 to listen to street musicians\n2 to watch painters at work\n3 to buy art souvenirs")
            if pc11 == "1":
                print("you listen to an enchanting melody that inspires your next poem.")
                self.inventory["inspiration"] = []
                self.inventory["inspiration"].append("melody")
                print("Melody added to your inventory")
            elif pc11 == "2":
                print("you are watching a painter create a magnificent work of art.")
                self.inventory["inspiration"].append("art")
                print("Art inspiration added to your inventory")
            elif pc11 == "3":
                print("you are purchasing a wonderful souvenir to remember this city.")
                self.inventory["souvenir"] = "art piece"
                print("Art piece added to your inventory")
            else:
                print("try again !")
        elif place.name=="Morder":
            print("You explore Mordor, a dangerous place filled with evil creatures and dark landscapes. You must be vigilant at every step.")
        sc11 = input("Press:\n1 to explore a mysterious cave\n2 to search for rare ingredients in the dark forest\n3 to challenge a powerful creature\n4 to follow the cursed river\n5 to investigate the enchanted waterfall\n6 choose this to meet a friend")
    
        if sc11 == "1":
            print("You find a cave filled with magic crystals.")
            self.inventory["ingredients"].append("magic crystals")
            print("Magic crystals added to your inventory")
    
        elif sc11 == "2":
            print("You find rare and powerful toadstool in the forest.")
            self.inventory["ingredients"].append("toadstool")
            print("Toadstool added to your inventory")
    
        elif sc11 == "3":
            print("You challenge a powerful creature and earn a reward.")
            self.inventory["trophy"].append("creature trophy")
            print("Creature trophy added to your inventory")
        elif sc11 == "4":
            print("You follow the mystic path of the river and find:")
            found_ingredient = random.choice(["phoenix feather", "dragon scale", "rose petals", "nightingale song", "moonlight essence"])
            self.inventory["ingredients"].append(found_ingredient)
            print(f"{found_ingredient.capitalize()} added to your inventory")
            print("you hear someone whispering 'come back soon...'\n")

        elif sc11 == "5":
            print("you venture towards the melodious waterfall, where powerful energies and rare minerals await.")
            sc12 = input("Press:\n1 to harvest stardust\n2 to look for a bat wing\n3\nto collect some sparkling water\n ")
            
            if sc12 == "1":
                print("You try and harvset some colorful stardust.")
                self.inventory["ingredients"].append("stardust")
                print("Stardust added to your inventory")
            
            elif sc12 == "2":
                print("You find a bat wing hanging by a tree next to the waterfall.")
                self.inventory["ingredients"].append("bat wing")
                print("Bat wing added to your inventory")
            elif sc12=="3":
                print("You collect some shiny sparkling water.")
                self.inventory["ingredients"].append("sparkling water")
                print("Sparkling water added to your inventory")
            else:
            print("try again wise ol' man.")
        elif sc11=="6":
            print("you hear an angelic voice say to your back, Mellon")
            print("\n you turn around, it's your old elf friend, Legolas, he smiles at you\n")
            print("you say, my dear Mellon, gen suilon, anann le u-gennin")
            print("he responds, suilad, i have been waiting for you.\n i have something for you, take this,\n he hands you a purse")
            print("you take the purse and look what's in it:\n")
            print("you find a flask of elf tears\n and a newt's eye")
            print("exactly what I was missing, rim hennaid")
            self.inventory["ingredients"].append("elf tears")
            self.inventory["ingredients"].append("eye of newt")
       
        else:
            print("try again wise old man.")


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

    def go_to(self, place):
        if place.name=="Belova":
            print("--- Exploring Belova ---")
        elif place.name=="Exola":
            print("--- Exploring Exola ---")
        elif place.name=="Mordor":
            print("--- Exploring Mordor ---")
        
        self.search_for_words(place)
        print("now going back to Belova")
            
    def search_for_words(self, place):
        print(f"Searching for words in {place.name}...")
        if not place.words:
            print("You found no words.")
        else:
            found_word = random.choice(place.words)
            print(f"You found the word: {found_word}")
            self.words.append(found_word)
            place.words.remove(found_word)

    def write(self, words):
        print("you have these words:", self.words, "\n and you have to write the best louange for the king or else you die")
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
            return False
        elif val<50:
            print("the king decides that you'll soon be sentenced to death")
            print("you are dead")
            self.health=0
            print("you'll write mourning poems about death in the lambs")
            return True
                
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

        if self.health <= 0:
            print("you lost...")
            print("come back next time when you're stronger!")

   
class Sorcerer(Perso): 
    #reaaalyy need to gérer le sorcerer ! TODO
    
    def __init__(self, name=None, health=100, inventory=None):
        super().__init__(name, health, inventory, role=self, silent=True)
        self.power=10
        self.tried_potion = False 

    def find_ingredients(self):
        ingredient_options = ["fire flower", "dragon tooth", "teary cloud", "ancient wooden fragment"]
        found = random.choice(ingredient_options)
        print("you found an ingredient:", found)
        ramasse = input("do you want to take it? (yes or no): ")
        if ramasse == "yes":
            if "ingredients" not in self.inventory:
                self.inventory["ingredients"] = []
            self.inventory["ingredients"].append(found)
            print("you added", found, "to your inventory.\n")
        else:
            print("you decided not to take the ingredient.\n")
            
    def make_new_potion(self):
        if self.tried_potion:
            return False
        
        potions = [
            {"name": "immortality potion", "ingredients": ["magic crystal", "phoenix feather", "dragon scale"]},
            {"name": "filtre d'amour", "ingredients": ["rose petals", "nightingale song", "moonlight essence"]},
            {"name": "fairy elixir", "ingredients": ["stardust", "elf tears", "sparkling water"]},
            {"name": "witches brew", "ingredients": ["toadstool", "eye of newt", "bat wing"]}
        ]

        print("What kind of potion do you want to make?")
        for i, potion in enumerate(potions, 1):
            print(f"{i}) {potion['name']}")

        choice = input("Enter the number of the potion you want to make: ")
        
        try:
            potion_index = int(choice) - 1
            if 0 <= potion_index < len(potions):
                selected_potion = potions[potion_index]
                required_ingredients = selected_potion["ingredients"]
                if all(ingredient in self.inventory.get("ingredients", []) for ingredient in required_ingredients):
                    potion_name = selected_potion["name"]
                    print(f"You successfully created a {potion_name}.")
                    for ingredient in required_ingredients:
                        self.inventory["ingredients"].remove(ingredient)
                    
                    if "potions" not in self.inventory:
                        self.inventory["potions"] = []
                    self.inventory["potions"].append(potion_name)
                    self.tried_potion = True  # Set the flag to True after successfully making a potion
                    return True
                else:
                    print("You don't have all the required ingredients.")
                    self.tried_potion = True  # Set the flag to True even if the attempt failed
                    return False
            else:
                print("Invalid choice.")
                return False
        except ValueError:
            print("Invalid input. Please enter a number.")
            return False
        
class Enemy():
    pass
class NPC():
    pass
class Place():
    def __init__(self, name=None, enemy=None, treasure=None, quest=None, words=None):
        self.name=name
        self.enemy=enemy
        self.treasure=treasure
        self.quest=quest
        self.words = words
        
    def __str__(self):
        #todo gotta add more style
        return f"You are currently in {self.name}\nThe quest here is: {self.quest}\nTreasure: {self.treasure if self.treasure else 'No treasure'} Words: {', '.join(self.words)}\n"
        """ print("you are currently in", self.name)
        print("the quest in here is:", self.quest)
        
        if self.treasure is not None:
            print("the treasure in here is:", self.treasure)"""
        
class Game:
    place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
    place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
    place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

    def __init__(self, person,file="save.json"):
        print("New game")
        self.file=file
        self.load_game()
        self.person = person
        self.playing = True

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
    
    def start_game(self):
        print("welcome to our world...")
        print("*" * 69)
        print("here you can be anything you want, explore various places, discover new treasures, make potions and live the most vivacious adventures of all time")
        print("*" * 69)
        print("first let's see who you are: ")

    def main_menu(self):
        while self.playing:
            choice = input("press\n1 to see your character\n2 to quit the game\n")
            if choice == "2":
                self.quit_game()
            elif choice == "1":
                self.show_character()
                self.quest_menu()
            else:
                print("try again\n")

    def quit_game(self):
        print("oh how sad, do you really want to leave us and go?")
        choice1 = input("think wise, before we break into your computer :)\n yes \nor \nno?\n")
        if choice1.lower() == "yes":
            print("you suck. bye.")
            self.playing = False
        elif choice1.lower() == "no":
            print("you really don't know what you want.. pff goodbye anyway")
            self.playing = False
        else:
            print("what?")
            print("sorry i take this as a yes :)")
            self.playing = False

    def show_character(self):
        print(self.person)
        print("\nhm we've got an interesting character here...\n")
        print("now that you know who you are, you are given a quest to complete.")

    def quest_menu(self):
        if self.person.role.__class__.__name__ == 'Knight':
            self.knight_quest()
        elif self.person.role.__class__.__name__ == 'Poet':
            self.poet_quest()
        elif self.person.role.__class__.__name__ == 'Sorcerer':
            self.sorcerer_quest()
        else:
            print("Unknown role. Cannot assign quest.")

    def knight_quest(self):
        place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
        print("Your quest as a knight is to explore the world, to find an enemy and to combat it.")
        print("your quest starts now")
        enemy = Knight([{"points": 5, "attack": "punch"}, {"points": 15, "attack": "sword strike"}], 20, 20, "Enemio Enim", 100, {"weapon": "Katana"})
        quest_finished = False
        while self.playing and not quest_finished:
            kc1 = input("press\n1 to explore Exola\n2 to find your enemy\n3 to check your inventory\n4 to see the map\n5 to quit the game\n")
            if kc1 == "5":
                print("the courage has left the chat...")
                self.playing = False
            elif kc1 == "4":
                print(place_exo)
            elif kc1 == "3":
                self.person.check_inventory(self.person.inventory)
            elif kc1 == "1":
                self.person.explore(place_exo)
            elif kc1 == "2":
                print("you found your biggest enemy", enemy.name.upper(), "...")
                print("he was waiting for you, to finally kill you...")
                self.person.role.combat(enemy)
                self.finished_knight_quest()
                quest_finished = True
            else:
                print("try again!")

    def finished_knight_quest(self):
        print("you finish your game with :", self.person.role.health, "health points\nand ", self.person.role.strength, " strength points")
        if self.person.role.health>0:
            dashes="-"*30
            dashes=dashes.center(60)
            print(dashes)
            con=f"Congratulations, Knight {self.person.name} !"
            msg= "You have successfully completed your quest COMBAT"
            con=con.center(80)
            msg=msg.center(80)
            print(con)
            print(msg)
            print(dashes)
        else: 
            print("next time, you'll do better knight", self.person.name)
        self.playing = False
        
    def poet_quest(self):
        place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
        place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
        place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

        print(f"Your quest as a poet is to explore the world, to collect words and create the most beautiful poem of the universe")
        quest_finished = False
        while self.playing and not quest_finished:
            pc1 = input("now sweet little poet, what do you want to do ? press\n1 to explore Belova\n2 to search for words\n3 to write a poem\n4 to check your words inventory\n5 to see your purse inventory\n6 to see the map\n7 to travel to a new place\n8 to quit the game\n")
            if pc1 == "8":
                print("proceeds to flee quickly...")
                self.playing = False
            elif pc1 == "7":
                new_place=input("where do you wanna go?\n")
                if new_place.lower()=="belova":
                    print("you are already there")
                elif new_place.lower()=="exola":
                    self.person.role.go_to(place_exo)
                elif new_place.lower()=="mordor":
                    self.person.role.go_to(place_mor)
                else:
                    print("there is no place called ", new_place )
            elif pc1 == "5":
                self.person.check_inventory(self.person.inventory)
            elif pc1 == "6":
                print(place_belov)
            elif pc1 == "1":
                self.person.explore(place_belov)
            elif pc1 == "2":
                self.person.role.search_for_words(place_belov)
            elif pc1 == "3":
                self.finished_poet_quest()
                quest_finished = True
            elif pc1 == "4":
                print(self.person.role.words)
            else:
                print("hm i don't think i get it")
                
    def finished_poet_quest(self):
        dead=False
        pc11 = input("do you want to write a poem?\n1 to start\n2 to die because of your inexistent muse\n")
        if pc11 == "1":
            writing = self.person.role.write(self.person.role.words)
            print("the king found your poem and wants you to play it for him. NOW")
            print("the king listens intensively...")
            if writing is not None:
              dead=self.person.role.evaluate_poem(writing)
        elif pc11 == "2":
            print("you died miserably...")
            print("poor little tortured poet")
            dead=True
        else:
            print("come again.")
        if not dead:
            dashes="-"*30
            dashes=dashes.center(60)
            print(dashes)
            print(f"congratulations, poet {self.person.name}! you have successfully completed your quest POEM")
            print(dashes)
        self.playing = False

    def sorcerer_quest(self):
        place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
        place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
        place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

        print(f"Your quest as a sorcerer is to explore the world, to discover new ingredients and make the world's most dangerous potion")
        quest_finished = False
        while self.playing and not quest_finished:
            sc1 = input("oh great sorcerer ! what would enchant your mind today?\n1 to explore Mordor\n2 to search for the missing ingredients for your potion\n3 to create a new secret potion\n4 to check your inventory\n5 to see the map\n6 to quit game\n")
            if sc1 == "6":
                print("pouf, he disappeared suddenly")
                self.playing = False
            elif sc1 == "5":
              print(place_mor)
            elif sc1 == "1":
                self.person.explore(place_mor)
            elif sc1 == "2":
                self.person.role.find_ingredients()
            elif sc1 == "3":
                self.person.role.make_new_potion()
                self.finished_sorcerer_quest()
                quest_finished = True
            elif sc1 == "4":
                self.person.check_inventory(self.person.inventory)
            else:
                print("huh?")
    
    def finished_sorcerer_quest(self):
        if self.person.role.make_new_potion():
            dashes="-"*30
            dashes=dashes.center(60)
            print(dashes)
            print(f"congratulations, Sorcerer {self.person.name}! You have successfully completed your quest MAGIC")
            print(dashes)
        else:
            print("next time, try again wise man!")
        self.playing = False


person=None
if person is None :
    name=None
    role=None
    health= 100
    strength=10
    inventory={}
    person=Perso(name, health, inventory, role)
game = Game(person)
game.start_game()
game.main_menu()


