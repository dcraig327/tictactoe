import os

player_list = ['X','O']
game_board = None
instruction_board = None
current_player = None
game_over_message = None
input_square = None

def clear_screen():
    os.system('clear')

def init_game_board():
    global game_board
    game_board =    [[' ',' ',' '],
                     [' ',' ',' '],
                     [' ',' ',' ']]

def init_instruction_board():
    global instruction_board
    instruction_board =    [['1','2','3'],
                            ['4','5','6'],
                            ['7','8','9']]

# X, O, Tie, Unfinished
def check_for_winner():
    z = game_board
    for i in range(0,3):
        if( ' ' == z[i][0]):
            continue
        if( ord(z[i][0]) == ((ord(z[i][0]) & ord(z[i][1])) & ord(z[i][2])) ):
            return(z[i][0] + " is the winner!")
    if( ' ' != z[0][0]):
        if( ord(z[0][0]) == ((ord(z[0][0]) & ord(z[1][1])) & ord(z[2][2])) ):
            return(z[0][0] + " is the winner!")
    if( ' ' != z[2][0]):
        if( ord(z[2][0]) == ((ord(z[2][0]) & ord(z[1][1])) & ord(z[0][2])) ):
            return(z[2][0] + " is the winner!")
    for i in range(0,3):
        for j in range(0,3):
            if(' ' == z[i][j]):
                return("Unfinished game.")
    return("It's a tie.")

def draw_instruction_board_empty_row():
    print("+---+---+---+")

def draw_instruction_board_row(row):
    print('|',' ',row[0],' ','|',' ',row[1],' ','|',' ',row[2],' ','|',sep='')

def draw_instruction_board():
    draw_instruction_board_empty_row()
    draw_instruction_board_row(instruction_board[0])
    draw_instruction_board_empty_row()
    draw_instruction_board_row(instruction_board[1])
    draw_instruction_board_empty_row()
    draw_instruction_board_row(instruction_board[2])
    draw_instruction_board_empty_row()

def draw_game_board_empty_row():
    print("+---+---+---+")

def draw_game_board_row(row):
    print('|',' ',row[0],' ','|',' ',row[1],' ','|',' ',row[2],' ','|',sep='')

def draw_game_board():
    draw_game_board_empty_row()
    draw_game_board_row(game_board[0])
    draw_game_board_empty_row()
    draw_game_board_row(game_board[1])
    draw_game_board_empty_row()
    draw_game_board_row(game_board[2])
    draw_game_board_empty_row()

def restart():
    global game_over_message
    global current_player
    global input_square
    game_over_message = None
    input_square = None
    current_player = player_list[0]

    clear_screen()
    init_game_board()
    init_instruction_board()
    display_introduction()
    draw()

def display_introduction():
    print("Welcome to 2 Player Tic-Tac-Toe!")
    print("--------------------------------")
    print("")
    print("X goes first. O goes second. Please decide who will be X and O.")
    print("")
    print("Below is the numbers used to input your move. For example. When it's X's turn, X will be asked 'Which square X?' and typing '1' will put an X in the top left of the game board.")
    print("")
    print("Have fun!")
    print("")
    print("")
    draw_instruction_board()
    print("")
    input("Press ENTER to continue..")

def startup():
    restart()

def shutdown():
    pass

def restart_check():
    print("")
    print("")
    #would you like to replay? restart()
    input_replay = input("Would you like to play again? [Y/N]: ")
    if((input_replay == "Y") or (input_replay == "Yes") or (input_replay == "y") or (input_replay == "yes")):
        restart()

def userinput():
    global input_square
    print("")
    input_square = int(input(f"Which square {current_player}?"))

def move():
    global game_board
    global current_player
    global game_over_message
    i = ((input_square-1)//3)
    j = ((input_square-1)%3)
    game_board[i][j] = current_player

    check = check_for_winner()
    if(check != "Unfinished game."):
        game_over_message = check
    
    if(player_list[0] == current_player):
        current_player = player_list[1]
    else:
        current_player = player_list[0]

def draw():
    clear_screen()
    if(game_over_message != None):
        print(game_over_message)
        print("")
    draw_game_board()

def gameloop():
    userinput()
    move()
    draw()

def main():
    startup()
    while(game_over_message == None):
        gameloop()
        if(game_over_message != None):
            restart_check()
    shutdown()

main()