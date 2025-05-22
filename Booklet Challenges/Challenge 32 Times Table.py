#Challenge 32
import time
for i in range(1,13):
    #Gets the first number
    print(i, "Times table\n")
    for j in range(1,13):
        #Gets the second number
        print(f"{i} times {j} =", i*j, end=", ")
        #Multiplies them
        time.sleep(0.05)
        