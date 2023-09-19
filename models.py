from pygame.color import THECOLORS


class Cannon:
    __TRIANGLE_HEIGHT = 50

    def __init__(self, screen_width, screen_height):
        color = THECOLORS['grey']

    def __fill_list(self, screen_width, screen_height):
        x1 = screen_width / 2
        y1 = screen_height - self.__TRIANGLE_HEIGHT
        x2 = x1 - self.__TRIANGLE_HEIGHT / 2
        y2 = screen_height
        x3 = x2 + self.__TRIANGLE_HEIGHT
        y3 = y2
        return [(x1, y1), (x2, y2), (x3, y3)]



