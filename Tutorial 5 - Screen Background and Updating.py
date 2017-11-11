import pygame

pygame.init()  #Initialize

#====================INITIALIZING ===================================

screen = pygame.display.set_mode((600,500))  # ( X, Y )

# ========================== (R,G,B) ==========================

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
yellow = (255,255,0)

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


    pygame.display.flip()  #update()
    










