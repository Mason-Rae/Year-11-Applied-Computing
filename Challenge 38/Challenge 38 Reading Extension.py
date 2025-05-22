#Challenge 38 Reading Extension
myFile = open("example.txt", "rt")
myList = []
#Gets the file and creats a dictionary to store it
for line in myFile:
    myList.append(line)
myFile.close()
#Uploads the file items into the dictionary
num6 = int(myList.pop())
num5 = int(myList.pop())
num4 = int(myList.pop())
num3 = int(myList.pop())
num2 = int(myList.pop())
num1 = int(myList.pop())
#Puts the numbers into their own variables
sorter = [num6, num5, num4, num3, num2, num1]
print("The mean of",sorted(sorter), "is:")
#Sorts the numbers provided
mean = (num1+num2+num3+num4+num5+num6)/6
print(f"The mean average of the file is", "%0.2f"%(mean))
#Gets the mean and prints it

