#Challenge 24
guess = input('What is the password: ')
guess = guess.lower()
#Has user enter password and make it lowercase
while True:
    if guess == "electricity":
        break
    #Stops the loop once password is correct
    print('Not even close.')
    guess = input('Guess: ')
    guess = guess.lower()
    #Prompts the user to enter the password again
print('You guessed it! Buzzzz')