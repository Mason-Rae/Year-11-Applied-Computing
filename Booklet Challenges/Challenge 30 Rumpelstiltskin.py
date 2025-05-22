#Challenge 30
for a in range(-2, 1, 1):
    guess = input("Guess the first name: ")
    guess = guess.lower()
    #Has user attempt to guess name
    if guess == "mason":
        print("Well done")
        break
    #Activates if name is guessed correctly
    if a == 0:
        print("Out of tries")
        break
    #Activates if out of guesses
    print(a*-1,"left")
    #Counts done