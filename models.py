import pygame
from pygame.color import THECOLORS


class Cannon:
    __TRIANGLE_HEIGHT = 50

    def __init__(self, screen_width, screen_height):
        self.__color = THECOLORS['red']
        self.__triangle_points = self.__fill_list(screen_width, screen_height)

    def __fill_list(self, screen_width, screen_height):
        x1 = screen_width / 2
        y1 = screen_height - self.__TRIANGLE_HEIGHT
        x2 = x1 - self.__TRIANGLE_HEIGHT / 2
        y2 = screen_height
        x3 = x2 + self.__TRIANGLE_HEIGHT
        y3 = y2
        return [(x1, y1), (x2, y2), (x3, y3)]

    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color, (self.__triangle_points[0],
                                                    self.__triangle_points[1],
                                                    self.__triangle_points[2]))

    def get_color(self):
        return self.__color

    def get_triangle_points(self):
        return self.__triangle_points

    def get_main_point(self):
        return self.__triangle_points[0]


class Bullet:
    def __init__(self, center):
        self.__center = center
        self.__radius = 7
        self.__color = THECOLORS['blue']
        self.__speed = 3

    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, self.__center, self.__radius, width=0)

    def move(self, surface):
        self.__center[1] -= self.__speed
        self.draw(surface)

    def get_center(self):
        return self.__center

    def get_radius(self):
        return self.__radius


class Target:
    __START_X = 20
    __START_Y = 0

    def __init__(self):
        self.__color = THECOLORS['orange']
        self.__speed = 5
        self.__rect = self.__create_rectangle(self.__START_X, self.__START_Y)

    @staticmethod
    def __create_rectangle(x, y):
        return pygame.Rect(x, y, 50, 30)

    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.__rect, width=0)

    def move(self, surface, screen_width):
        if self.__START_X <= 0 or self.__START_X >= (screen_width - 50):
            self.__speed = -self.__speed
        self.__START_X += self.__speed
        self.__rect = self.__create_rectangle(self.__START_X, self.__START_Y)
        self.draw(surface)
