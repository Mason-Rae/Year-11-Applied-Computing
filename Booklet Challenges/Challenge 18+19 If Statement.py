#Challenge 18+19
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#User's two numbers
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print(num1, "is equal to", num2)