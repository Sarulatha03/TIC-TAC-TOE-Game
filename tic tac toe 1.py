def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row, col = -1, -1

        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): "))
                if 1 <= move <= 9:
                    row, col = divmod(move - 1, 3)
                    if board[row][col] == ' ':
                        break
                    else:
                        print("That spot is already taken. Try again.")
                else:
                    print("Invalid input. Enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
