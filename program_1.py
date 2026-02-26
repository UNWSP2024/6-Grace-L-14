'''Random Dice Program
By Grace LeVoir
2 - 26 - 26'''

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    # Sum 2 numbers
    sum = roll1 + roll2
    # return sum to calling function
    return sum
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.

total = 0

for r in range(100):
    roll = randDice()
    total += roll

average = total/100
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

print(f'The average is {average:.2f}.')