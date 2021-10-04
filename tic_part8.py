import pygame,sys,numpy as np
pygame.init()

board_row = 3
board_col = 3
LINE_COLOR = (23, 145, 135)
HEIGHT = 600
WIDTH = HEIGHT
square_size = HEIGHT/3
draw_lines_width = HEIGHT//100
circle_width = HEIGHT//25
x_line_width = HEIGHT//20
space = HEIGHT//10

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tictac_demo")
screen.fill("black")

def draw_lines():
    #vertical lines
    pygame.draw.line(screen,LINE_COLOR,(HEIGHT/3,0),(HEIGHT/3,HEIGHT),draw_lines_width)
    pygame.draw.line(screen,LINE_COLOR,(HEIGHT-HEIGHT/3,0),(HEIGHT-HEIGHT/3,HEIGHT),draw_lines_width)
    #horizontal lines
    pygame.draw.line(screen,LINE_COLOR,(0,WIDTH/3),(WIDTH,WIDTH/3),draw_lines_width)
    pygame.draw.line(screen,LINE_COLOR,(0,WIDTH-WIDTH/3),(WIDTH,WIDTH-WIDTH/3),draw_lines_width)

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
                pygame.draw.circle(screen,"red",(int(col*square_size+square_size/2),int(row*square_size+square_size/2)),space,circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen,"red",(col*square_size+space,row*square_size+space),(col*square_size+square_size-space,row*square_size+square_size-space),x_line_width)
                pygame.draw.line(screen,"red",(col*square_size+space,row*square_size+square_size-space),(col*square_size+square_size-space,row*square_size+space),x_line_width)


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
    hor_line_pos = row*square_size + square_size/2
    if player == 1:
        color = 'white'
    elif player == 2:
        color = 'white'
    pygame.draw.line(screen,color,(15,hor_line_pos),(WIDTH-15,hor_line_pos),15)
    
def vertical_winning_line(row,player):
    ver_line_pos = row*square_size + square_size/2
    if player == 1:
        color = 'white'
    elif player == 2:
        color = 'white'
    pygame.draw.line(screen,color,(ver_line_pos,15),(ver_line_pos,HEIGHT-15),15)

def desc_winning_line(player):
    if player == 1:
        color = 'white'
    elif player == 2:
        color = 'white'
    pygame.draw.line(screen,color,(0+20,0+15),(WIDTH-15,HEIGHT-20),20)


def asc_winning_line(player):
    if player == 1:
        color = 'white'
    elif player == 2:
        color = 'white'
    pygame.draw.line(screen,color,(0+20,HEIGHT-20),(WIDTH-20,0+20),20)


def restart():
    screen.fill('black')
    draw_lines()
    player = 1
    for row in range(board_row):
        for col in range(board_col):
            board[row][col] = 0

draw_lines()

font = pygame.font.Font('freesansbold.ttf',30)
text = font.render('Restart-r/R',True,"red")
txtrect = text.get_rect()
txtrect.left


player = 1
game_over = False
while True:
    screen.blit(text,txtrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY//square_size)
            clicked_col = int(mouseX//square_size)

            if avail_sqr(clicked_row,clicked_col):
                mark_sqr(clicked_row,clicked_col,player)
                if check_winner(player):
                    game_over = True
                player = player % 2 + 1
                print(board,'new board...!')
                draw_figure()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()





    '''
    SUMMARY OF THIS CODE:
    1.For restart a game,create restart() function.
    2.To call restart function into a mainloop through the KEY_r.
    3.After r_key is pressed in your keyboard game will be restarted.
    '''