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
    quitAction = False
    while quitAction is True:
        userSelection = str( input( 'Choose which shape you want calculate the area of: ' ) )
        if userSelection is '1':
            rectangleArea( )
        elif userSelection is '2':
            triangleArea( )
        elif userSelection is '3':
            trapeziumArea( )
        elif userSelection is '4':
            ellipseArea( )
        elif userSelection is '5':
            squareArea( )
        elif userSelection is '6':
            parallelogramArea( )
        elif userSelection is '7':
            circleArea( )
        elif userSelection is '8':
            sectorArea( )
        elif userSelection is '9':
            quitAction = True
        else:
            print( 'Invalid selection' )
    print( 'Thank you for using this software.' )
