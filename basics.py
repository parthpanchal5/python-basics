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