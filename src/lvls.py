from pygame import mouse, draw, event
from colours import Colour as C


# --- Ball Class --- #
class Ball:
    def __init__(self, x, y, r, surface, colour=C.WHITE):
        self.x = x
        self.y = y
        self.r = r
        self.surface = surface
        self.colour = colour
    
    def draw(self):
        draw.circle(self.surface, self.colour, (self.x, self.y), self.r)
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def getPos(self):
        return (self.x, self.y)


# --- Levels --- #
class Lvls:
    def __init__(self, screen):
        self.screen = screen
        self.ball = Ball(100, 100, 10, screen)


class Lvl1(Lvls):
    def __init__(self, screen):
        super().__init__(screen)
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

        self.mouseDown = False

    def draw(self, mouseDown):
        self.ball.draw()
        self.x1, self.y1 = mouse.get_pos()

        self.x2, self.y2 = mouse.get_pos()
        draw.line(self.screen, C.WHITE, (self.x1, self.y1), (self.x2, self.y2), 5)

        if (mouseDown):
            draw.line(self.screen, C.WHITE, (self.x1, self.y1), (self.x2, self.y2), 5)
    

