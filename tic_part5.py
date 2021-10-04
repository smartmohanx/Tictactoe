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

draw_lines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)

            if avail_sqr(clicked_row,clicked_col):
                mark_sqr(clicked_row,clicked_col,player)
                player = player % 2 + 1
                print(board,'new board...!')
                draw_figure()

    pygame.display.update()



    '''
    SUMMARY OF THIS CODE:
    1.Draw figures outside the mainloop,using draw_figure function.
    2.draw_figure function is called in mainloop.
    '''