# encoding: utf-8
# The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
# A complete text game, the program will let users move through rooms based on user input and get
# descriptions of each room. To create this, you’ll need to establish the directions in which the
# user can move, a way to track how far the user has moved (and therefore which room he/she is in), and
# to print out a description. You’ll also need to set limits for how far the user can move.
# In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”

# Concepts to keep in mind:
#
#     Strings
#     Variables
#     Input/Output
#     If/Else Statements
#     Print
#     List
#     Integers
#
# The tricky parts here will involve setting up the directions and keeping track of just how far the
# user has “walked” in the game. I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most.
# This project also continues to build on using user-inputted data. It can be a relatively basic game, but if
# you want to build this into a vast, complex word, the coding will get substantially harder, especially if
# you want your user to start interacting with actual objects within the game. That complexity could be
# great, if you’d like to make this into a long-term project. *Hint hint.


def choseSE( ):
    print( 'You have choose the Southeast door\n' )
    return


def choseSW( ):
    print( 'You have choose the Southwest door\n' )
    return


def start( ):
    print( 'Welcome to the Mansion of the dead.\n' )
    print( 'You\'re in Level 1 Room 1. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        lvl2room1( )
    elif decision == 'SW':
        choseSW( )
        lvl2room2( )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl2room1( ):
    print( '\nYou\'re in Level 2 Room 1. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        lvl3room1( )
    elif decision == 'SW':
        choseSW( )
        lvl3room2( )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl2room2( ):
    print( '\nYou\'re in Level 2 Room 2. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        lvl3room3( )
    elif decision == 'SW':
        choseSW( )
        lvl3room4( )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl3room1( ):
    print( '\nYou\'re in Level 3 Room 1. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    elif decision == 'SW':
        choseSW( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl3room2( ):
    print( '\nYou\'re in Level 3 Room 2. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    elif decision == 'SW':
        choseSW( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl3room3( ):
    print( '\nYou\'re in Level 3 Room 3. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    elif decision == 'SW':
        choseSW( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    else:
        print( 'You died.' )
        quit( )
    return


def lvl3room4( ):
    print( '\nYou\'re in Level 3 Room 4. There are two doors, pick one.' )
    decision = str( input( "Door labeled 'SE' or door labeled 'SW'\n" ) )
    if decision == 'SE':
        choseSE( )
        print( 'You found the treasure!!!' )
    elif decision == 'SW':
        choseSW( )
        print( 'The door collapsed on you!' )
        print( 'You died.' )
    else:
        print( 'You died.' )
        quit( )
    return


start( )

print( 'Thank You :-)' )
