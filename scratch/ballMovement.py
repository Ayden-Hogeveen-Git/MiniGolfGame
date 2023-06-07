import pygame

w, h = 960, 720
title = "MiniGolf"
fps = 60

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption(title)


running = True
bX, bY = w//2, h//2
dirX, dirY = 1, 1


def draw(bX, bY):
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (bX, bY), 20)

    pygame.display.update()
    clock.tick(fps)


def move(bX, bY, dirX, dirY):
    bX += 5 * dirX
    bY += 5 * dirY

    if (bX >= w or bX <= 0):
        dirX *= -1
    if (bY >= h or bY <= 0):
        dirY *= -1

    return bX, bY, dirX, dirY


if (__name__ == "__main__"):
    while (running):
        
        draw(bX, bY)
        bX, bY, dirX, dirY = move(bX, bY, dirX, dirY)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    running = False