from py_ai.ia import ia


instructions = """
This is the tic tac toe board

   1 ┃ 2 ┃ 3         1 ║ 2 ║ 3
 ━━━━╋━━━╋━━━━      ═══╬═══╬═══
   4 ┃ 5 ┃ 6         4 ║ 5 ║ 6
 ━━━━╋━━━╋━━━━      ═══╬═══╬═══
   7 ┃ 8 ┃ 9         7 ║ 8 ║ 9

*intstruction :
1. Insert the spot number (1-9) to put your sign
2. You must fill all 9 spots to get the result
3. Player 1 will go first 
"""

game_mode = """
Game mode available

    1. Player vs player
    ━━━━━━━━━━━━━━━━━━━
    2. Player vs AI
    ━━━━━━━━━━━━━━━━━━━
"""

sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')


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


def calculate_result(player_name):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] != ' ' or \
            sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] != ' ' or \
            sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] != ' ' or \
            sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] != ' ' or \
            sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] != ' ' or \
            sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] != ' ' or \
            sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] != ' ' or \
            sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] != ' ':
        print(f"\nCongratulation {player_name} !!\nYou WON !")
        quit("Thank you both for joining.\n")


def main():
    print("Welcome to the tic tac toe game !")
    print(game_mode)
    mode = int(input("Choose your game mode : "))
    match mode:
        case 1:
            player_one = input("Enter player one name : ")
            player_two = input("Enter player two name : ")

            print(f"Thank you for joining {player_one} and {player_two}")
            print(instructions)
            print(f"{player_one} is sign will be - X")
            print(f"{player_two} is sign will be - O")
            input("Press enter to start the game.")

            print_board()

            for j in range(9):
                if j % 2 == 0:
                    print(f"{player_one}, it's your turn")
                    take_input(player_one, sign_dictionary, 'X')
                    calculate_result(player_one)
                else:
                    print(f"{player_two}, it's your turn")
                    take_input(player_one, sign_dictionary, 'O')
                    calculate_result(player_two)
                print_board()
            print("This a TIE, Nobody Won. Play Again.")

        case 2:
            player_one = input("Enter player name : ")

            print(instructions)
            print(f"{player_one} is sign will be - X")
            input("Press enter to start the game.")

            print_board()

            for j in range(9):
                if j % 2 == 0:
                    print(f"{player_one}, it's your turn")
                    take_input(player_one, sign_dictionary, 'X')
                    calculate_result(player_one)
                else:
                    ia(sign_dictionary, 'O')
                    calculate_result("AI")
                print_board()
            print("This a TIE, Nobody Won. Play Again.")


main()
