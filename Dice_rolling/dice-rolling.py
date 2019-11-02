import random

def roll_dice():
    rolled_num = random.randint(1, 6)
    return rolled_num

def main():
    rolled = True
    while rolled:
        roll_again = input("Let's roll the dice? ENTER=Roll, 'Q'=Quit. ")
        if roll_again.lower() != 'q':
            rollled_num = roll_dice()
            print("You rolled : ",rollled_num)
        else:
            rolled = False

    print("Dice rolling simulator ended!")

main()