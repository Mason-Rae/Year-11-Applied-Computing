#Challenge 3-5
num1 = float(input("Enter a number between 1-10: "))
#Gets a number
while True:
    if num1 >= 1 and num1 <= 10:
        break
    #Breaks the loop
    else:
        num1 = float(input("Between 1-10 please: "))
    #Makes the user repeat until correct
#Runs a loop for the right set
        
num2 = float(input("Enter a number between 1-10: "))
#Gets another number
while True:
    if num2 >= 1 and num1 <= 10:
        break
    #Breaks the loop
    else:
        num2 = float(input("Between 1-10 please: "))
        #Makes the user repeat until correct
#Runs a loop for the right set
print(num1 + num2)
#Prints the numbers