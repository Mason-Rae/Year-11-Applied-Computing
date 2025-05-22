#Challenge 39 Reading
myFile = open("example2.txt", "rt")
#Gets and reads the file
people = []
for line in myFile:
    people.append(line)
#Transfers file into dictionary
weight1 = float(people.pop())
height1 = int(people.pop())
name1 = people.pop()
weight2 = float(people.pop())
height2 = int(people.pop())
name2 = people.pop()
weight3 = float(people.pop())
height3 = int(people.pop())
name3 = people.pop()
weight4 = float(people.pop())
height4 = int(people.pop())
name4 = people.pop()
weight5 = float(people.pop())
height5 = int(people.pop())
name5 = people.pop()
weight6 = float(people.pop())
height6 = int(people.pop())
name6 = people.pop()
#Transfers the dictionary into variables 

print(f"{name1}{height1} tall : weighs {weight1}")
print(f"{name2}{height2} tall : weighs {weight2}")
print(f"{name3}{height3} tall : weighs {weight3}")
print(f"{name4}{height4} tall : weighs {weight4}")
print(f"{name5}{height5} tall : weighs {weight5}")
print(f"{name6}{height6} tall : weighs {weight6}")
#Prints it per person
myFile.close()