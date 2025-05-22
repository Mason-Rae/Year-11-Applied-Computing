#Secret Challenge
money = float(input("How much money did you bring to school today: $"))
#Total money
spent = float(input("How much did you spend on lunch today: $"))
#Money spent
moneyLeft = money-spent
if moneyLeft < 0:
    print("You're in debt")
#Under $0
else:
    print(f"You have ${moneyLeft} left over.")
#Over $0
