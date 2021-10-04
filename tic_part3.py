import pygame,sys,numpy as np
pygame.init()

board_row = 3
board_col = 3

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

mark_sqr(0,0,1)
mark_sqr(0,1,1)
mark_sqr(0,2,1)

mark_sqr(1,0,1)
mark_sqr(1,1,1)
mark_sqr(1,2,1)

mark_sqr(2,0,1)
mark_sqr(2,1,1)
mark_sqr(2,2,1)

print(board,"new board")



def avail_sqr(row,col):
    return board[row][col] == 0
print(avail_sqr(1,1))
print(avail_sqr(2,1))


def board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                return False
    return True   
print(board_full())


draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()




    '''
    SUMMARY OF THIS CODE:
    1.mark squares through a mark_sqr function.
    2.Test that marked sqrs, through the avail_sqr function.
    3.Check a board is full or not through the board_full function.
    '''