import random
import time
import math
from random import randint
from random import *

number1 = (randint(10,30))


print("Welcome to the guessing game.")

print("----------------------------")

print("In this game, you must choose a number between 10-30.")

print("----------------------------")

print("Ready? BEGIN!")

print("----------------------------")


max1 = int(input("Please Choose a number. ")) # the number must be between the number given at `number1`. The default is 10-30.

answer = number1





print("The choosen number is", answer)

print("----------------------------")


if answer == max1:
    print('You Win the game!')
else:
    print("You lost! The answer was")
print("----------------------------")
input("Press enter to exit")