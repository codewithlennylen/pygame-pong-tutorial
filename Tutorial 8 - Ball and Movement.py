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

ballX = scr_X/2
ballY = scr_Y/2
ballRadius = 10 



# ================== Game Loop ============================

gameOver = False

while not gameOver:
    # ========================Event Loop==================4===4
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playPadY -= 10
            if event.key == pygame.K_DOWN:
                playPadY += 10
    
    #=========================Game Logic=====================

    screen.fill(white)

    pygame.draw.rect(screen,green,[playPadX,playPadY,playSizeX,playSizeY])
    pygame.draw.rect(screen,red,[compPadX,compPadY,compSizeX,compSizeY])

    pygame.draw.circle(screen, blue,[ballX,ballY],ballRadius)


    pygame.display.flip()  #update()
    
pygame.quit()
quit()









