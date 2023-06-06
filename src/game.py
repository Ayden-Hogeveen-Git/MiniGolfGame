from colours import Colour as C
from button import Button
from lvls import Lvls, Lvl1
import pygame
pygame.init()


# --- Setup Variables --- #
x, y = 800, 600
title = "MiniGolf"
fps = 60

screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
pygame.display.set_caption(title)


# --- Game Class --- #
class Game:
    def __init__(self):
        self.running = True
        self.mouseDown = False
        self.mouseReleased = False

        self.m1 = (0, 0)
        self.m2 = (0, 0)

        self.scene = 0
        self.grass = pygame.image.load("assets/miniGolfGrass.jpg")
        self.grass = pygame.transform.scale(self.grass, (x, y))

        # Buttons
        self.startButton = Button(x//2, y//2, 100, 50, "Start")

        # Lvls
        self.lvl = 1

        self.lvls = Lvls(screen)
        self.lvl1 = Lvl1(screen)

    def draw(self):
        screen.fill(C.DARK_GREY)
        screen.blit(self.grass, (0, 0))
        pygame.draw.rect(screen, C.WALL, (0, 0, x, y), x//20)

        self.drawScene(self.scene)

        pygame.display.update()
        clock.tick(fps)

    def drawScene(self, scene):
        if (scene == 0):
            self.drawMenu()
        elif (scene == 1):
            self.drawGame()
        elif (scene == 2):
            self.drawEnd()

    def drawMenu(self):
        if (self.startButton.draw(screen)):
            self.scene = 1

    def drawGame(self):
        if (self.lvl == 1):
            self.mouseReleased = self.lvl1.draw(self.mouseDown, self.mouseReleased, self.m1)
    
    def drawEnd(self):
        pass

    def run(self):
        while (self.running):
            self.draw()
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.running = False
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        self.running = False
                
                # --- Mouse Events --- #
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.mouseDown = True
                    self.m1 = pygame.mouse.get_pos()
                
                if (event.type == pygame.MOUSEBUTTONUP):
                    self.mouseDown = False
                    self.m2 = pygame.mouse.get_pos()

                    self.mouseReleased = True
         