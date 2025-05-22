#Challenge 38 Writing
myFile = open("example.txt", "wt")
#opens the file for the input
print("Enter 6 numbers:")
myList = [int(input("")), int(input("")), int(input("")), int(input("")), int(input("")), int(input(""))]
#Has user enter the 6 numbers
for item in myList:
    myFile.write(f"{item}\n")
    #Adds the numbers to example.txt
myFile.close()