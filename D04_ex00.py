#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
###############################################################################
# Imports
from random import randint

# Body
anything = randint(1, 26)
count = 0
while(count < 5):
    count += 1
    try:
        n = int(input("Guess a number between 1 and 25 "))
        if n > 25:
            print("Number out of range")
        elif n == anything:
            print("You guessed correctly!")
        elif n < anything:
            print("Too low")
        elif n > anything:
            print("Too high")
        continue
    except:
        print('Please enter a number')


###############################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()