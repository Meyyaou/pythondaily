import random
print("welcome to our first mini python game")
print("*"*50)
print("----------the game is number guesser!----------")
play=input("say yes if you wanna play?")
number= random.randint(1, 1000)
att=5
if play=="no":
    print("goodbye then!")
elif play!="no" and play!="yes":
    print("i dont understand?")
elif play=="yes":
    print("you have 5 attempts...")
    print("guess a number between 1 and 1000:")
    guess= int(input("your guess: "))
    att-=1
    win=False
    while att > 0 and win==False:
        if guess < number:
            guess = int(input("guessed too low, try again: "))
            att-=1
        if guess > number:
            guess = int(input("guessed too high, try again: "))
            att-=1
        if guess == number:
            win=True
            print("YOU WIN !")
    
    if win==False:
        print("YOU LOSE !")
        print(f"the number was {number}")
