from pygame import mouse, draw
from colours import Colour as C
from math import atan2, pi, sin, cos


# --- Ball Class --- #
class Ball:
    def __init__(self, x, y, r, surface, colour=C.WHITE):
        self.x = x
        self.y = y
        self.r = r

        # Ball Physics
        self.angle = 0
        self.magnitude = 0

        self.surface = surface
        self.colour = colour
    
    def draw(self):
        """
        Draws the ball
        :return: None
        """
        draw.circle(self.surface, self.colour, (self.x, self.y), self.r)
    
    def move(self, x, y):
        """
        Moves the ball
        :param x: (int)
        :param y: (int)
        :return: None
        """
        
        self.x -= x
        self.y += y

    def setPos(self, x, y):
        """
        Sets the position of the ball
        :param x: (int)
        :param y: (int)
        """
        self.x = x
        self.y = y
    
    def getAngle(self, p1, p2):
        """
        Returns the angle between two points
        :param p1: (x, y) (int)
        :param p2: (x, y) (int)
        :return: (int) angle in radians
        """
        x1, y1 = p1
        x2, y2 = p2

        dX = x2 - x1
        dY = y2 - y1

        angle = atan2(-dY, dX)
        angle %= 2 * pi

        return angle

    def getMagnitude(self, p1, p2):
        """
        Returns the distance between two points
        :param p1: (x, y) (int)
        :param p2: (x, y) (int)
        :return: (int)
        """
        x1, y1 = p1
        x2, y2 = p2

        dX = x2 - x1
        dY = y2 - y1

        return (dX ** 2 + dY ** 2) ** 0.5

    def getPos(self):
        return (self.x, self.y)


# --- Levels --- #
class Lvls:
    def __init__(self, screen):
        self.screen = screen
        self.ball = Ball(100, 100, 10, screen)
        
        self.x1, self.y1 = 0, 0


class Lvl1(Lvls):
    def __init__(self, screen):
        super().__init__(screen)

    def draw(self, mouseDown, mouseReleased, m1):
        """
        Draws the level
        :param mouseDown: (bool)
        :param mouseReleased: (bool)
        :param m1: (x, y) (int)
        :return: (bool) mouseReleased
        """
        self.ball.draw()

        self.x1, self.y1 = mouse.get_pos()

        if (mouseDown):
            draw.circle(self.screen, C.WHITE, (self.x1, self.y1), 5)
            draw.line(self.screen, C.WHITE, m1, (self.x1, self.y1), 3)
            draw.circle(self.screen, C.WHITE, m1, 5)


        if (mouseReleased):
            self.ball.angle = self.ball.getAngle(m1, (self.x1, self.y1))
            self.ball.magnitude = self.ball.getMagnitude(m1, (self.x1, self.y1))

            print(f"Angle: {self.ball.angle}\nMagnitude: {self.ball.magnitude}\n")

            self.ball.move(cos(self.ball.angle) * self.ball.magnitude, sin(self.ball.angle) * self.ball.magnitude)

            mouseReleased = False

        return mouseReleased


