import  sys, pygame, random
from gameMap import gameMap
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

WINDOWWIDTH = 900
WINDOWHEIGHT = 600

PLAYERHEIGHT = 20
PLAYERWIDTH = 20

size = (WINDOWWIDTH,WINDOWHEIGHT)

#Velocidad
speed_x=0
speed_y=0

# Timer
clock = pygame.time.Clock()
# Crear ventana
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

#Building the map

map = gameMap(WINDOWWIDTH,WINDOWHEIGHT)
mapNumber = str(random.randint(1,4))
coord_x, coord_y = map.setMapPixels('map'+mapNumber,PLAYERWIDTH,PLAYERHEIGHT)
#Displaying the map
background = pygame.image.load('data/maps/map'+mapNumber+'.jpg').convert()

winner = False

while not winner:
    screen.blit(background,(0,0))
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
        #MOUSE position
    mouse_x,mouse_y = pygame.mouse.get_pos()

    # --------------

    ### ---- ZONA DE DIBUJO
    coord_x_holder = coord_x
    coord_y_holder = coord_y
    coord_x+=speed_x
    coord_y+=speed_y
    #CHECKING FOR COLLITIONS
    if coord_x >= WINDOWWIDTH-PLAYERWIDTH:
        speed_x*=0
        coord_x = WINDOWWIDTH-PLAYERWIDTH-1
    if coord_x <= 0:
        speed_x*=0
        coord_x = 0
    if coord_y >= WINDOWHEIGHT-PLAYERHEIGHT:
        speed_y*=0
        coord_y = WINDOWHEIGHT-PLAYERHEIGHT-1
    if coord_y <= 0:
        speed_y*=0
        coord_y = 0
    if map.winner((coord_x,coord_y),PLAYERWIDTH,PLAYERHEIGHT):
        winner = True
    if map.collition((coord_x,coord_y),PLAYERWIDTH,PLAYERHEIGHT):
        speed_x*=0
        speed_y*=0
        coord_x = coord_x_holder
        coord_y = coord_y_holder


    pygame.draw.rect(screen, BLUE, (coord_x,coord_y,PLAYERWIDTH,PLAYERHEIGHT))
    ### -----
    pygame.display.flip()
    clock.tick(600)
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    winnerNumber = '1'
    winner_image = pygame.image.load('data/winner/winner'+winnerNumber+'.jpg').convert()
    screen.blit(winner_image,(WINDOWWIDTH/8,WINDOWHEIGHT/8))
    pygame.display.flip()
