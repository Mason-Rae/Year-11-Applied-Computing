#Challenge 8
name = input("Whats your name: ")
age = int(input("In years, how old are you: "))
#Gets name and age
days = age * 365
#Finds days old
print(f"You are roughly {days} days old.")
hours = days * 24
#Finds hours old
print(f"You are roughly {hours} hours old.")

minutes = hours * 60
#Finds minutes old
print(f"You are roughly {minutes} minutes old.")

seconds = minutes * 60
#Finds seconds old
print(f"You are roughly {seconds} seconds old.")