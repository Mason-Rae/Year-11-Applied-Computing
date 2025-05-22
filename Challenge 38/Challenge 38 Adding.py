#Challenge 38 Adding
myFile = open("example.txt", "at")
#Opens file
print("Enter 4 numbers:")
myList = [int(input("")), int(input("")), int(input("")), int(input(""))]
#Has user enter the 4 numbers
for item in myList:
    myFile.write(f"{item}\n")

myFile.close()
#Closes file

myFile = open("example.txt", "rt")
myList = []
#Gets the file and creats a dictionary to store it
for line in myFile:
    myList.append(line)
myFile.close()
#Uploads the file items into the dictionary
num10 = int(myList.pop())
num9 = int(myList.pop())
num8 = int(myList.pop())
num7 = int(myList.pop())
num6 = int(myList.pop())
num5 = int(myList.pop())
num4 = int(myList.pop())
num3 = int(myList.pop())
num2 = int(myList.pop())
num1 = int(myList.pop())
#Moves the numbers into variables
mean = (num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)/10
print(f"The mean average of the file is", "%0.2f"%(mean))
#Gets the mean and prints it