#Chapter 16 Harder
people = int(input("How many people are eating dinner: "))
#Gets number of people
bill = float(input("What was the price of dinner: $"))
#Gets dinner price
tip = int(input("How much do you want to tip by: "))
tip = (tip / 100) + 1
#Gets and calculates tip price
tipIncluded = bill * tip
#Makes total price
split = tipIncluded / people
#Splits it
print(f"Altogether it is","$%0.2f"%(split), "each.")
#Prints output