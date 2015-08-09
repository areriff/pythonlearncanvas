# __author__ = 'areriff'
# print('Hello World')
# print('Please enter the amount of loan')
# loan = int(input('in RM'))
# interestRate = float(0.05)
# numberOfPayment = int(input('how many month would you like to pay'))
# monthly = loan*(float(interestRate)*(1+interestRate)*numberOfPayment)/((1+interestRate)*numberOfPayment-1)
# print('your monthly payment is', int(monthly))

import datetime
# currentDate = datetime.date.today()
# # print(currentDate)
# # print(currentDate.month)
# # print(currentDate.day)
# # print(currentDate.year)
# # print(currentDate.strftime('%d %B %Y'))
# # print(currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))
#
# userInput = input("What is your birthday? (dd/mm/yyyy)\n")
# birthday = datetime.datetime.strptime(userInput, '%d/%m/%Y').date()
# print(birthday)
# days = currentDate - birthday
# print(days.days,'days have passed since you were born')

# currentTime = datetime.datetime.now()
# print(currentTime)
# print(currentTime.hour)
# print(currentTime.minute)
# print(currentTime.second)
# print(datetime.datetime.strftime(currentTime, '%H:%M:%S %p'))
# print(currentTime.minute)

# This code is to calculate the dateline
# currentDate = datetime.date.today()
# datelineInput = input('Enter the dateline for your project, (dd/mm/yyyy)\n').upper()
# dateline = datetime.datetime.strptime(datelineInput, '%d/%m/%Y').date()
# remainingDays = dateline - currentDate
# if remainingDays == '0':
#     print('the dateline has passed. You\'re out')
# else:
#     print(dateline)
#     print('You have', remainingDays.days, 'days left.')

import turtle

for steps in range(20):
    turtle.forward(100)
    turtle.right(45)
    for moresteps in range(6):
        turtle.color('blue')
        turtle.forward(50)
        turtle.color('green')
        turtle.left(20)
    turtle.backward(90)
    turtle.left(45)
