from py_ai.ia import ia

print("""
 _____  _  ____         _____  _____  ____         _____  ____  _____
/__ __\/ \/   _\       /__ __\/  _  \/   _\       /__ __\/  _ \/  __/    
  / \  | ||  /   _____   / \  | / \ ||  /   _____   / \  | / \||  \      
  | |  | ||  \__ \____\  | |  | |-| ||  \__ \____\  | |  | \_/||  /__     
  \_/  \_/\____/         \_/  \_/ \_/\____/         \_/  \____/\____/
""")

game_mode = """
Game mode available

    1. Player vs player
    ━━━━━━━━━━━━━━━━━━━
    2. Player vs AI
    ━━━━━━━━━━━━━━━━━━━
    3. Game History
    ━━━━━━━━━━━━━━━━━━━
    4. Quit
    ━━━━━━━━━━━━━━━━━━━
"""

game_continue = """
Game mode available

    1. Home
    ━━━━━━━━━━━━━━━━━━━
    2. Quit
    ━━━━━━━━━━━━━━━━━━━
"""

instructions = """
This is the tic tac toe board

   1 ┃ 2 ┃ 3
 ━━━━╋━━━╋━━━━
   4 ┃ 5 ┃ 6
 ━━━━╋━━━╋━━━━
   7 ┃ 8 ┃ 9

*instruction :
1. Insert the spot number (1-9) to put your sign
2. You must fill all 9 spots to get the result
3. Player 1 will go first 
"""

sign_dictionary = []
def load_sign_dictionary():
    for element in range(9):
        sign_dictionary.append(" ")


def reload_sign_dictionary():
    sign_dictionary.clear()


def print_board():
    board = f"""
        \t{sign_dictionary[0]} ┃ {sign_dictionary[1]} ┃ {sign_dictionary[2]} \t\t\t\t  1 ┃ 2 ┃ 3
          ━━━━╋━━━╋━━━━             ━━━━╋━━━╋━━━━
        \t{sign_dictionary[3]} ┃ {sign_dictionary[4]} ┃ {sign_dictionary[5]} \t\t\t\t  4 ┃ 5 ┃ 6
          ━━━━╋━━━╋━━━━             ━━━━╋━━━╋━━━━
        \t{sign_dictionary[6]} ┃ {sign_dictionary[7]} ┃ {sign_dictionary[8]} \t\t\t\t  7 ┃ 8 ┃ 9
    """
    print(board)


def take_input(player_name, board, sign):
    while True:
        try:
            x = int(input(f"{player_name} : "))
            x -= 1
            if 0 <= x < 9:
                if x in board:
                    print("This spot is blocked.")
                    continue
                board.append(x)
                board[x] = sign
                return board
            else:
                print("Please enter a number between 1-9.")
        except ValueError:
            print("Oops ! That was not a number.\n"
                  "Please enter a number between 1-9.")


def take_input_end_game():
    print(game_continue)
    mode = int(input(""))
    match mode:
        case 1:
            reload_sign_dictionary()
            main()
        case 2:
            quit("Thank you both for joining.\n")


def win_condition(player_name):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] != ' ' or \
            sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] != ' ' or \
            sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] != ' ' or \
            sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] != ' ' or \
            sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] != ' ' or \
            sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] != ' ' or \
            sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] != ' ' or \
            sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] != ' ':
        print(f"\nCongratulation {player_name} !!\nYou WON !")
        take_input_end_game()


def main():
    while True:
        try:
            print(game_mode)
            mode = int(input("Choose your game mode : "))
            match mode:
                case 1:
                    player_one = input("Enter player one name : ")
                    player_two = input("Enter player two name : ")

                    print(f"Thank you for joining {player_one} and {player_two}")
                    print(f"{instructions}\n{player_one} is sign will be - X")
                    print(f"{player_two} is sign will be - O")
                    input("Press enter to start the game.")

                    load_sign_dictionary()
                    print_board()

                    for i in range(9):
                        if i % 2 == 0:
                            print(f"{player_one}, it's your turn")
                            take_input(player_one, sign_dictionary, 'X')
                            win_condition(player_one)
                        else:
                            print(f"{player_two}, it's your turn")
                            take_input(player_one, sign_dictionary, 'O')
                            win_condition(player_two)
                        print_board()
                    print("This a TIE, Nobody Won. Play Again.")

                case 2:
                    player_one = input("Enter player name : ")

                    print(f"{instructions}\n{player_one} is sign will be - X")
                    input("Press enter to start the game.")

                    load_sign_dictionary()
                    print_board()

                    for i in range(9):
                        if i % 2 == 0:
                            print(f"{player_one}, it's your turn")
                            take_input(player_one, sign_dictionary, 'X')
                            win_condition(player_one)
                        else:
                            ia(sign_dictionary, 'O')
                            win_condition("AI")
                        print_board()
                    print("This a TIE, Nobody Won. Play Again.")

                case 4:
                    quit(":'(")

        except ValueError:
            continue


main()
