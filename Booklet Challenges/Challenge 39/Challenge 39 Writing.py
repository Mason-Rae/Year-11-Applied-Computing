#Challenge 39
myFile = open("example2.txt", "wt")
#Gets the ability to write in the file
print("Name, Height(2 digits), Weight(3 digit decimal):")
people = ["James", 73, 1.82, "Peter", 78, 1.80, "Jay", 75, 1.79, "Beth", 65, 1.53, "Mags", 66, 1.50, "Joy", 62, 1.34]
#Has the dicionary store to upload
for item in people:
    myFile.write(f"{item}")
    myFile.write("\n")
myFile.close()