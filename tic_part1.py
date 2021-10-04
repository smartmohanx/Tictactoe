import pygame,sys
pygame.init()

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

draw_lines()


font = pygame.font.Font('freesansbold.ttf',30)
text = font.render('Restart-r/R',True,"red")
txtrect = text.get_rect()
txtrect.left

while True:
    screen.blit(text,txtrect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()



    '''
    SUMMARY OF THIS CODE:
    1.Imort pygame and Access pygame module.
    2.To Create a surface (Screen).
    3.Add Main Loop (while loop).
    4.To Attech QUIT or exit system in loop.
    5.Draw lines on screen through a function and call it Outside the loop.
    '''