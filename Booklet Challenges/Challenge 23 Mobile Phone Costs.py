#Challenge 23
pics = int(input("How many photos do you want to send: "))
texts = int(input("How many texts do you want to send: "))
data = int(input("How many MBs data do you want to use: "))
#Gets user's phone usage
picsPrice = pics * 0.35
textsPrice = texts * 0.1
dataPrice = data * 0.05
#Turns the input into monetary values
total = picsPrice + textsPrice + dataPrice
#Adds the values together
if total < 10:
    print(f"Your total phone fee is ${total}.")
#If less than $10
else:
    print(f"Your total phone fee is ${total}, I recommend getting a contract.")
#If more than $10