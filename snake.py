import pygame,random

SCREENSIZE=600
SNAKEBODY=20
GREEN=(0,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
FOODSIZE=20

pygame.init()
screen = pygame.display.set_mode([SCREENSIZE,SCREENSIZE])
pygame.display.set_caption("Snake")

keepGoing = True

snakeImg = pygame.Surface([SNAKEBODY-2,SNAKEBODY-2])
snakeImg.fill(GREEN)

snakeX = [200,200,200,200,200]
snakeY = [300,280,260,240,220]

foodImg = pygame.Surface([FOODSIZE,FOODSIZE])
foodImg.fill(WHITE)

foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20

direction = "DOWN"

score = 0

timer = pygame.time.Clock()

def die():
    global keepGoing
    myFont = pygame.font.SysFont("Arial",50)
    myText = myFont.render("Game Over!",True,WHITE)
    screen.blit(myText,(200,250))
    pygame.display.update()
    pygame.time.wait(3000)
    keepGoing = False


def collide(x1,y1,w1,h1,x2,y2,w2,h2):
    if x2<x1+w1 and x1<x2+w2 and y1<y2+h2 and y2<y1+h1:
        return True
    else:
        return False
    



while keepGoing:
    timer.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction !="UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction !="RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction !="LEFT":
                direction ="RIGHT"

    i = len(snakeX)-1
    while i>=1:
        snakeX[i] = snakeX[i-1]
        snakeY[i] = snakeY[i-1]
        i-=1


    if direction == "UP":
        snakeY[0]-=SNAKEBODY
    elif direction == "DOWN":
        snakeY[0]+=SNAKEBODY
    elif direction == "LEFT":
        snakeX[0]-=SNAKEBODY
    elif direction == "RIGHT":
        snakeX[0]+=SNAKEBODY


    if snakeY[0] < 0 or snakeY[0] > SCREENSIZE-SNAKEBODY or snakeX[0] < 0 or snakeX[0] > SCREENSIZE-SNAKEBODY: 
        die()
        

    i = len(snakeX)-1
    while i>=4:
        if collide(snakeX[0],snakeY[0],SNAKEBODY,SNAKEBODY,snakeX[i],snakeY[i],SNAKEBODY,SNAKEBODY):
            die()
        i-=1
    

    if collide(snakeX[0],snakeY[0],SNAKEBODY,SNAKEBODY,foodX,foodY,FOODSIZE,FOODSIZE):
        score+=1
        foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
        foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
        while foodX in snakeX and foodY in snakeY and snakeX.index(foodX)==snakeY.index(foodY):
            foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
            foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
        snakeX.append(1000)
        snakeY.append(1000)
        






    
    
    screen.fill(BLACK)
    screen.blit(foodImg,(foodX,foodY))
    for i in range(len(snakeX)):
        screen.blit(snakeImg,(snakeX[i]+1,snakeY[i]+1))
    if keepGoing:
        pygame.display.update()





pygame.quit()





##import pygame,random
##
##SCREENSIZE=600
##SNAKEBODY=20
##GREEN=(0,255,0)
##BLACK=(0,0,0)
##WHITE=(255,255,255)
##FOODSIZE=20
##
##pygame.init()
##screen = pygame.display.set_mode([SCREENSIZE,SCREENSIZE])
##pygame.display.set_caption("Snake")
##
##keepGoing = True
##
##snakeImg = pygame.Surface([SNAKEBODY-2,SNAKEBODY-2])
##snakeImg.fill(GREEN)
##
##snakeX = [200,200,200,200,200]
##snakeY = [300,280,260,240,220]
##
##foodImg = pygame.Surface([FOODSIZE,FOODSIZE])
##foodImg.fill(WHITE)
##
##foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##
##direction = "DOWN"
##
##score = 0
##
##timer = pygame.time.Clock()
##
##def die():
##    global keepGoing
##    myFont = pygame.font.SysFont("Arial",50)
##    myText = myFont.render("Game Over!",True,WHITE)
##    screen.blit(myText,(200,250))
##    pygame.display.update()
##    pygame.time.wait(3000)
##    keepGoing = False
##
##
##def collide(x1,y1,w1,h1,x2,y2,w2,h2):
##    if x2<x1+w1 and x1<x2+w2 and y1<y2+h2 and y2<y1+h1:
##        return True
##    else:
##        return False
##    
##
##
##
##while keepGoing:
##    timer.tick(3)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            keepGoing = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_UP and direction != "DOWN":
##                direction = "UP"
##            elif event.key == pygame.K_DOWN and direction !="UP":
##                direction = "DOWN"
##            elif event.key == pygame.K_LEFT and direction !="RIGHT":
##                direction = "LEFT"
##            elif event.key == pygame.K_RIGHT and direction !="LEFT":
##                direction ="RIGHT"
##
##    i = len(snakeX)-1
##    while i>=1:
##        snakeX[i] = snakeX[i-1]
##        snakeY[i] = snakeY[i-1]
##        i-=1
##
##
##    if direction == "UP":
##        snakeY[0]-=SNAKEBODY
##    elif direction == "DOWN":
##        snakeY[0]+=SNAKEBODY
##    elif direction == "LEFT":
##        snakeX[0]-=SNAKEBODY
##    elif direction == "RIGHT":
##        snakeX[0]+=SNAKEBODY
##
##
##    if snakeY[0] < 0 or snakeY[0] > SCREENSIZE-SNAKEBODY or snakeX[0] < 0 or snakeX[0] > SCREENSIZE-SNAKEBODY: 
##        die()
##        
##
##    i = len(snakeX)-1
##    while i>=4:
##        if collide(snakeX[0],snakeY[0],SNAKEBODY,SNAKEBODY,snakeX[i],snakeY[i],SNAKEBODY,SNAKEBODY):
##            die()
##        i-=1
##    
##
##    if collide(snakeX[0],snakeY[0],SNAKEBODY,SNAKEBODY,foodX,foodY,FOODSIZE,FOODSIZE):
##        score+=1
##        foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##        foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##        while foodX in snakeX and foodY in snakeY and snakeX.index(foodX)==snakeY.index(foodY):
##            foodX = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##            foodY = random.randint(0,(SCREENSIZE-FOODSIZE)/20)*20
##        snakeX.append(1000)
##        snakeY.append(1000)
##        
##
##
##
##
##
##
##    
##    
##    screen.fill(BLACK)
##    screen.blit(foodImg,(foodX,foodY))
##    for i in range(len(snakeX)):
##        screen.blit(snakeImg,(snakeX[i]+1,snakeY[i]+1))
##    if keepGoing:
##        pygame.display.update()
##
##
##
##
##
##pygame.quit()
