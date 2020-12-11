# Input Examples

# print('Hello World')
# myName = input("Whats your name?\n")
# print("It is good to meet you, " + myName)
# print('The length of your name is: ')
# print(len(myName))
# myAge = input("Whats age?\n")
# print('you will be ' + str(int(myAge) + 1) + ' in a year.')

# Flow Controls

# example 1
# name = 'Msry'
# password = 'swordfish'
# if name == 'Mary':
#     print('Hello Mary')
#     if password == 'swordfish':
#         print('Access Granted')
#     else:
#         print('Wrong Pass')
# else:
#     print('Program Terminated!')

# example 2
# name = 'Alisce'
# age = 11
# if name == 'Alice':
#     print('Hi Alice')
# elif age < 12:
#     print('Not Allice')
# elif age > 2000:
#     print('you are immortal')
# else:
#     print('hello alice')

# exxample 3
# with if
import pprint
from random import randint, sample
import re
import sys
import random
from typing import Type
spam = 0
# if spam < 5:
# 	print ('Hello')
# 	spam = spam + 1

# with while
# while spam < 5:
#     print('hello')
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('thanks')

# example 4
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Parth':
#         continue
#     print('Hello ' + name + ' What\'s your password')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access Granted')

#  example 5
# for loop
# print('My name is')
# for i in range(5):
#     print('Parth five times (' + str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num
# print (total)

#  normal for loop Start - Stop
# for i in range(12, 16):

# for loop with Start - Stop - Step
# for i in range(0, 10, 2):

# for loop to count down
# for i in range(5, -1, -2):
#     print(i)

# importing modules

# import random
# for i in range(5):
#     print(random.randint(1, 10))

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# functions
# def hello():
# 	print('Howdy!')
# 	print('Hwdy!')
# 	print('Hello There')

# hello()
# hello()
# hello()


# with params
# def hello(name):
#     print('Hello ' + name)


# hello('Alice')
# hello('Bob')


# def getAnswer(answerNum):
#     if answerNum == 1:
#         return 'It is certain'
#     elif answerNum == 2:
#         return 'It is decidedly so'
#     elif answerNum == 3:
#         return 'Yes'
#     elif answerNum == 4:
#         return 'Reply hazy try again'
#     elif answerNum == 5:
#         return 'Ask again later'
#     elif answerNum == 6:
#         return 'Concentrate and ask again'
#     elif answerNum == 7:
#         return 'My reply is no'
#     elif answerNum == 8:
#         return 'Outlook not so good'
#     elif answerNum == 9:
#         return 'very doubtful'


# r = random.randint(1, 9)
# print(r)
# fortune = getAnswer(r)
# print(fortune)

# test = None
# print(test)

# Exception handling
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid Argument')


# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


# Example: Guess my number game

# secretNum = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20')

# # Ask player to guess 6 times
# for guessTaken in range(1, 7):
#     guess = int(input('Take a guess: '))

#     if guess < secretNum:
#         print('Your guess is too low')
#     elif guess > secretNum:
#         print('Your guess is too high')
#     else:
#         break  # this codition is correct guess

#     if guess == secretNum:
#         print('Good job! You guessed my number in ' +
#               str(guessTaken) + ' guesses!')
#     else:
#         print('Nope. the number i was thinking of was ' + str(secretNum))

# Practice 1
# def collatz(number):
#     if number % 2 == 0:
#         print(number // 2)
#         return number // 2
#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#         return result


# try:
#     userInput = int(input("Enter Num: "))
#     while (userInput != 1):
#         userInput = collatz(int(userInput))
# except ValueError:
#     print("Please enter integer")

# list
# catNames = []
# while True:
#     print("Enter name of cat " + str(len(catNames) + 1) + '(or nothing to stop.)')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]
# print('The cat names are: ')

# for name in catNames:
#     print(' ' + name)

someList = ['cat', 'dog', 'mat']

# for someVal in range(len(someList)):
#     print('Index ' + str(someVal) + ' in supplies is: ' + someList[someVal])

# 'in' and 'not in'

# 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# 'hey' not in ['hello', 'hi', 'howdy', 'heyas']


# myPets = ['jacob', 'john', 'lucifer']
# print("Enter a pet name: ")
# name = input()

# if name not in myPets:
#     print('No pet named ' + name)
# else:
#     print(name + ' is my pet')

# dog = ['fat', 'black', 'loud']
# size, color, feature = dog
# print(dog)

# Magic 8 Ball with a list


# messages = [['It is certain',
#              'It is decidedly so',
#              'Yes definitely',
#              'Reply hazy try again',
#              'Ask again later',
#              'Concentrate and ask again',
#              'My reply is no',
#              'Outlook not so good',
#              'Very doubtful']]
# print(messages[random.randint(0, len(messages) - 1)])


# passing references
# def eggs(params):
# 	params.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)


# spam = [['A', 'B', 'C', 'D'], ['a', 'b', 'c', 'd']]
# cheese = copy.deepcopy(spam)
# # cheese[1] = 42

# print(spam)
# print(cheese)

# spam = ['a', 'b', 'c', 'd']
# print(spam[int(int('3' * 2) / 11)])
# print(spam[:2])

# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.remove('cat'))
# print(bacon)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list3 = list1 + list1
# list3 = list1 * list1
# print(list3)


# practice of list
# spam = ['apples', 'bananas', 'tofu', 'cat']
# newSpam = [1, 3, 'hello']


# def makeStringFromList(aList):
#     for i in aList:
#         print(i, end=", ")


# makeStringFromList(newSpam)


# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# heart = ''
# for j in range(len(grid[-1])):
#     for i in reversed(range(len(grid))):
#         heart += grid[i][j]

#         if i == 0:
#             heart += '\n'
# print(heart)


# n = int(input("Enter Num: "))

# if n % 2 != 0:
#     print('Weird')
# elif n % 2 == 0 and (n in range(2, 6)):
#     print('Not Weird 2 - 5')
# elif n % 2 == 0 and (n in range(6, 21)):
#     print('Weird 6 - 20')
# elif n % 2 == 0 and (n in range(20, 101)):
#     print("Not Weird 20 up")


# n = int(input("Enter Num: "))

# for i in range(1, n+1):
#     print(i, end="")

# Dictonary example

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print("Enter a name / (blank to quit): ")
#     name = input()
#     if name == "":
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I don\'t have birthday info for ' + name)
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated')

# spam = {'color': 'red', 'age': 42}

# # for i in spam.values():
# # for i in spam.keys():
# for i in spam.items():
#     print(i)

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for char in message:
#     count.setdefault(char, 0)
#     count[char] = count[char] + 1

# pprint.pprint(count)


# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print("-+-+-")
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print("-+-+-")
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#     # print("-+-+-")


# turn = 'X'

# for i in range(9):
#     printBoard(theBoard)
#     print("Turn for " + turn + ". Move on which space?")
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# printBoard(theBoard)

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}


# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought


# print('Number of things being brought: ')
# print(" - Apples: " + str(totalBrought(allGuests, 'apples')))
# print(' - Cups: ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes: ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches: ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies: ' + str(totalBrought(allGuests, 'apple pies')))


# gameInventory = {'rope': 1, 'torch': 6,
#                  'gold coin': 42, 'dagger': 1, 'arrow': 12}


# def displayInventory(inventory):
#     print("Inventory: ")
#     inventoryItems = 0
#     for k, v in inventory.items():
#         inventoryItems = inventoryItems + v
#         print(str(v) + " - " + str.capitalize(k))

#     print("Total number of items: " + str(inventoryItems))


# displayInventory(gameInventory)


# def addToInventory(inventory, addedItems):
#     for item in addedItems:
#         inventory.setdefault(item, 0)
#         inventory[item] += 1
#     return inventory


# def displayInventory(inventory):
#     print("Inventory: ")
#     invTotItems = 0
#     for k, v in inventory.items():
#         invTotItems = invTotItems + v
#         print(str(v) + " - " + str(k))

#     print("Total number of items: " + str(invTotItems))


# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# Sincerely,
# Bob''')

# Strings

# def printPicnic(itemsDict, leftWidth, rightWdth):
#     print("PICNIC ITEMS".center(leftWidth + rightWdth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWdth))


# picnicItems = {'sandwiches': 4,
#                'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


# Validate input

# while True:
#     print('Enter your age: ')
#     age = input()

#     if age.isdecimal():
#         break
#     print('Please enter number for your age.')

# while True:
#     print('Select a new password (letters and numbers only): ')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers')

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]


# def printTable(itemDict, leftWidth, rightWdth):
#     print("PICNIC ITEMS".center(leftWidth + rightWdth, '-'))
#     for k, v in itemDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWdth))


# printTable(tableData, 12, 5)


# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True


# print('415-555-4242 is a phone no')
# print(isPhoneNumber('415-555-4242'))
# print('hello is a phone number')
# print(isPhoneNumber('hello is a phone number'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. ididn iss 415-555-9998'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found. ' + chunk)
# print('Done')

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())
