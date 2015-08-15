# coding=utf-8

# The user will be prompted with a menu where he/she will select a shape. Then the
# user will give the appropriate information needed to solve for the area, and the
# computer will give the area! Hope you all have taken geometry!
# What you will be Using:
# Input/Output, \
# Integers, Variables, \
# Strings, Print, \
# If/Elif/Else

import math


def cls( ):
    loop = 1
    while loop < 100:
        print( " \n" )
        loop += 1

def rectangleArea( ):
    h = int( input( 'Enter the height: ' ) )
    w = int( input( 'Enter the width: ' ) )
    area = h * w
    print( 'The area of your rectangle is', area )


def triangleArea( ):
    b = int( input( 'Enter the base length: ' ) )
    h = int( input( 'Enter the vertical height: ' ) )
    area = 0.5 * b * h
    print( 'The area of your triangle is', area )


def trapeziumArea( ):
    a = int( input( 'Enter the length of the top part: ' ) )
    b = int( input( 'Enter the length of the bottom part: ' ) )
    h = int( input( 'Enter the height: ' ) )
    area = 0.5 * (a + b) * h
    print( 'The area of your trapezium is', area )


def ellipseArea( ):
    pi = math.pi
    a = int( input( 'Enter the shortest distance from the origin: ' ) )
    b = int( input( 'Enter the longest distance from the origin: ' ) )
    area = pi * a * b
    print( 'The area of your ellipse is', area )


def squareArea( ):
    a = int( input( 'Enter the length of a side: ' ) )
    area = a ** 2
    print( 'The area of your square is', area )


def parallelogramArea( ):
    b = int( input( 'Enter the base length: ' ) )
    h = int( input( 'Enter the vertical height: ' ) )
    area = 0.5 * b * h
    print( 'The area of your parallelogram is', area )


def circleArea( ):
    r = int( input( 'Enter the radius: ' ) )
    pi = math.pi
    area = pi * (r ** 2)
    print( 'The area of your circle is', area )


def sectorArea( ):
    d = int( input( 'Enter the degree of the sector: ' ) )
    rad = math.radians( d )
    r = int( input( 'Enter the radius: ' ) )
    area = 0.5 * (r ** 2) * rad
    print( 'The area of your sector is', area )


def main( ):
    quitAction = True

    while quitAction == True:
        print( 'This is the available area to choose from:' )
        print( '1. Rectangle' )
        print( '2. Triangle' )
        print( '3. Trapezium' )
        print( '4. Ellipse' )
        print( '5. Square' )
        print( '6. Parallelogram' )
        print( '7. Circle' )
        print( '8. Sector' )
        print( '9. QUIT' )

        userSelection = int( input( 'Choose which shape you want calculate the area of: ' ) )

        if userSelection == 1:
            rectangleArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 2:
            triangleArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 3:
            trapeziumArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 4:
            ellipseArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 5:
            squareArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 6:
            parallelogramArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 7:
            circleArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 8:
            sectorArea( )
            retry = str( input( 'Do you want to try again? y/n: ' ) )
            retry = retry.upper( )
            print( retry )
            if retry == 'Y':
                cls( )
                continue
            elif retry == 'N':
                quitAction = False
            else:
                main( )

        elif userSelection == 9:
            quitAction = False

        else:
            print( 'Invalid selection' )
    return



main( )
print( 'Thank you for using this software.' )
