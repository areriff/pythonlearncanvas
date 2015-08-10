__author__ = 'arif_'
###########
# Basic Division Calculator
###########
import sys

first = input('Enter the first number\n')
second = input('Enter the second number\n')

firstNumber = float(first)
secondNumber = float(second)
try:
    firstNumber = float(first)
    secondNumber = float(second)
    result = firstNumber / secondNumber
    print(first + ' / ' + second + ' = ' + str(result))

except (ZeroDivisionError, TypeError, ValueError):
    print('Contact the coder')
    errorFlag = True
    sys.exit()

except:
    error = sys.exc_info()[0]
    print('\nI am sorry something went wrong\n')
    print(error)
    sys.exit()

finally:
    print('\nThank you for using Python')
    ###########
    # firstNumber = float(input('enter the first number\n'))
    # secondNumber = float(input('enter the second number\n'))
    # try:
    #     result = firstNumber / secondNumber
    #     print(result)
    # except:
    #     print('I sorry, try again')
    ###########
