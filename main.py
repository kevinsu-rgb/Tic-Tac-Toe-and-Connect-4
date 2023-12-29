import sys
import pygame

HEIGHT = 1000
WIDTH = 1000
BG_COLOR = (255, 255, 245)
LINE_COLOR = (0, 0, 0)
BOARD_SIZE = 3
GAME_BOARD_HEIGHT = HEIGHT - 100  # Adjust the height as needed
LINE_WIDTH = 10
SQUARE_SIZE = ((GAME_BOARD_HEIGHT) // BOARD_SIZE) - 35
connect_4_col = 7
connect_4_row = 6
SQUARE_SIZE_connect4 = (HEIGHT // connect_4_row) - 50
RADIUS = (SQUARE_SIZE_connect4 // 2 - 15)

def draw_xy(board):
    x_image = pygame.image.load("x_image.png")
    o_image = pygame.image.load("o_image.png")
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'x':
                screen.blit(x_image, (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 25))
            elif board[row][col] == 'o':
                screen.blit(o_image, (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 25))


def draw_grid_tictactoe():
    for i in range(1, BOARD_SIZE):
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, 725), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, (i * SQUARE_SIZE) - 25), (GAME_BOARD_HEIGHT, (i * SQUARE_SIZE) - 25),LINE_WIDTH)


def print_board_tictactoe(board):
    for row in board:    # row: ["-", "-", "-"]
        for col in row:
            print(col, end=" ")
        print()

def initialize_board():
    # 1st approach
    return [["-" for i in range(3)] for j in range(3)]

def available_square(board, row, col):
    return board[row][col] == '-'

def mark_square(board, row, col, chip_type):
    board[row][col] = chip_type

def board_is_full(board):
    for row in board:
        for chip in row:
            if chip == "-":
                return False
    return True

def check_if_winner_tic_tac_toe(board, chip_type):
    # check all rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == chip_type:
            return True

# check all columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == chip_type:
            return True

    if board[0][0] == board[1][1] == board[2][2] == chip_type:
            return True
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
            return True
    return False

# row: row index, col: col index
def is_valid(board, row, col):
    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '-':
        return True
    return False

def initialize_board_connect4(num_rows, num_cols):
    return [["-" for i in range(num_cols)] for j in range(num_rows)] # defines the number of columns and rows (length and height)

def draw_grid_connect4(board):
    for row in range(connect_4_row):
        for col in range(connect_4_col):
            pygame.draw.rect(screen, (0,0,255), (col * SQUARE_SIZE_connect4, row * SQUARE_SIZE_connect4, SQUARE_SIZE_connect4, SQUARE_SIZE_connect4))
            pygame.draw.circle(screen, (0,0,0), (col * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2, row * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2), RADIUS)

    for row in range(connect_4_row):
        for col in range(connect_4_col):
            if board[row][col] == '1':
                pygame.draw.circle(screen, (255,0,0), (col * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2, (connect_4_row - row - 1) * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2), RADIUS)
            elif board[row][col] == '2':
                pygame.draw.circle(screen, (255,255,0), (col * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2, (connect_4_row - row - 1) * SQUARE_SIZE_connect4 + SQUARE_SIZE_connect4 // 2), RADIUS)

def print_board_connect4(board):
    for row in reversed(board): # reverses the board by turning board upside down
        for col in row:
            print(col, end=" ") # prints the board with a space in between "-"
        print()

def insert_chip_connect4(board, col, chip_type):
    insertion = True
    row = 0
    if board[row][col] == '-': # checks for open space
        board[row][col] = chip_type # returns / prints the chip type in the open space
    elif board[row][col] == '1' or '2': # checks if space is occupied
        row = 1
        while insertion == True:
            if row >= connect_4_row:
                row -= 1
                insertion = False
            elif board[row][col] == '-': # checks if space is open and goes up a column to check for open space
                board[row][col] = chip_type
                insertion = False
            elif board[row][col] == 'x' or 'o':
                row += 1
    return row

def check_if_winner_connect4(board, col, row, chip_type):
    count = 0
    for item in board:
        if item[col] == chip_type: # goes through every column to see if there is four in a row
            count += 1 # adds up how many in a row for each column
        else:
            count = 0
        if count == 4: # winner is decided if there is 4 of the same chip in a row
            return True
    count = 0
    for item in board[row]:
        if item == chip_type: # Checks each space in a row to see if it is occupied
            count += 1 # if multiple of the same chip_types occur in a row, then it will count up the amount in a row
        else:
            count = 0
        if count == 4: # winner is decided if there is 4 of the same chip in a row
            return True
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            diagonal1 = [board[i + k][j + k] for k in range(4)]
            diagonal2 = [board[i + k][j + 3 - k] for k in range(4)]
            if any(all(cell == chip_type for cell in diagonal1[i:i+4]) for i in range(len(diagonal1) - 3)) or any(all(cell == chip_type for cell in diagonal2[i:i+4]) for i in range(len(diagonal2) - 3)):
                return True
    return False

def Connect4_SCREEN(screen):
    board = initialize_board_connect4(connect_4_row,connect_4_col)
    winner_text = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 55)
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    surface.fill(BG_COLOR)

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    reset_text_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_text_surf.fill((66, 66, 66))
    reset_text_surf.blit(reset_text, (10, 10))
    reset_text_rect = reset_text_surf.get_rect(center=(600, HEIGHT // 2 + 360))
    screen.blit(reset_text_surf, reset_text_rect)

    mainmenu_text = button_font.render("Main Menu", 0, (255, 255, 255))
    mainmenu_text_surf = pygame.Surface((mainmenu_text.get_size()[0] + 20, mainmenu_text.get_size()[1] + 20))
    mainmenu_text_surf.fill((66, 66, 66))
    mainmenu_text_surf.blit(mainmenu_text, (10, 10))
    mainmenu_text_rect = mainmenu_text.get_rect(center=(200, HEIGHT // 2 + 350))
    screen.blit(mainmenu_text_surf, mainmenu_text_rect)

    game_run = True
    winner = False

    player = 1
    chip_type = '1'
    while game_run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_text_rect.collidepoint(event.pos):
                    player = 1
                    chip_type = '1'
                    board = initialize_board_connect4(connect_4_row, connect_4_col)
                    winner = False
                    game_run = True
                if mainmenu_text_rect.collidepoint(event.pos):
                    game_run = False
                else:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    col = mouseX // 115
                    if winner == False & col < 7 & (mouseY < 700):
                        row = insert_chip_connect4(board,col,chip_type)
                        if check_if_winner_connect4(board,col,row,chip_type) and winner == False:
                            Win_text = winner_text.render(f"Player {player} Wins", 0, (0, 255, 0))
                            Win_text_surf = pygame.Surface((Win_text.get_size()[0] + 20, Win_text.get_size()[1] + 20),pygame.SRCALPHA)
                            Win_text_surf.blit(Win_text, (10, 10))
                            Win_text_rect = Win_text_surf.get_rect(center=(400, HEIGHT // 2 - 100))
                            winner = True
                        elif board_is_full(board) == True:
                            Win_text = winner_text.render("No Winner", 0, (0, 255, 0))
                            Win_text_surf = pygame.Surface((Win_text.get_size()[0] + 20, Win_text.get_size()[1] + 20),pygame.SRCALPHA)
                            Win_text_surf.blit(Win_text, (10, 10))
                            Win_text_rect = Win_text_surf.get_rect(center=(400, HEIGHT // 2 - 100))
                            winner = True
                        player = 2 if player == 1 else 1  # if statements so that players alternate turns
                        chip_type = '2' if chip_type == '1' else '1'
        draw_grid_connect4(board)
        if(winner == True):
            screen.blit(Win_text_surf, Win_text_rect)
        pygame.display.flip()
        pygame.display.update()


def TIC_TAC_TOE_SCREEN(screen):
    winner_text = pygame.font.Font(None, 85)
    board = initialize_board()
    print_board_tictactoe(board)
    button_font = pygame.font.Font(None, 55)
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    surface.fill(BG_COLOR)

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    reset_text_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_text_surf.fill((66, 66, 66))
    reset_text_surf.blit(reset_text, (10, 10))
    reset_text_rect = reset_text_surf.get_rect(center=(600, HEIGHT // 2 + 360))
    screen.blit(reset_text_surf, reset_text_rect)

    Main_Menu_text = button_font.render("Main Menu", 0, (255, 255, 255))
    Main_Menu_text_surf = pygame.Surface((Main_Menu_text.get_size()[0] + 20, Main_Menu_text.get_size()[1] + 20))
    Main_Menu_text_surf.fill((66, 66, 66))
    Main_Menu_text_surf.blit(Main_Menu_text, (10, 10))
    Main_Menu_text_rect = Main_Menu_text.get_rect(center=(200, HEIGHT // 2 + 350))
    screen.blit(Main_Menu_text_surf, Main_Menu_text_rect)

    game_run = True
    winner = False
    player = 1
    chip = 'x'
    while game_run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_text_rect.collidepoint(event.pos):
                    board = initialize_board()
                    surface.fill(BG_COLOR)
                    screen.blit(reset_text_surf, reset_text_rect)
                    screen.blit(Main_Menu_text_surf, Main_Menu_text_rect)
                    winner = False
                    player = 1
                    chip = 'x'
                if Main_Menu_text_rect.collidepoint(event.pos):
                    game_run = False
                else:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    row = mouseY // 240
                    col = mouseX // 265
                    if row < 3 and col < 3:
                        if available_square(board,row,col) == True and winner == False:
                            mark_square(board,row,col,chip)
                            if check_if_winner_tic_tac_toe(board,chip) == True and winner == False:
                                Win_text = winner_text.render(f"Player {player} Wins", 0, (0, 0, 255))
                                Win_text_surf = pygame.Surface((Win_text.get_size()[0] + 20, Win_text.get_size()[1] + 20), pygame.SRCALPHA)
                                Win_text_surf.blit(Win_text, (10, 10))
                                Win_text_rect = Win_text_surf.get_rect(center=(400, HEIGHT // 2 - 100))
                                winner = True
                            elif board_is_full(board) == True:
                                Win_text = winner_text.render("Tie", 0, (0, 0, 255))
                                Win_text_surf = pygame.Surface((Win_text.get_size()[0] + 20, Win_text.get_size()[1] + 20), pygame.SRCALPHA)
                                Win_text_surf.blit(Win_text, (10, 10))
                                Win_text_rect = Win_text_surf.get_rect(center=(400, HEIGHT // 2 - 100))
                                winner = True
                            player = 2 if player == 1 else 1
                            chip = 'o' if chip == 'x' else 'x'
        draw_grid_tictactoe()
        draw_xy(board)
        if winner == True:
            screen.blit(Win_text_surf, Win_text_rect)
        pygame.display.update()
        pygame.display.flip()

def start_game(screen):

    button_font = pygame.font.Font(None, 55)
    title = pygame.font.Font(None, 85)
    bg = pygame.image.load("Game_background.jpg")

    screen.blit(bg, (0, 0))

    Game_text = title.render("Games", 0, (255, 255, 255))
    Game_text_surf = pygame.Surface((Game_text.get_size()[0] + 20, Game_text.get_size()[1] + 20), pygame.SRCALPHA)
    Game_text_surf.blit(Game_text, (10, 10))
    Game_text_rect = Game_text_surf.get_rect(center=(400, HEIGHT // 2 - 300))
    screen.blit(Game_text_surf, Game_text_rect)

    Tic_Text = button_font.render("Tic Tac Toe", 0, (255, 255, 255))
    Tic_Text_surf = pygame.Surface((Tic_Text.get_size()[0] + 20, Tic_Text.get_size()[1] + 20))
    Tic_Text_surf.fill((66, 66, 66))
    Tic_Text_surf.blit(Tic_Text, (10, 10))
    Tic_Text_rect = Tic_Text_surf.get_rect(center=(200, HEIGHT // 2 + 100))
    screen.blit(Tic_Text_surf, Tic_Text_rect)

    connect4_text = button_font.render("Connect 4", 0, (255, 255, 255))
    connect4_text_surf = pygame.Surface((connect4_text.get_size()[0] + 20, connect4_text.get_size()[1] + 20))
    connect4_text_surf.fill((66, 66, 66))
    connect4_text_surf.blit(connect4_text, (10, 10))
    connect4_text_rect = connect4_text_surf.get_rect(center=(600, HEIGHT // 2 + 100))
    screen.blit(connect4_text_surf, connect4_text_rect)

    start = True

    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tic_Text_rect.collidepoint(event.pos):
                    return 0
                elif connect4_text_rect.collidepoint(event.pos):
                    return 1
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    WIDTH = 800
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")
    end = False
    while end == False:
        game = start_game(screen)
        if game == 0:
            TIC_TAC_TOE_SCREEN(screen)
        elif game == 1:
            Connect4_SCREEN(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True



