import random
import time
import math
from random import randint
from random import *




print(
    """Welcome to the guessing game."""

"""\n----------------------------"""


"""\nIn this game, you must choose a number between 10-30."""

"""\n----------------------------"""

"""BEGIN!"""


"""----------------------------"""
)

user_wins = 0
computer_wins = 0

while True: #creates an endless loop 
    



    number1 = (randint(1,10))



    answer = number1


    print()

    max1 = int(input("Please Choose a number. ")) # the number must be between the number given at `number1`. The default is 10-30.





    print("----------------------------")


    if answer == max1:
        print('You Win the game!')

        user_wins+=1
        print("You have "+str(user_wins)+" wins")

        print("The computer has "+str(computer_wins)+" win(s)")
        print("\n----------------------------\n")


    else:
        print("You lost! The answer was", answer)

        computer_wins+=1
        print("The computer has "+str(computer_wins)+" win(s)")
        print("\n----------------------------\n")
