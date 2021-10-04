import pygame,sys,numpy as np
pygame.init()

board_row = 3
board_col = 3
square_length = 200

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("tictac_demo")
screen.fill("black")

def draw_lines():
    #vertical lines
    pygame.draw.line(screen,"white",(200,0),(200,600),15)
    pygame.draw.line(screen,"white",(400,0),(400,600),15)
    #horizontal lines
    pygame.draw.line(screen,"white",(0,200),(600,200),15)
    pygame.draw.line(screen,"white",(0,400),(600,400),15)

#console board
board = np.zeros((board_row,board_col))
print(board,"initial board\n")

def mark_sqr(row,col,player):
    board[row][col] = player

def avail_sqr(row,col):
    return board[row][col] == 0

def board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                return False
    return True   


def draw_figure():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 1:
                pygame.draw.circle(screen,"red",(int(col*square_length+square_length/2),int(row*square_length+square_length/2)),60,20)
            elif board[row][col] == 2:
                space = 50
                pygame.draw.line(screen,"red",(col*square_length+space,row*square_length+square_length-space),(col*square_length+square_length-space,row*square_length+space),30)
                pygame.draw.line(screen,"red",(col*square_length+space,row*square_length+space),(col*square_length+square_length-space,row*square_length+square_length-space),30)


def check_winner(player):
        #vertical
    for col in range(board_col):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_winning_line(col,player)
            return True
        #horizontal
    for row in range(board_row):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_winning_line(row,player)
            return True
        #descanding
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        desc_winning_line(player)
        return True
        #ascending
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        asc_winning_line(player)
        return True

    return False

def horizontal_winning_line(row,player):
    hor_line_pos = row*square_length + square_length/2
    if player == 1:
        color = 'red'
    elif player == 2:
        color = 'red'
    pygame.draw.line(screen,color,(15,hor_line_pos),(600-15,hor_line_pos),15)
    
def vertical_winning_line(row,player):
    ver_line_pos = row*square_length + square_length/2
    if player == 1:
        color = 'red'
    elif player == 2:
        color = 'red'
    pygame.draw.line(screen,color,(ver_line_pos,15),(ver_line_pos,600-15),15)

def desc_winning_line(player):
    if player == 1:
        color = 'red'
    elif player == 2:
        color = 'red'
    pygame.draw.line(screen,color,(0+20,0+15),(600-15,600-20),15)


def asc_winning_line(player):
    if player == 1:
        color = 'red'
    elif player == 2:
        color = 'red'
    pygame.draw.line(screen,color,(0+20,600-20),(600-20,0+20),15)


draw_lines()

player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)

            if avail_sqr(clicked_row,clicked_col):
                mark_sqr(clicked_row,clicked_col,player)
                if check_winner(player):
                    game_over = True
                player = player % 2 + 1
                print(board,'new board...!')
                draw_figure()

    pygame.display.update()



    '''
    SUMMARY OF THIS CODE:
    1.Check a winner(player) through a check_winner() function.
    2.Creating functions are;
                            check_winner() function,
                            horizontal_winning_line(),
                            vertical_winning_line(),
                            desc_winning_line(),
                            asc_winning_line().                       
    3.Calling check_winner() function in mainloop.
    4.After calling check_winner() function, it will be executed and
        After executed, inside functions will be called 
        when one particular condition is satisfied and that one is executed too.
        (if not satisfied all .., return back to called place.)
    5.if anyone satisfied above condition,the winning line will be showed up on screen.
    6.After winning line is showed up, draw_figure() function is terminated.
    7.game_over=fasle variable is added outside mainloop and that variable is used in mainloop too.
    8.game_over=True, end the loop and game too.
    
    '''