#Chapter 16 Harder
people = int(input("How many people are eating dinner: "))
bill = float(input("What was the price of dinner: $"))
tip = int(input("How much do you want to tip by: "))
tip = (tip / 100) + 1
#Gets tip
tipIncluded = bill * tip
#Gets total price
split = tipIncluded / people
#split per person
print(f"Altogether it is","$%0.2f"%(split), "each.")
distance = float(input("How far do you live(in km): "))
taxiPrice = distance * 0.45
#Calculates a taxi
print(f"That taxi has cost you ${taxiPrice}")
overall = tipIncluded + (taxiPrice * people)
perPerson = split + taxiPrice
#The total and per person price
print(f"The overall price is ","$%0.2f"%(overall),"and the individual price is ","$%0.2f."%(perPerson))