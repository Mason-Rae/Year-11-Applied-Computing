#SAC 2
def add_to_dict_keep_old(report, key, value):
    if key in report:
        report[key].append(value)
        #Adds on if the key(student name) was already in the file
    else:
        report[key] = [value]
        #Creates a new section for the student
    return report
#Def to add all the values into the dictionary

report = {}
#Dictionary base

students = int(input("How many students in the class: "))
#Gets the amount of students in the class
while True:
    classes = int(input("From 1 to 5, how many classes that week: "))
    if classes in range(1,6):
        break
    print("Please enter correctly")
#Has classes ensured it matches whats required
print("")
#Seperates to look cleaner

for i in range(1, students+1):
#Creates the loop to go through every stundent's classes and name
    name = input(f"What was the name student {i}: ")
    name = name.capitalize()
    #Gets student's name and auto capitalises
    while True:
        if classes >= 1:
            class1 = input(f"Was {name} present for period 1(P/A): ")
            class1 = class1.lower()
            if class1 == "p":
                class1 = 1
            elif class1 == "a":
                class1 = 0
        #Gets the answer for class 1 and sorts response into correct values, if matched
        if classes >= 2:
            class2 = input(f"Was {name} present for period 2(P/A): ")
            class2 = class2.lower()
            if class2 == "p":
                class2 = 1
            elif class2 == "a":
                class2 = 0
        #Gets the answer for class 2 and sorts response into correct values, if matched
        if classes >= 3:
            class3 = input(f"Was {name} present for period 3(P/A): ")
            class3 = class3.lower()
            if class3 == "p":
                class3 = 1
            elif class3 == "a":
                class3 = 0
        #Gets the answer for class 3 and sorts response into correct values, if matched
        if classes >= 4:
            class4 = input(f"Was {name} present for period 4(P/A): ")
            class4 = class4.lower()
            if class4 == "p":
                class4 = 1
            elif class4 == "a":
                class4 = 0
        #Gets the answer for class 4 and sorts response into correct values, if matched
        if classes >= 5:
            class5 = input(f"Was {name} present for period 5(P/A): ")
            class5 = class5.lower()
            if class5 == "p":
                class5 = 1
            elif class5 == "a":
                class5 = 0
        #Gets the answer for class 5 and sorts response into correct values, if matched
                
        match classes:      
            case 5:
                if (class1 and class2 and class3 and class4 and class5) in (1, 0):
                    ave = (class1 + class2 + class3 + class4 + class5)/5
                    break
            case 4:
                if (class1 and class2 and class3 and class4) in (1, 0):
                    ave = (class1 + class2 + class3 + class4)/4
                    break
            case 3:
                if (class1 and class2 and class3) in (1, 0):
                    ave = (class1 + class2 + class3)/3
                    break
            case 2:
                if (class1 and class2) in (1, 0):
                    ave = (class1 + class2)/2
                    break
            case 1:
                if class1 in (1, 0):
                    ave = class1
                    break
        #Depending on the amount of classes as to which if is triggered
            
        print("Repeat, something was wrong")
        print("")
        #Incase of emergency, guider
        
    classesPresent = ave*classes
    classesPresent = int(classesPresent)
    #Reverts back to total amounts of attended classes
    ave = ave*100
    #Puts the average into a percentage

    report = add_to_dict_keep_old(report, name, ave)
    #Sends the results to the def to add to the dictionary
    
    print("")
    #Makes code cleaner for the user

attendanceRecords = open("AttendanceRecords.txt", "wt")

print("Attendance Report:")
#Title
for key, value in report.items():
#Repeats so everything can come out one at a time
    value = value.pop()
    value = int(value)
    #Takes the value outside its dictionary
    if value > 75:
        if classesPresent == 1:
            print(f"{key}: {classesPresent} period present ({value}%)")
        else:
            print(f"{key}: {classesPresent} periods present ({value}%)")
    else:
        if classesPresent == 1:
            print(f"{key}: {classesPresent} period present ({value}%) - Warning: Low attendence")
        else:
            print(f"{key}: {classesPresent} periods present ({value}%) - Warning: Low attendence")
    #Prints depending on if attendance passes a specific number and whether or not the amount of attended classes is 1 or not
    
    attendanceRecords.write(f"{key} : {value}% attendance")
    attendanceRecords.write("\n")
    #Adds results into a file
print("Data written to file.")
#Lets user know that the data was stored
attendanceRecords.close()