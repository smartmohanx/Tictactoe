#MODULES:

import pygame,sys,numpy as np

#INITIALING pygame
pygame.init()

#CONSTANTS:

#SQUARE SIZE:
height = 600
width = height
#FIGURES:
square_size = height/3
space = height//10
draw_lines_width = height//100
circle_width = height//25
x_line_width = height//20
line_width = 15
#BOARD:
board_row = 3
board_col = 3
#COLORS:
bg_color = (30,199,180)
line_color = (0,255,255)
#SURFACE:
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("tic tac toe game.")
screen.fill(bg_color)
#CONSOLE BOARD:
board = np.zeros((board_row,board_col))
#print(board)

#FUNCTIONS:
def draw_figure():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 1:
                pygame.draw.circle(screen,"white",(int(col*square_size+square_size/2),int(row*square_size+square_size/2)),space,circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen,"black",(col*square_size+space,row*square_size+space),(col*square_size+square_size-space,row*square_size+square_size-space),x_line_width)
                pygame.draw.line(screen,"black",(col*square_size+space,row*square_size+square_size-space),(col*square_size+square_size-space,row*square_size+space),x_line_width)

def draw_line():
    #horizontal line
    pygame.draw.line(screen,line_color,(0,square_size),(width,square_size),line_width)
    pygame.draw.line(screen,line_color,(0,width-width/3),(width,width-width/3),line_width)
    #vertical line
    pygame.draw.line(screen,line_color,(square_size,0),(square_size,height),line_width)
    pygame.draw.line(screen,line_color,(height-height/3,0),(height-height/3,height),line_width)   

def mark_sqr(row,col,player):
    board[row][col] = player

def avail_sqr(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False

def board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                return False
    return True

def check_winner(player):
    #vertical win
    for col in range(board_col):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_winning_line(col,player)
            return True
    #horizontal win
    for row in range (board_row):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_winning_line(row,player)
            return True
    #asc diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        acs_diagonal_winning_line(player)
        return True
    #desc diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        desc_diagonal_winning_line(player)
        return True
        
    return False

def vertical_winning_line(col,player):
    posX = col * square_size + square_size/2
    if player == 1:
        color = "red"
    elif player == 2:
        color = "red"
    pygame.draw.line(screen, color,(posX,15),(posX,height - 15),20)

def horizontal_winning_line(row,player):
    posY = row * square_size + square_size/2
    if player == 1:
        color = "red"
    elif player == 2:
        color = "red"
    pygame.draw.line(screen, color,(15,posY),(width - 15,posY),20)
def acs_diagonal_winning_line(player):
    if player == 1:
        color = "red"
    elif player == 2:
        color = "red"
    pygame.draw.line(screen, color,(15,height-15),(width - 15,15),20)
def desc_diagonal_winning_line(player):
    if player == 1:
        color = "red"
    elif player == 2:
        color = "red"
    pygame.draw.line(screen, color,(15,15),(width-15,height-15),20)

def restart():
    screen.fill(bg_color)
    draw_line()
    player = 1
    for row in range(board_row):
        for col in range(board_col):
            board[row][col] = 0
draw_line()

#TEXT IN SURFACE:
font = pygame.font.SysFont('constantia',35)
text = font.render(' Restart : r/R',True,"white")
txtrect = text.get_rect()
txtrect.left

font = pygame.font.SysFont('verdana',15)
text1 = font.render('Created by Smart Mohanx.',True,"white")
txtrect1 = text1.get_rect()
txtrect1.center = (width-120,height-20)

player = 1
game_over = False
#MAINLOOP OF GAME:
while True:
    screen.blit(text,txtrect)
    screen.blit(text1,txtrect1)

    
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
                draw_figure()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
