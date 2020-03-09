import pygame

pygame.init()
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("My first game")
x = 50
y = 200
wight = 50
height = 50
speedX = 0
speedY = 0
gravity = 10
run = True
ground = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if x < 5 or x > 490:
        speedX = 0
    if keys[pygame.K_LEFT] and speedX > -10:
        speedX -= 0.2
    if keys[pygame.K_RIGHT] and speedX < 10:
        speedX += 0.2
    if keys[pygame.K_UP] and ground:
        speedY = -10
        ground = False

    x += speedX
    y += speedY
    if not ground:
         speedY += 0.2
    if y > 400:
        ground = True
    if ground:
        speedY = 0
    win.fill((0, 0, 0))
    x = int(x)
    y = int(y)
    pygame.draw.rect(win, (189, 23, 43), (x, y, wight, height))
    pygame.display.update()

pygame.quit()
