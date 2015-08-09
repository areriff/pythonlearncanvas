# __author__ = 'arif_'
################

# guests = ['Susan', 'Christopher', 'Bill', 'Satya']
# print(guests[-2])
# print(guests[1])
# guests[1] = 'Steve' # Replacing item from the list
# guests.append('Arif') # Append item to the list
# guests.remove('Satya')
# guests.remove(guests[-2])
# guests.append('Colin')
# del guests[0]
# print(guests[-1:-2])
# print(guests)
# print(guests.index('Arif'))
###############
# guests = ['Susan', 'Christopher', 'Bill', 'Satya']
# nbrValueList = len(guests)
# for steps in range(nbrValueList):
#     print(guests[steps])
################
# guests = ['Susan', 'Christopher', 'Bill', 'Satya']
# guests.sort()
# currentGuest = ()
# for currentGuest in guests:
#     print(currentGuest)
################
# guests = []
# name = ''
# while name != 'arif':
#     name = input('Welcome guest\nEnter your name\n')
#     print('')
#     guests.append(name)
# guests.remove('arif')
# guests.sort()
# for currentGuest in guests:
#     print(guests)
################
fileName = 'list.csv'
WRITE = 'w'
READ = 'r'
READWRITE = 'w+'
APPEND = 'a'

# myList = open(fileName, mode=WRITE)
# myList.write('arif effendi, 30\n')
# myList.write('syia, 30')
# myList.close()

# data = input('Please enter file info')
# file = open(fileName, mode=WRITE)
# file.write(data)
# file.close()

# How to read from file
# fileList = open('list.csv')
# allFileContents =  fileList.read()
# print(allFileContents)
# firstLine = fileList.readline()
# print(firstLine)
# secondLine = fileList.readline()
# print(secondLine)

# Import CSV and display all data row by row and one value by value.
import csv

with open(fileName, mode=READ) as animalFile:
    allRowsList = csv.reader(animalFile)
    for currentRow in allRowsList:
        print(','.join(currentRow))  # .join is use to combine the value and use , to display it
        # print(currentRow) # This is hideous form.
        print('This is individual values from the row above')
        for currentWord in currentRow:
            print(currentWord)
        print('')
