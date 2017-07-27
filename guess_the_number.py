'''
guess_the_number.py

This program lets the user guess a random number between 1 and 10.

'''

import sys
import random

def game():
    #generate an int between 1 and 10, including 1 and 10
    secretNum = random.randint(1,10)
    guesses = [] #limits number of guesses
    
    while len(guesses) < 5: 
        try:
            userGuess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} is not a number!".format(userGuess))
        else:
        #compare the input to the secret number
            if userGuess == secretNum:
                print("You got it! My number was {}.".format(userGuess))
                break
            elif userGuess < secretNum:
                print("My number is higher than {}".format(userGuess))
            elif userGuess > secretNum:
                print("My number is lower than {}".format(userGuess))
            else:
                print("Nope, try again!")
            guesses.append(userGuess)
    else:
        print("Sorry, you didn't get it. My number was {}.".format(secretNum))
        
    playAgain = input("Would you like to play again? Y/n: ")
    if playAgain.lower() != 'n':
        game()
    else:
        print("Ok, bye!")
        sys.exit(0)
        
game()

sys.exit(0)
