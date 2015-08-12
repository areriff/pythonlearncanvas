__author__ = 'arif_'
print( 'This program will look for the prime number\n' )
minRange = 2
maxRange = int( input( '\nEnter maximum number.\n' ) )

for n in range( minRange, maxRange ):
    for x in range( minRange, n ):
        if n % x == 0:
            print( n, 'equals', x, '*', n // x )
            break
    else:
        # loop fell through without finding a factor
        print( n, 'is a prime number' )
