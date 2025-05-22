#Challenge 16
bill = float(input("What was the dinner bill: $"))
#Gets dinner price
tipIncluded = bill*1.15
#Includes a 15% tip
Split = tipIncluded / 2
#Halfs the total price
print("Splitting by half, you two each pay ", "%0.2f"%(Split))