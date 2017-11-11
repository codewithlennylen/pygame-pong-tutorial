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
playPadMove = 0

compPadX = 520
compPadY = scr_Y/2
compSizeX = 30
compSizeY = 100
compPadMove = 0

ballX = scr_X/2
ballY = scr_Y/2
ballRadius = 10 
ballSpeed = 10
ballMoveX = ballSpeed 
ballMoveY = -ballSpeed

compScore = 0
playScore = 0

clock = pygame.time.Clock()

def writeToScreen(text,color,(posX,posY)):
    text = str(text)
    font = pygame.font.SysFont('comicsansms',30)#comicsansms
    textWrite = font.render(text,True,color)
    screen.blit(textWrite,(posX,posY))


# ================== Game Loop ============================

gameOver = False

while not gameOver:
    # ========================Event Loop==================4===4
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playPadMove = -10
            if event.key == pygame.K_DOWN:
                playPadMove = +10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playPadMove = 0
            if event.key == pygame.K_DOWN:
                playPadMove = 0
    
    #=========================Game Logic=====================

    if playPadY <= 0:
        playPadY = 0
    if playPadY + playSizeY >= scr_Y:
        playPadY  = scr_Y - playSizeY
    if compPadY <= 0:
        compPadY = 0
    if compPadY + compSizeY >= scr_Y:
        compPadY = scr_Y - compSizeY

    #=============== Ball Bounce And Score Check============== 
    if ballX <= 0:               #Hitting the playGoal
        ballMoveX = +ballSpeed
        compScore += 1
    if ballX >= scr_X:           #Hitting the compGoal
        ballMoveX = -ballSpeed
        playScore += 1
    if ballY <= 0:
        ballMoveY = +ballSpeed
    if ballY >= scr_Y:
        ballMoveY = -ballSpeed

    # =========== Computer movement=============
    if compPadY < ballY:
        compPadMove = 10
    if compPadY > ballY:
        compPadMove = -10

    #=========== Paddle Detection ============    
    if ballX <= playPadX + playSizeX and ballX + ballRadius >= playPadX:
        if ballY >= playPadY and ballY + ballRadius <= playPadY + playSizeY:
            ballMoveX = +ballSpeed
    if ballX + ballRadius >= compPadX and ballX <= compPadX + compSizeX:
        if ballY >= compPadY and ballY + ballRadius <= compPadY + compSizeY:
            ballMoveX = -ballSpeed            
        

    playPadY += playPadMove
    compPadY += compPadMove
    ballX += ballMoveX
    ballY += ballMoveY
    
    screen.fill(grey)

    pygame.draw.rect(screen,green,[playPadX,playPadY,playSizeX,playSizeY])
    pygame.draw.rect(screen,red,[compPadX,compPadY,compSizeX,compSizeY])
    pygame.draw.circle(screen, blue,[ballX,ballY],ballRadius)

    writeToScreen('Player : %s'%playScore,yellow,(10,10))
    writeToScreen('Computer : %s'%compScore,yellow,(350,10))
    print 'compScore : %s playScore : %s '%( compScore,playScore)
    
    pygame.display.flip()  #update()
    clock.tick(30)  #20-30, 40-60, 120
    
pygame.quit()
quit()









