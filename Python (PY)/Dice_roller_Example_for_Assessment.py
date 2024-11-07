import sys 
import random as rnd

def roll_dice(sides):
    num = rnd.randint(1, sides)


    for roll in range(10):
        result_d10 = roll_dice(10)
        result_d6 = roll_dice(6)
        print(f"The d10 is {result_d10}, and the D6 is {result_d6}")
        d10_str = str(result_d10)
        d6_str = str(result_d6)
        print("the D10 is" + d10_str + "The D6 is " + d6_str)