from TicTacToeClass import *


def restart():
    print("Would you like to run the game again? (yes/no)")
    again_question = input()
    if again_question.lower() == "yes":
        print("")
        main()
    elif again_question.lower() == "no":
        print("")
        print("Thank You for using our App!")
    else:
        print("Invalid input, please try again.")
        print("")
        restart()


def main():
    s = input("Please enter the size of the game: ")
    size = int(s)
    # player X is a random player and O is a player using alphabeta search
    play_game(TicTacToe(size, size, size), {'X': random_player, 'O': player(minimax_search)}, verbose=True)
    restart()


if __name__ == "__main__":
    main()