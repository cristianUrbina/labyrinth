import  sys, pygame
from gameMap import gameMap
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

WINDOWWIDTH = 900
WINDOWHEIGHT = 600

PLAYERHEIGHT = 40
PLAYERWIDTH = 40

size = (WINDOWWIDTH,WINDOWHEIGHT)

#Coordenadas
coord_x=50
coord_y=50

#Velocidad
speed_x=0
speed_y=0

# Timer
clock = pygame.time.Clock()
# Crear ventana
screen = pygame.display.set_mode(size)
screen.fill(WHITE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_y = -1
            if event.key == pygame.K_DOWN:
                speed_y = 1
            if event.key == pygame.K_RIGHT:
                speed_x = 1
            if event.key == pygame.K_LEFT:
                speed_x = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y= 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_LEFT:
                speed_x = 0

    # LOGICA --------
    """    #MOUSE position
    mouse_x,mouse_y = pygame.mouse.get_pos()
    if mouse_x < coord_x :
        speed_x=-1
    else:
        speed_x= 1
    if mouse_y < coord_y:
        speed_y =-1
    else:
        speed_y = 1
    # --------------
    """
    ### ---- ZONA DE DIBUJO
    coord_x+=speed_x
    coord_y+=speed_y
    #CHECKING FOR COLLITIONS
    if coord_x >= WINDOWWIDTH-PLAYERWIDTH:
        speed_x*=0
        coord_x = WINDOWWIDTH-PLAYERWIDTH
    if coord_x <= 0:
        speed_x*=0
        coord_x = 0
    if coord_y >= WINDOWHEIGHT-PLAYERHEIGHT:
        speed_y*=0
        coord_y = WINDOWHEIGHT-PLAYERHEIGHT
    if coord_y <= 0:
        speed_y*=0
        coord_y = 0

    pygame.draw.rect(screen, BLACK, (coord_x,coord_y,PLAYERWIDTH,PLAYERHEIGHT))

    """pygame.draw.line(screen,GREEN,[0,100],[200,200],5)

    pygame.draw.circle(screen, RED, (400,400),30)"""
    ### -----
    pygame.display.flip()
    clock.tick(200)
