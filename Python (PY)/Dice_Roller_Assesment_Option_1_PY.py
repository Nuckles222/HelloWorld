running = True 

def roll_dice (dice_Number):
    num = rnd.randint(1, dice_Number)
    return num 

while running:
    import sys 
    import random as rnd


    print("Would you Like to Roll the dice?")
    dice_Number = input("How many Sides on dice would you Like? > ")

    #for roll in range(dice_Number):
        #Result_Dice = roll_dice(dice_Number)

    Result_Dice = roll_dice(dice_Number)

    print(f"the result for the dice of {Result_Dice}")

    keep_going = input("would like to go Try Again? (Y/N)").upper()[0]
    if keep_going !='Y': 
        running = False 