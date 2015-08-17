# # coding=utf-8
# You should create a program to display a bingo board starting with 10 randomly chosen numbers, like this:
#
# Bingo!
# Here's your board:
#
# __ __ __ __ __ __ __ __ __ __
# __ 12 __ __ __ __ __ __ 99 __
# __ __ __ __ __ __ __ __ __ __
# __ __ __ __ __ __ __ __ __ __
# __ __ 56 __ __ __ 87 __ __ __
# __ __ __ __ __ __ __ __ __ __
# __ __ __ __ __ __ __ __ __ __
# __ __ __ __ 82 __ __ __ __ __
# __ __ __ __ __ __ __ 35 __ __
# __ __ __ __ __ __ __ __ __ __
# Enter the called number 'q' to quit
# >
#
# You’ve written programs using random numbers before, but have never needed to store more than one. The problem with just doing this…
#
# listOfNumbers = []
# for n in range(10):
#    listOfNumbers += [random.randint(1,101)]
#
# …is that you may get the same number more than once. So how can we make sure that we get 10 different numbers?
#
# One way is to create a list of all of the numbers from 1 to 100, shuffle the list, and then take the first 10 items of the shuffled list:
#
# #this creates a list of the numbers 1 to 100
# possibleNumbers = [i for i in range(1,101)]
#
# #this shuffles the list
# random.shuffle(possibleNumbers)
#
# #this gets the first 10 numbers in the list (0-9)
# board = possibleNumbers[:10]
#
# You could create a fully functional Bingo game, where the user is presented with a board, and types in numbers that are called. If the user has a called number on their board, the number could be removed from the list and the board redrawn. You could also create another program for the caller, to generate the numbers.
