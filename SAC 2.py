#SAC 2
students = int(input("How many students in the class: "))
#Gets the amount of students in the class
for i in range(1, students+1):
    globals()[f"name_{i}"] = input("Student's name: ")
    #Uses a for loop to create variables to store the names
    periods = int(input("Number of periods that week(1-5): "))
    while periods not in range(1,5):
        periods = int(input("Number of periods that week(1-5): "))
    for j in range(1, periods+1):
        globals()[f"period{j}_{i}"]= input(f"Enter attendence for period {j}(P/A): ").lower()
    #Has 'Present' or 'Absent' entered for the periods
    
