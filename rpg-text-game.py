# press Python 3 code in this online editor and run it.
import random
#todo biggest is to stylize more and add ascii stuff
class Perso:
    
    def __init__(self, name=None, health=100, inventory=None, role=None, silent=False):
        if not silent:
            print("Hello new gamer!")
            print("\nPlease enter your information to start building your character")
            if name is None:
                name = input("Choose your name: ")
        self.name = name
        self.health = health
        if inventory is None:
            inventory = {}
        self.inventory = inventory
        if role is None:
            role = self.create_perso()
        self.role = role
        if not silent:
            print("Are you ready to play? let's start...\n")

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
            role= input("Choose the role you want to play with during this adventure: poet, sorcerer or knight? ")
            if role.lower()=="poet":
                return Poet(["sun", "life", "little", "good"])
            elif role.lower()=="knight":
                return Knight([{"points": 10, "attack": "daggers throw"}, {"points": 20, "attack": "knife thrust"},{"points":5, "attack":"counterattack"}, {"points": 15, "attack": "sword slash"}], 10, 10)
            elif role.lower()=="sorcerer":
                return Sorcerer()
            else:
                print("There is no place for a", role, "in our world. come back in another garment", self.name, "please\n")
            
    def explore(self, place):
        if place.name=="Exola":
            print("")
            print("You are exploring Exola, a vibrant kingdom with various interesting spots: an antique shop for old weapons, a flower boutique, and a farmer's market.")
            kc11 = input("press: \n 1 to visit the antique shop and acquire a weapon\n 2 to buy a romantic flower for your beloved\n 3 to grab some food from the market")
            if kc11 == "1":
                print("You bought a shiny new knife.")
                self.inventory["weapon"] = "knife"
                print("Knife added to your inventory.")
            elif kc11 == "2":
                print("You bought a fragrant petunia flower for your beloved.")
                self.inventory["extra"] = "petunia flower"
                print("Petunia flower added to your inventory.")
            elif kc11 == "3":
                print("You bought some fresh veggies and fish.")
                self.inventory["food"] = []
                self.inventory["food"].append("veggies")
                self.inventory["food"].append("fish")
                print("Veggies and fish added to your inventory.")
            else:
                print("Invalid choice, try again!")
            
        
        elif place.name=="Belova":
            print("You explore Belova, an enchanted place filled with magnificent scenes of life. You see lovers holding hands, children playing in gardens, and artists painting masterpieces")
            pc11 = input("press\n1 to listen to street musicians\n2 to watch painters at work\n3 to buy art souvenirs")
            if pc11 == "1":
                print("You listen to an enchanting melody that inspires your next poem.")
                if "inspiration" not in self.inventory:
                    self.inventory["inspiration"] = []
                if "souvenir" not in self.inventory:
                    self.inventory["souvenir"]=[]
                self.inventory["inspiration"].append("melody")
                print("Melody added to your inventory")
            elif pc11 == "2":
                print("You are watching a painter create a magnificent work of art.")
                self.inventory["inspiration"].append("art")
                print("Art inspiration added to your inventory")
            elif pc11 == "3":
                print("You are purchasing a wonderful souvenir to remember this city.")
                self.inventory["souvenir"] = "art piece"
                print("Art piece added to your inventory")
            else:
                print("Try again !")
                
                
        elif place.name=="Morder":
            print("You explore Mordor, a dangerous place filled with evil creatures and dark landscapes. You must be vigilant at every step.")
            sc11 = input("press:\n1 to explore a mysterious cave\n2 to search for rare ingredients in the dark forest\n3 to challenge a powerful creature\n4 to follow the cursed river\n5 to investigate the enchanted waterfall\n6 choose this to meet a friend\n")
            if "ingredients" not in self.inventory:
                self.inventory["ingredients"] = []
            if "trophy" not in self.inventory:
                self.inventory["trophy"]=[]
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
                found_ingredient = random.choice(["phoenix feather", "dragon scale", "nightingale song", "moonlight essence"])
                self.inventory["ingredients"].append(found_ingredient)
                print(f"{found_ingredient.capitalize()} added to your inventory")
                print("You hear someone whispering 'come back soon...'\n")
    
            elif sc11 == "5":
                print("You venture towards the melodious waterfall, where powerful energies and rare minerals await.")
                sc12 = input("press:\n1 to harvest stardust\n2 to look for a bat wing\n3 to collect some sparkling water\n ")
                
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
                    print("Try again wise ol' man.")
            elif sc11=="6":
                if "ingredients" not in self.inventory:
                    self.inventory["ingredients"] = []
                print("You hear an angelic voice say to your back, Mellon")
                print("\n You turn around, it's your old elf friend, Legolas, he smiles at you\n")
                print("You say, my dear Mellon, gen suilon, anann le u-gennin\n")
                print("He responds, suilad, i have been waiting for you.\n i have something for you, take this, he hands you a purse")
                print("You take the purse and look what's in it:\n")
                print("You find a flask of elf tears, rose petals and a newt's eye")
                print("Exactly what I was missing, rim hennaid, you told him")
                print("And go back to exploring and discovering more secrets of the world\n")
                self.inventory["ingredients"].append("elf tears")
                self.inventory["ingredients"].append("eye of newt")
                self.inventory["ingredients"].append("rose petals")
           
            else:
                print("Try again wise old man.")


    """ def take_treasure(place):
        pass
    
    def put_down_treasure(treasure):
        pass
    """
    def check_inventory(self,inventory):
        if self.inventory:
            print("You have: ", str(self.inventory), "in your inventory")
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
        print("Now going back to Belova")
            
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
        print("You have these words:", self.words, "\n and you have to write the best louange for the king or else you die")
        print("Think wise:")
        poem=input("")
        
        return poem
            
    def check_words(self, poem):
        poem_words=poem.split(" ")
        for word in poem_words:
           if word.lower() not in [w.lower() for w in self.words]:
                print("You used words beyond your power ")
                return False
        return True
        
        
    def evaluate_poem(self, poem):
        if poem is None or not self.check_words(poem):
            val = 0
        else:
            val = random.randint(1, 100)
        if val>50:
            print("By chance, the king loved it")
            print("You're fine, you're now called Jaskier and you sing for the king")
            print("Your quest is finished and you'll live a happy romantic life")
            return False
        elif val<50:
            print("The king decides that you'll soon be sentenced to death")
            print("You are dead")
            self.health=0
            print("You'll pass time by writing mourning poems about death and misery in the lambs")
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
                print("You can attack the enemy with", self.power, "power")
                print("Choose the attack to make him lose: 1) for", self.attack[0]["attack"], "\n2) for", self.attack[1]["attack"], "\n3) for", self.attack[2]["attack"],"\n4) for", self.attack[3]["attack"])
                attack_type = input("You chose: ")
                if attack_type == "1":
                    damage = self.attack[0]["points"]
                    enemy.health -= damage
                elif attack_type == "2":
                    damage = self.attack[1]["points"]
                    enemy.health -= damage
                elif attack_type =="3":
                    damage = self.attack[2]["points"]
                    enemy.health -= damage
                elif attack_type=="4":
                    damage = self.attack[3]["points"]
                    enemy.health -= damage
                else:
                    print("That attack is an illusion\n")
                print("You made him lose:", damage,"\n")
                
            else:
                attack_type = random.choice(enemy.attack)
                print("He chose: ", attack_type)
                damage = attack_type["points"]
                self.health -= damage
                print(f"Enemy attacked with {attack_type['attack']} causing {damage} damage.\n")
                print(f"Your health is now {self.health}.")
            if random.random() > 0.5:
                self.strength += 10
                print(f"Your strength increased to {self.strength}.\n")
            else:
                enemy.strength += 15
                print(f"Enemy strength increased to {enemy.strength}.\n")

        if enemy.health <= 0:
            print("Your enemy is dead")
            print("You won !")
            print("The quest you had to finish is now done")

        if self.health <= 0:
            print("You lost...")
            print("Come back next time when you're stronger!")

   
class Sorcerer(Perso): 

    def __init__(self, name=None, health=100, inventory=None):
        super().__init__(name, health, inventory, role=self, silent=True)
        self.power=10
        self.tried_potion = False 

    def find_ingredients(self):
        print("Let's see what our book of spells says")
        print("To see what ingredients you need for each potion, select the potion you wanna make and then you need to go explore Mordor to collect your missing ingredients\n")
        potions = [
            {"name": "immortality potion", "ingredients": ["magic crystal", "phoenix feather", "dragon scale"]},
            {"name": "filtre d'amour", "ingredients": ["rose petals", "nightingale song", "moonlight essence"]},
            {"name": "fairy elixir", "ingredients": ["stardust", "elf tears", "sparkling water"]},
            {"name": "witches brew", "ingredients": ["toadstool", "eye of newt", "bat wing"]}
        ]
        for i, potion in enumerate(potions, 1):
            print(f"{i}) {potion['name']}")
        try:
            selected_index = int(input("Select one by entering the corresponding number:\n"))
            if 1 <= selected_index <= len(potions):
                selected_potion = potions[selected_index - 1]
                print(f"You selected {selected_potion['name']}.")
                print("You'll need the following ingredients:")
                for ingredient in selected_potion["ingredients"]:
                    print(f"- {ingredient}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")
        """ingredient_options = ["fire flower", "dragon tooth", "teary cloud", "ancient wooden fragment"]
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
            """
    def make_new_potion(self, inventory):
        if self.tried_potion:
            return False
        
        potions = [
            {"name": "immortality potion", "ingredients": ["magic crystals", "phoenix feather", "dragon scale"]},
            {"name": "filtre d'amour", "ingredients": ["rose petals", "nightingale song", "moonlight essence"]},
            {"name": "fairy elixir", "ingredients": ["stardust", "elf tears", "sparkling water"]},
            {"name": "witches brew", "ingredients": ["toadstool", "eye of newt", "bat wing"]}
        ]

        print("What kind of potion do you want to make?")
        for i, potion in enumerate(potions, 1):
            print(f"{i}) {potion['name']}")

        choice = input("Enter the index of the potion you want to make: ")
        
        try:
            potion_index = int(choice) - 1
            if 0 <= potion_index < len(potions):
                selected_potion = potions[potion_index]
                required_ingredients = selected_potion["ingredients"]
                ingredient_count = {}
    
    
                for ingredient in inventory.get("ingredients", []):
                    if ingredient in ingredient_count:
                        ingredient_count[ingredient] += 1
                    else:
                        ingredient_count[ingredient] = 1
    
            
                can_create = True
                for ingredient in required_ingredients:
                    if ingredient_count.get(ingredient, 0) < required_ingredients.count(ingredient):
                        can_create = False
                        break
    
                if can_create:
                    potion_name = selected_potion["name"]
                    print(f"You successfully created a {potion_name}.")
                    
                    if "potions" not in inventory:
                        inventory["potions"] = []
                    inventory["potions"].append(potion_name)
                    self.tried_potion = True
                    return True
                else:
                    print("You don't have all the required ingredients.")
                    self.tried_potion = True 
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
        return f"You are currently in {self.name}\nThe quest here is: {self.quest}\nTreasure: {self.treasure if self.treasure else 'No treasure'}\nWords: {', '.join(self.words)}\n"
        """ print("you are currently in", self.name)
        print("the quest in here is:", self.quest)
        
        if self.treasure is not None:
            print("the treasure in here is:", self.treasure)"""
        
class Game:
    place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
    place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
    place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

    def __init__(self, person,file="save.json"):
        #print("New game")
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
        print("Welcome to our world...")
        print("*" * 69)
        print("Here you can be anything you want, explore various places, discover new treasures, make potions and live the most vivacious adventures of all time")
        print("*" * 69)
        print("First let's see who you are: ")

    def main_menu(self):
        while self.playing:
            choice = input("press: \n1 to see your character\n2 to quit the game\n")
            if choice == "2":
                self.quit_game()
            elif choice == "1":
                self.show_character()
                self.quest_menu()
            else:
                print("try again\n")

    def quit_game(self):
        print("Oh how sad, do you really want to leave us and go?")
        choice1 = input("Think wise, before we break into your computer :)\n yes \nor \nno?\n")
        if choice1.lower() == "yes":
            print("You suck. bye.")
            self.playing = False
        elif choice1.lower() == "no":
            print("You really don't know what you want.. pff goodbye anyway")
            self.playing = False
        else:
            print("What?")
            print("Sorry i take this as a yes :)")
            self.playing = False

    def show_character(self):
        print(self.person)
        print("\nHm we've got an interesting character here...\n")
        print("Now that you know who you are, you are given a quest to complete.")

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
        print("Your quest starts now")
        enemy = Knight([{"points": 5, "attack": "punch"}, {"points": 15, "attack": "sword strike"}], 20, 20, "Enemio Enim", 100, {"weapon": "Katana"})
        quest_finished = False
        while self.playing and not quest_finished:
            kc1 = input("press: \n1 to explore Exola\n2 to find your enemy\n3 to check your inventory\n4 to see the map\n5 to quit the game\n")
            if kc1 == "5":
                print("The courage has left the chat...")
                self.playing = False
            elif kc1 == "4":
                print(place_exo)
            elif kc1 == "3":
                self.person.check_inventory(self.person.inventory)
            elif kc1 == "1":
                self.person.explore(place_exo)
            elif kc1 == "2":
                print("You found your biggest enemy", enemy.name.upper(), "...")
                print("He was waiting for you, to finally kill you...")
                self.person.role.combat(enemy)
                self.finished_knight_quest()
                quest_finished = True
            else:
                print("Try again!")

    def finished_knight_quest(self):
        print("You finish your game with :", self.person.role.health, "health points\nand ", self.person.role.strength, " strength points")
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
            print("Next time, you'll do better knight", self.person.name)
        self.playing = False
        
    def poet_quest(self):
        place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
        place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
        place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

        print(f"Your quest as a poet is to explore the world, to collect words and create the most beautiful poem of the universe")
        quest_finished = False
        while self.playing and not quest_finished:
            pc1 = input("Now sweet little poet, what do you want to do ? press: \n1 to explore Belova\n2 to search for words\n3 to write a poem\n4 to check your words inventory\n5 to see your purse inventory\n6 to see the map\n7 to travel to a new place\n8 to quit the game\n")
            if pc1 == "8":
                print("Proceeds to flee quickly...")
                self.playing = False
            elif pc1 == "7":
                new_place=input("Where do you wanna go?\n")
                if new_place.lower()=="belova":
                    print("You are already there")
                elif new_place.lower()=="exola":
                    self.person.role.go_to(place_exo)
                elif new_place.lower()=="mordor":
                    self.person.role.go_to(place_mor)
                else:
                    print("There is no place called ", new_place )
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
                print("Hm i don't think i get it")
                
    def finished_poet_quest(self):
        dead=False
        pc11 = input("Do you want to write a poem?\n1 to start\n2 to die because of your inexistent muse\n")
        if pc11 == "1":
            writing = self.person.role.write(self.person.role.words)
            print("The king found your poem and wants you to play it for him. NOW")
            print("The king listens intensively...")
            if writing is not None:
              dead=self.person.role.evaluate_poem(writing)
        elif pc11 == "2":
            print("You died miserably...")
            print("Poor little tortured poet")
            dead=True
        else:
            print("Come again.")
        if not dead:
            dashes="-"*30
            dashes=dashes.center(60)
            print(dashes)
            print(f"Congratulations, poet {self.person.name}! you have successfully completed your quest POEM")
            print(dashes)
        self.playing = False

    def sorcerer_quest(self):
        place_exo = Place("Exola", "Enemio Enim", None, "COMBAT", ["bravery", "sword", "shield", "rapid", "kill"])
        place_belov = Place("Belova", None, "Love", "POEM", ["love", "beauty", "passion"])
        place_mor = Place("Mordor", None, "Infinity Stone", "MAGIC", ["magic", "power", "darkness", "blackmagic"])

        print(f"Your quest as a sorcerer is to explore the world, to discover new ingredients and make the world's most dangerous potion")
        quest_finished = False
        while self.playing and not quest_finished:
            sc1 = input("Oh great sorcerer ! what would enchant your mind today?\n1 to search for the missing ingredients for your potion\n2 to explore Mordor\n3 to create a new secret potion\n4 to check your inventory\n5 to see the map\n6 to quit game\n")
            if sc1 == "6":
                print("Pouf, he disappeared suddenly")
                self.playing = False
            elif sc1 == "5":
              print(place_mor)
            elif sc1 == "2":
                self.person.explore(place_mor)
            elif sc1 == "1":
                self.person.role.find_ingredients()
            elif sc1 == "3":
                self.person.role.make_new_potion(self.person.inventory)
                self.finished_sorcerer_quest()
                quest_finished = True
            elif sc1 == "4":
                self.person.check_inventory(self.person.inventory)
            else:
                print("huh?")
    
    def finished_sorcerer_quest(self):
        if self.person.role.make_new_potion(self.person.inventory):
            dashes="-"*30
            dashes=dashes.center(60)
            print(dashes)
            print(f"Congratulations, Sorcerer {self.person.name}! You have successfully completed your quest MAGIC")
            print(dashes)
        else:
            print("Next time, try again wise man!")
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

