import random
import time
import math
from random import randint
from random import *
import os



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



    if max1 > 10:
        repeat = input("That is not a valid choice. Please try again: ").lower()

    if max1 < 1:
        repeat = input("That is not a valid choice. Please try again: ").lower()
    



    print("----------------------------")


    if answer == max1:
        print(f"""You Win the game!
        \nYou chose {max1} and I chose {answer} """)

        user_wins+=1
        print("You have "+str(user_wins)+" wins")

        print("The computer has "+str(computer_wins)+" win(s)")
        print("\n----------------------------\n")


    else:
        print(f"""You lost! 
        \nI chose {answer} and you chose {max1}""")

        computer_wins+=1
        print("The computer has "+str(computer_wins)+" win(s)")
        print("\n----------------------------\n")



    repeat = input("Play again? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()
    
    if repeat == 'n':
        break



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
