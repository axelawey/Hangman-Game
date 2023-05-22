import time

name = input('What is your name? ')
print('Hello, ' + name + "." + " It's time to play HANGMAN!")

time.sleep(1)

#User can proceed guessing
print('Time to start guessing...')
time.sleep(1)

#The secret would be set here and user can now select any word to play with.
word = ("secret")

#Variable with an empty value
num_guesses = ''

#Construct the number of turns
num_turns = 12

#Proceed with While Loop 
while num_turns > 0:

    #Create a counter starting with Zero
    wrong = 0

    #Determine whether User's CHaracter is in the User's guess
    for character in word:
        if character in num_guesses:
            print(character, end=""),
        #If User's guess is not among characters, "_" would be used to display so
        else:
            print("_", end=""),
            wrong += 1

        #If User produces correct answer
    if wrong == 0:
        print(" is the word. You Win" + " " + name + "!")
        break

    #Ask User again to guess a character
    guess = input("Guess a Character: ")
    num_guesses += guess

    #If User's guess is not found in the secret word Counter would decreases by 1
    num_turns -= 1
    print("Wrong")

    #Random display of User's remaning attempts or turns
    print(name + " you have", + num_turns, "left")

    #Game would end if User's attempts or turns are exhausted or equal to zero
    if num_turns == 0:
        print("You lost " + name + "," + " try again next time!")
            