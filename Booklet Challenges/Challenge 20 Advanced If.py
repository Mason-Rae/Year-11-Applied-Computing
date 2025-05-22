#Challenge 20
choice = input("Which home group are you in?")

choice = choice.lower()
if choice not in ("xb1", "xb2", "xb3", "xb4", "xk1", "xk2", "xk3", "xk4"):
#Checks if homegroup doesn't meet standards
    print("Sorry you have not madde a valid choice.")