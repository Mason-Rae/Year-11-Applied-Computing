#Challenge 31
import random
import time
print("Lets play Rock, Paper, Scissors")
#Tells user the game

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
#Code answers

codeWins = 0
userWins = 0
tie = 0
#Winners

while True:
    games = int(input("How many games from 3-10: "))
    if games in range(3,10):
        break
    print("Please enter from 3-10")
    #Gets user game amount
for number in range(0, games, 1):
    print("game", number+1)
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
            tie += 1
            #Adds 1 to tie
        elif user == "paper":
            print("You win, good game.")
            userWins +=1
            #Adds 1 to userWins
        else:
            print("You lose, good game.")
            codeWins +=1
            #Adds 1 to codeWins
        #Options depending on user
    elif choice == 2:
    #Paper
        print("I choose paper")
        time.sleep(0.25)
        #Delay 0.25s
        if user == "paper":
            print("Tie, good game.")
            tie += 1
            #Adds 1 to tie
        elif user == "scissors":
            print("You win, good game.")
            userWins +=1
            #Adds 1 to userWins
        else:
            print("You lose, good game.")
            codeWins +=1
            #Adds 1 to codeWins
        #Options depending on user
    else:
    #Scissors
        print("I choose scissors")
        time.sleep(0.25)
        #Delay 0.25s
        if user == "scissors":
            print("Tie, good game.")
            tie += 1
            #Adds 1 to tie
        elif user == "rock":
            print("You win, good game.")
            userWins +=1
            #Adds 1 to userWins
        else:
            print("You lose, good game.")
            codeWins +=1
            #Adds 1 to codeWins
        #Options depending on user
    time.sleep(1)
print(f"I won {codeWins} times \nYou won {userWins} times \nWe tied {tie} times")
#Prints overall scores
time.sleep(0.5)
if codeWins > userWins and codeWins > tie:
    print("I win overall, good game.")
elif userWins > codeWins and userWins > tie:
    print("You win overall, good game.")
else:
    print("We tied, good game.")
#Highest outcome
    