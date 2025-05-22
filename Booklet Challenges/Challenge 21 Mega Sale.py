#Challenge 21
money = float(input("How much money did you spend at the shop today: $"))
#User's money spent

if money > 20:
    print("You are eligible to a $3 voucher.")
#Tells the user they get a #3 voucher for spending more than $20
elif money > 10:
    print("You are eligible to a $1 voucher.")
#If the user spends less than $20 but more than $10
else:
    print("Sorry, you are not eligible for a voucher.")