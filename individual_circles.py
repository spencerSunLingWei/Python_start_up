import pygame,random

pygame.init()
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("My First Pygame Project")
keepGoing=True
hasDrawn = True

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
colorList = [RED,GREEN,BLUE]

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            hasDrawn = False


    if hasDrawn == False:
        for i in range (100):          
            pygame.draw.circle(screen,colorList[i%3],spot,random.randint(0,50))
        hasDrawn=True
    pygame.display.update()




    
pygame.quit()
