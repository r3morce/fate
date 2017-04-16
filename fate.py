#!/usr/bin/env python

import random
# import tabulate

print("Simulate dice roll")

def diceRoll():
    dice1 = [-1, 0, 1]
    dice2 = [-1, 0, 1]
    dice3 = [-1, 0, 1]
    dice4 = [-1, 0, 1]

    dices = [dice1, dice2, dice3, dice4]


    rolls = []
    for dice in dices:
        rolls.append(random.choice(dice))

    result = 0
    for roll in rolls:
        result += roll



    print("Roll: {:<3} {}".format(result, rolls))


count = 0
while (count < 9):
    diceRoll()
    count = count + 1
