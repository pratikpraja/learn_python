import random


def player_input():
    player_choice = input("Choose Rock, Paper or Scissors.")
    if player_choice in ["Rock","rock","R","r"]:
        player_choice = 'r'
    elif player_choice in ["Paper","paper","P","p"]:
        player_choice = 'p'
    elif player_choice in ["Scissors","scissors","S","s"]:
        player_choice = 's'
    else:
        print("Invalid Selection! Please try again!")
        player_input()
    return player_choice


def comp_input():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = 'r'
    elif comp_choice == 2:
        comp_choice = 'p'
    else:
        comp_choice = 's'
    return comp_choice

def main():
    player_wins = 0
    comp_wins = 0

    while True:
        player_choice = player_input()
        comp_choice = comp_input()
        
        if player_choice == 'r':
            if comp_choice == 'r':
                print("You chose Rock and Computer chose Rock. It's a Tie!")
            elif comp_choice == 'p':
                print("You chose Rock and Computer chose Paper. Computer Won!")
                comp_wins += 1
            elif comp_choice == 's':
                print("You chose Rock and Computer chose Scissors. You Won!")
                player_wins += 1

        elif player_choice == 'p':
            if comp_choice == 'r':
                print("You chose Paper and Computer chose Rock. You Won!")
                player_wins += 1
            elif comp_choice == 'p':
                print("You chose Paper and Computer chose Paper. It's a Tie!")
            elif comp_choice == 's':
                print("You chose Paper and Computer chose Scissors. Computer Won!")
                comp_wins += 1

        elif player_choice == 's':
            if comp_choice == 'r':
                print("You chose Scissors and Computer chose Rock. Computer Won!")
                comp_wins += 1
            elif comp_choice == 'p':
                print("You chose Scissors and Computer chose Paper. You Won!")
                player_wins += 1
            elif comp_choice == 's':
                print("You chose Scissors and Computer chose Scissors. It's a Tie!")

        print("Player wins: ", player_wins)
        print("Computer wins: ", comp_wins)

        player_choice = input("Let's Play Again? (y/n)")
        if player_choice in ["Y","y"]:
            pass
        elif player_choice in ["N","n"]:
            exit()
        else:
            
if __name__ == '__main__':
    main()