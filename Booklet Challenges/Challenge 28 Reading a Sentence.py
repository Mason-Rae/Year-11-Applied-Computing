#Challenge 28
sentence = input("Write a sentence: ")
numberE = 0
#Base number of e

for letter in sentence:
    if letter =="e":
        #if its "e"
        numberE +=1
        #Adds a 1 per "e" in the sentence

print ("The number of e's in the sentence is:", numberE)
