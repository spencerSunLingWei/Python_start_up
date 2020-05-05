import pygame, random

pygame.init()
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("Animation Project")

keepGoing = True
freeze = False

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

posX = 300
posY = 300
speedX = 0
speedY = 0
radius = 50

posX2 = 0
posY2 = 300
speedX2 = random.randint(-10,10)
speedY2 = random.randint(-10,10)
radius2 = 20

soundBallHitTheWall=pygame.mixer.Sound("hitWall.wav")
soundBall2HitTheWall=pygame.mixer.Sound("hit.wav")
soundBallHitBall2=pygame.mixer.Sound("gameOver.wav")


while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speedY -= 10
            if event.key == pygame.K_DOWN:
                speedY += 10
            if event.key == pygame.K_RIGHT:
                speedX += 10
            if event.key == pygame.K_LEFT:
                speedX -= 10

    
    if posX <= radius or posX >= 600-radius:
        speedX *= -1
        soundBallHitTheWall.play()
    if posY <= radius or posY >= 600-radius:
        speedY *= -1
        soundBallHitTheWall.play()

    if posX2 <= radius2:
        speedX2 = random.randint(0,10)
        soundBall2HitTheWall.play()
    if posX2 >= 600-radius2:
        speedX2 = random.randint(-10,0)
        soundBall2HitTheWall.play()
    if posY2 <= radius2:
        speedY2 = random.randint(0,10)
        soundBall2HitTheWall.play()
    if posY2 >= 600-radius2:
        speedY2 = random.randint(-10,0)
        soundBall2HitTheWall.play()
        
    posX2 += speedX2
    posY2 += speedY2

    posX += speedX
    posY += speedY

    screen.fill(BLACK)
    pygame.draw.circle(screen,RED,(posX,posY),radius)
    pygame.draw.circle(screen,GREEN,(posX2,posY2),radius2)
    if (posX-posX2)**2+(posY-posY2)**2 <= (radius+radius2)**2 and freeze == False:
        freeze = True
        speedX = 0
        speedY = 0
        speedX2 = 0
        speedY2 = 0
        soundBallHitBall2.play()
    if not freeze:
        pygame.display.update()
        

pygame.quit()
