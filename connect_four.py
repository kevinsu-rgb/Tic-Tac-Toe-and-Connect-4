def print_board(board):
    for row in reversed(board): # reverses the board by turning board upside down
        for col in row:
            print(col, end=" ") # prints the board with a space in between "-"
        print()

def initialize_board(num_rows, num_cols):
    return [["-" for i in range(num_cols)] for j in range(num_rows)] # defines the number of columns and rows (length and height)

def insert_chip(board, col, chip_type):
    insertion = True
    row = 0
    if board[row][col] == '-': # checks for open space
        board[row][col] = chip_type # returns / prints the chip type in the open space
    elif board[row][col] == 'x' or 'o': # checks if space is occupied
        row = 1
        while insertion:
            if board[row][col] == '-': # checks if space is open and goes up a column to check for open space
                board[row][col] = chip_type
                insertion = False
            elif board[row][col] == 'x' or 'o':
                row += 1
    return row

def check_if_winner(board, col, row, chip_type):
    count = 0
    for item in board:
        if item[col] == chip_type: # goes through every column to see if there is four in a row
            count += 1 # adds up how many in a row for each column
        if count == 4: # winner is decided if there is 4 of the same chip in a row
            return True
    count = 0
    for item in board[row]:
        if item == chip_type: # Checks each space in a row to see if it is occupied
            count += 1 # if multiple of the same chip_types occur in a row, then it will count up the amount in a row
        if count == 4: # winner is decided if there is 4 of the same chip in a row
            return True


def board_is_full(board):
    for row in board:
        for chip in row: # checks through every row if spaces are filled
            if chip == "-":
                return False
    return True # All spaces are filled if there is no open space "-"

if __name__ == "__main__":  # main function
    player = 1 # starting player
    chip_type = "x" # player 1's chip
    num_rows = int(input("What would you like the height of the board to be? ")) # user inputs how long and tall they want the connect 4 board to be
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols) # creates the board
    print_board(board) # prints out the board
    print("")
    print("Player 1: x")
    print("Player 2: o")
    game_continue = True
    while game_continue: # loops the game till winner
        print("")
        col = int(input(f"Player {player}: Which column would you like to choose? ")) # player decides the column to put the chip
        row = insert_chip(board, col, chip_type) # calls function to insert chip
        print_board(board)
        if check_if_winner(board, col, row, chip_type): # calls function to decide if a player has won the game
            print("")
            print(f"Player {player} won the game!")
            game_continue = False # game ends if the game is won
        else:
            if board_is_full(board):
                print("Draw. Nobody wins.")
                game_continue = False # game ends in a tie if the board fills up
        player = 2 if player == 1 else 1                # if statements so that players alternate turns
        chip_type = 'o' if chip_type == 'x' else 'x'