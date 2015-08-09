__author__ = 'arif_'
# answer = input('would you like express shipping')
# if answer == 'yes':
#     print('that will be an extra $10')
# else:
#     print('fine!')
# print('have a nice day')

# favouriteTeam = input('what is your favourite hockey team?\n')
# if favouriteTeam == 'Senators':
#     print('Yeah Go Sens Go')
#     print('Hmm')
# else:
#     print('bleh')
# if favouriteTeam == 'MU':
#     print('Yeah')
# else:
#     print('boo')

# bestTeam = 'MU'
# favouriteTeam = input('What is your favourite hockey team?\n')
# if favouriteTeam.upper() == bestTeam.upper():
#     print('Red Devil!!')
#     print('Yezza')
# print('Buekkk')

# Initialize the variable to fix the error from boolean being false
# freeToaster = False
# deposit = float(input('How much do you want to deposit\n'))
# if deposit >= 100:
#     freeToaster = True # This boolean here ;)
#     print('enjoy your toaster')
# else:
#     print('enjoy the free mug')
# print('have a nice day sucker')
# if freeToaster:
#     print('Just Kidding')

#############################################
# import locale
#
# locale.setlocale(locale.LC_ALL, '')  # use the user-default locale
# shippingCharge = False
# total = int(input('What is the total amount of purchase?\n'))
#
# if total < 50:
#     shippingCharge = True
# if shippingCharge == True:
#     TotalWithShipping = total + 10
#     print('You have to pay an extra', locale.currency(float(10)), 'for the total\
#  of', locale.currency(float(TotalWithShipping)), 'because\
#  you\'re cheap')  # What is locale.currency??
# else:
#     print('You have to pay', locale.currency(float(total)))
# print('Have a nice day.')
###########################################

# Team = input('Enter your favourite team: ').upper()
# Sport = input('Enter your favourite sport: ').upper()

##################
# if Sport == 'FOOTBALL':
#     print('Go Football!!')
#     if Team == 'MU':
#         print('Manchester United gonna win this year')
#     print('We love football')
# else:
#     print('Go and learn about football')
###################

# if Sport == 'FOOTBALL' and Team == 'MU': # make sure both are in capital latter because the previous .upper()
#     print('Go Red Devils!')
# # Make sure there are brackets. Same is as in math
# elif Sport == 'FOOTBALL' and (Team == 'LIVERPOOL' or Team == 'ARSENAL'):
#     print('you suck')
# else:
#     print('You\'re stupid')
###########################################
