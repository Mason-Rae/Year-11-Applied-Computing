#Challenge 22
happy = int(input("On a scale of 1-10 how happy are you: "))
if happy <= 3:
    print("Cheer up, i'm sure everything will go your way.")
#If happy is 3 or under
elif happy in (4,5,6,7):
    print("I'm glad your day is well, but make sure you have your own time.")
#If happy is from 4-7
else:
    print("Well done having a great day, keep it up.")