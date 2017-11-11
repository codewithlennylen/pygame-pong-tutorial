import pygame

pygame.init()  #Initialize

#====================INITIALIZING ===================================

scr_X = 600
scr_Y = 500

screen = pygame.display.set_mode((scr_X,scr_Y))  # ( X, Y )

# ========================== (R,G,B) ==========================

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
yellow = (255,255,0)

playPadX = 50
playPadY = scr_Y/2
playSizeX = 30
playSizeY = 100

compPadX = 520
compPadY = scr_Y/2
compSizeX = 30
compSizeY = 100

ballX =
ballY =
ballRadius = 

# ================== Game Loop ============================
while True:
    # ========================Event Loop=====================4
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #=========================Game Logic=====================

    screen.fill(white)

    pygame.draw.rect(screen,green,[playPadX,playPadY,playSizeX,playSizeY])
    pygame.draw.rect(screen,red,[compPadX,compPadY,compSizeX,compSizeY])

    pygame.draw.circle(screen, blue,[50,20],10)


    pygame.display.flip()  #update()
    










