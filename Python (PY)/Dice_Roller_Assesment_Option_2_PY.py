#list of Dice at Mininimum, D2 (Coin), D4 (Four side), D6 (Six Side), D8 (Eight Side), 
# D10 (Ten Side) (Might add on percentile for D10) D12 (Twelve Side) and the D20 (Twenty Side)

import sys
import random as rnd

def roll_dice (sides):
    num = rnd.randint(1, sides)
    return num

def Inp_dice():
    D_Sid = input("How Many Sides do you want the Dice to Have? > ")
    D_Sid = int(D_Sid)
    D_Rol = input("How Many Dice Would you Like to Roll? > ")
    D_Rol = int(D_Rol)
    return (D_Sid, D_Rol)


def Argv_Dice():
    D_Sid = sys.argv[1]
    D_Sid = int(D_Sid)
    D_Rol = sys.argv[2]
    D_Rol = int(D_Rol)
    return (D_Sid, D_Rol)


arg_count = len(sys.argv) 
if arg_count > 1:
    out_dice = Argv_Dice()
else: 
    out_dice = Inp_dice()

D_Rol = out_dice[1]
for roll in range(D_Rol):
    D_Anw = roll_dice(out_dice[0])
    print(f"The Result is {D_Anw}")