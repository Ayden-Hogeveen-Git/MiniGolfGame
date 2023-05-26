from pygame import mouse, draw
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

        self.holeR = 20

class Lvl1(Lvls):
    def __init__(self, screen):
        super().__init__(screen)
        self.ball = Ball(100, 100, 10, self.screen)
    
    def draw(self):
        self.ball.draw()

        draw.circle(self.screen, C.DARK_GREY, (self.x, self.y), self.holeR)


class Lvl2(Lvls):
    def __init__(self, screen):
        super().__init__(screen)
        pass
    
    def draw(self):
        pass


class Lvl3(Lvls):
    def __init__(self, screen):
        super().__init__(screen)
        pass
    
    def draw(self):
        pass
