# encoding: utf-8
# The Goal: Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user.
# The user needs to guess what that number is. (In other words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
# You’ll need functions to check if the user input is an actual number, to see the difference between the
# inputted number and the randomly generated numbers, and to then compare the numbers.
#
# Concepts to keep in mind:
#
#     Random function
#     Variables
#     Integers
#     Input/Output
#     Print
#     While loops
#     If/Else statements

import random

mainValue = int( random.randrange( 10, 100, 1 ) )
# print(mainValue) # To check the randomly generated value
userGuess = 1
guessAnswer = False

if userGuess and mainValue:
    guessAnswer = True

while guessAnswer is True:
    userGuess = input( 'Guess number from 10 to 99\n' )
    if int( userGuess ) == mainValue:
        guessAnswer = True
        print( 'Congratulation! You\'re correct.' )
        print( 'Thank you for trying this game.' )
        break

    elif int( userGuess ) < mainValue:
        print( 'Your guessed number is lower than actual number, try again.' )

    elif int( userGuess ) > mainValue:
        print( 'Your guessed number is higher than actual number, try again' )

    else:
        print( 'You have entered an invalid value, try again' )
        raise ValueError

print( 'The correct answer is ', mainValue )  # To verified the randomly generated value
print( 'Exiting...' )
