
from random import randint
# generate a number between 1~10
number = randint(1, 10)
print(number)
# input from user
guess = input('guess the number between 1~10 : ')
print(guess)
while True:
    try:
        if int(guess) > 0 and int(guess) < 11:
            print('all good')
            break
    except ValueError:
        print('please enter a number')
        continue