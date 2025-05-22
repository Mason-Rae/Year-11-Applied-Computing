#Chapter 17
import random

answer1 = "Absolutely!"
answer2 = "No way Pedro!"
answer3 = "Go for it tiger."
#Magic 8 ball answers

print("Welcome to the Magic 8 Ball game - use it to answer your questions...")

question = input("Ask me for any advice and I'll help you out: ")
#Gets user's question

print("shaking...\n", * 4)
#Prints 'shaking' 4 times

choice = random.randint(1,3)
#Chooses between 1-3 for an answer

if choice == 1:
    answer = answer1
elif choice == 2:
    answer = answer2
else:
    answer = answer3
#Gets the answer for the output

print(answer)