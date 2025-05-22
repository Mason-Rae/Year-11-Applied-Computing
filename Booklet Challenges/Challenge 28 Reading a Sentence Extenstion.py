#Challenge 28
sentence = input("Write a sentence: ")
numberOfVowels = 0

for letter in sentence:
    if letter in ("a", "e", "i", "o", "u"):
        numberOfVowels +=1

print ("The number of vowels in the sentence is:", numberOfVowels)
