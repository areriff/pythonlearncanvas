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


shippingCharge = False
total = float(input('What is the total amount of purchase?\n'))

if total < 50:
    shippingCharge = True
if shippingCharge == True:
    TotalWithShipping = total + 10
    print('You have to pay', TotalWithShipping, 'because you\'re cheap')
else:
    print('You have to pay', total)
print('Have a nice day.')
