#Challenge 31
import random
import time
print("Lets play Rock, Paper, Scissors")
#Tells user the game

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
#Code answers

while True:
    user = input("Rock, Paper, Scissors: ")
    user = user.lower()
    if user in ("rock", "paper", "scissors"):
        break
    print("Please enter correctly.")
    #Has user enter "rock" "paper" or "scissors"
choice = random.randint(1,3)
if choice == 1:
#Rock
    print("I choose rock")
    time.sleep(0.25)
    #Delay 0.25s
    if user == "rock":
        print("Tie, good game.")
    elif user == "paper":
        print("You win, good game.")
    else:
        print("You lose, good game.")
    #Options depending on user
elif choice == 2:
#Paper
    print("I choose paper")
    time.sleep(0.25)
    #Delay 0.25s
    if user == "paper":
        print("Tie, good game.")
    elif user == "scissors":
        print("You win, good game.")
    else:
        print("You lose, good game.")
    #Options depending on user
else:
#Scissors
    print("I choose scissors")
    time.sleep(0.25)
    #Delay 0.25s
    if user == "scissors":
        print("Tie, good game.")
    elif user == "rock":
        print("You win, good game.")
    else:
        print("You lose, good game.")
    #Options depending on user
    