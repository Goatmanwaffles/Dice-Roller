import os
import random
restart = 1
while restart == 1:
    diceCount = input("How many D6 would you like to roll (Enter only a whole number)")
    diceCount = int(diceCount)
    if diceCount == int:
        if int(diceCount) >= 1:
            while int(diceCount)>0:
                roll = random.randint(1,6)
                print(roll)
                diceCount = int(diceCount) - 1
    else:
        print("Not a valid number")
    i = input("Would you like to roll more dice ")
    if i == "N":
        restart = 0
