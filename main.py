# Word Guessing Game Using Python.
import random

print('Welcome To Number Guessing Game...!')

name = input('Enter Your Name : ')
print('Good Luck....!!!', name)

words = ['Noodles', 'Fried Rice', 'Manchuria', 'Aloo 65', 'Crispy Corn']
print('-' * 50)
print('Check List Items')
for wor in words:
    print(wor, end='\n')
print('-' * 50)
word = random.choice(words)

count = 0
while count <= 3:
    pick = input('Guess Any Item : ')
    if pick == word:
        print('Congrats....Received Item Free')
        break
    else:
        print('OOPS......You have to  5% of the Pay')
    count += 1





