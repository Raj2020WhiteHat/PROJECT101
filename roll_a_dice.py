import random


def roll_dice():
    return random.randint(1, 6)


dice_roll = roll_dice()
print("You rolled a", dice_roll)
