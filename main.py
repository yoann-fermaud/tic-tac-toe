# tic_tac_toe

instructions = """
This is the tic tac toe board

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

*intstruction :
1. Insert the spot number (1-9) to put your sign
2. You must fill all 9 spots to get the result
3. Player 1 will go first 
"""

sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')


def print_board():
    board = f"""
        | {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]} |
        | {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]} |
        | {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]} |
    """
    print(board)


index_list = []
def take_input(player_name):
    while True:
        x = int(input(f"{player_name} : "))
        x -= 1
        if 0 <= x <= 9:
            if x in index_list:
                print("This spot is blocked.")
                continue
            index_list.append(x)
            return x
        else:
            print("Please enter a number between 1-9")


def calculate_result(player_one, player_two):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or \
            sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' or \
            sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' or \
            sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or \
            sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or \
            sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or \
            sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or \
            sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X':

        print(f"Congratulation {player_one} !!!\nYou WON")
        quit("Thank you both for joining.\n")

    elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or \
            sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O' or \
            sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O' or \
            sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O' or \
            sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O' or \
            sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O' or \
            sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O' or \
            sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O':
        print(f"Congratulation {player_two} !!!\nYou WON")
        quit("Thank you both for joining.\n")


def main():
    print("Welcome to the tic tac toe game !")
    # CASE -> IA or player
    player_one = input("Enter player one name : ")
    player_two = input("Enter player two name : ")
    print(f"Thank you for joining {player_one} and {player_two}")

    print(instructions)
    print(f"{player_one} is sign will be - X")
    print(f"{player_two} is sign will be - O")
    input("Press enter to start the game.")

    print_board()

    for i in range(9):
        if i % 2 == 0:
            print(f"{player_one}, it's your turn")
            index = take_input(player_one)
            sign_dictionary[index] = 'X'
        else:
            print(f"{player_two}, it's your turn")
            index = take_input(player_two)
            sign_dictionary[index] = 'O'

        print_board()
        calculate_result(player_one, player_two)

    print("This a TIE, Nobody Won. Play Again.")


main()
