#Challenge 6
name = input("Your full name please: ")
#Gets user's name
print(f"{name}'s calorie counter")
#The title
calories = int(input("How many calories have you had today: "))

s= 2000 - calories
#Finds difference to max calories for the day
if s > 0:
    print(f"You can eat {s} more calories today")
#Prints if under maximum calories
elif s < 0:
    print(f"You've eaten over {s} calories for today")
#Prints if over maximum calories
else:
    print("You've had all your calories for today")
#Prints if on maximum calories