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

# mark_sqr(0,0,1)
# mark_sqr(0,1,1)
# mark_sqr(0,2,1)

# mark_sqr(1,0,1)
# mark_sqr(1,1,1)
# mark_sqr(1,2,1)

# mark_sqr(2,0,1)
# mark_sqr(2,1,1)
# mark_sqr(2,2,1)

# print(board,"new board")

def avail_sqr(row,col):
    return board[row][col] == 0
# print(avail_sqr(1,1))
# print(avail_sqr(2,1))


def board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                return False
    return True   
# print(board_full())


draw_lines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            print(mouseX)
            mouseY = event.pos[1]
            print(mouseY)

            clicked_row = int(mouseY//200)
            print(clicked_row)
            clicked_col = int(mouseX//200)
            print(clicked_col)
            if avail_sqr(clicked_row,clicked_col):
                mark_sqr(clicked_row,clicked_col,player)
                player = player % 2 + 1
                print(board,'new board...!')

    pygame.display.update()




    '''
    SUMMARY OF THIS CODE:
    1.Adding MOUSEBUTTONDOWN KEY in main loop.
    2.Tracking Mouse X,Y positions.
    3.Adding variable player = 1 outside the main loop
    4.Adding clicked_row and clicked_col in console board if it avails of sqrs.
    4.After player1 is marked,nxt turn becomes player2 vise-virsa.
    '''