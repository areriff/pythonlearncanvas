# encoding: utf-8
# The Goal: Inspired by Summer Son’s Mad Libs project with Javascript.
# The program will first prompt the user for a series of inputs a la Mad Libs.
# For example, a singular noun, an adjective, etc.
# Then, once all the information has been inputted, the program will take that data and
# place them into a premade story template. You’ll need prompts for user input, and to then print
# out the full story at the end with the input included.
#
# Concepts to keep in mind:
#
#     Strings
#     Variables
#     Concatenation
#     Print
#
repeat = True

while repeat:
    adjective1 = str( input( 'Give the first adjective.\n' ) )
    nouns1 = str( input( 'Give the first noun.\n' ) )
    number = str( input( 'Give a number.\n' ) )
    nouns2 = str( input( 'Give the second noun.\n' ) )
    adjective2 = str( input( 'Give the second adjective.\n' ) )
    verbs = str( input( 'Give a verb.\n' ) )
    nouns3 = str( input( 'Give the third noun.\n' ) )
    bodyPart = str( input( 'Give a body part.\n' ) )
    adjective3 = str( input( 'Give the third adjective.\n' ) )
    print( '\n' )
    storySentence1 = 'Look, I guarantee there`ll be ' + adjective1 + ' times. '
    storySentence2 = 'I guarantee that at some ' + nouns1 + ', ' + number + ' or both of us is gonna want to get out\n'
    storySentence3 = 'of this ' + nouns2 + '. '
    storySentence4 = 'But I also guarantee that if I don`t ask you to be ' + adjective2 + ', I`\n'
    storySentence5 = 'll ' + verbs + ' it for the rest of my ' + nouns3 + ', because I know, in my ' + bodyPart + ', you`re \n'
    storySentence6 = 'the ' + adjective3 + ' one for me.'
    theStory = storySentence1 + storySentence2 + storySentence3 + storySentence4 + storySentence5 + storySentence6
    print( '\n' + theStory )
    prompt = str( input( 'You want to try again? y/n\n' ) )
    if prompt == 'y':
        repeat = True
    elif prompt == 'n':
        repeat = False
    else:
        print( 'The program crashed LOL' )
        quit( )
print( 'Do enjoy this mad lib? Stay tune for more' )
quit( )
