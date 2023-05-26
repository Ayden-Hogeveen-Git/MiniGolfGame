from pygame import mouse, draw, font
from colours import Colour as C


class Button:
    def __init__(self, x, y, width, height, text=""):
        self.x, self.y = x - (width // 2), y - (height // 2)
        self.width = width
        self.height = height
        self.clicked = False

        self.font = font.Font("freesansbold.ttf", width // 4)
        self.text = self.font.render(text, True, C.WHITE)
        self.textRect = (self.x + (self.x//20), self.y + (self.y//20), width, height)

    def draw(self, surface):
        pos = mouse.get_pos()

        if (self.x < pos[0] < self.x + self.width):
            if (self.y < pos[1] < self.y + self.height):
                self.clicked = True
            
        if (mouse.get_pressed()[0] == 0):
            self.clicked = False

        draw.rect(surface, C.BUTTON1, (self.x, self.y, self.width, self.height))
        draw.rect(surface, C.WHITE, (self.x, self.y, self.width, self.height), surface.get_width()//75)
        draw.rect(surface, C.BUTTON2, (self.x, self.y, self.width, self.height), surface.get_width()//100)
        
        surface.blit(self.text, self.textRect)

        return self.clicked
