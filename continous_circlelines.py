import pygame,random

pygame.init()
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("COLORFUL CIRCLES AND LINES")
keepGoing=True
hasDrawn = True
shouldDraw = False
##
##RED=(255,0,0)
##GREEN=(0,255,0)
##BLUE=(0,0,255)

color= [255,255,255]

img = pygame.image.load("1223.jpg")
screen.blit(img,(0,0))
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing=False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_r:
##                color[0]-=30
##                if color[0]<0:
##                    color[0]=255
##            if event.key == pygame.K_g:
##                color=GREEN
##            if event.key == pygame.K_b:
##                color=BLUE
        if event.type == pygame.MOUSEBUTTONDOWN:
            shouldDraw = True
        if event.type == pygame.MOUSEBUTTONUP:
            shouldDraw = False
        if event.type == pygame.MOUSEMOTION:
            if shouldDraw:
               spot=event.pos
               pygame.draw.circle(screen,color,spot,random.randint(0,20))
               hasDrawn = False

    if hasDrawn == False:
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.circle(screen,color,spot,random.randint(0,20))
        hasDrawn=True

    
    pygame.display.update()
    

pygame.quit()
