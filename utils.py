import pygame
from math import sqrt
import random
from pygame.color import THECOLORS


def calc_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def point_in_circle(p, circle_center, circle_radius):
    return calc_distance(p, circle_center) <= circle_radius


def place_circle():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    return x, y


class Circle:
    __RADIUS = 15
    __COLOR = THECOLORS['blue']

    def __init__(self, center):
        self.__center = center

    def set_center(self, new_center):
        self.__center = new_center

    def get_center(self):
        return self.__center

    def get_radius(self):
        return self.__RADIUS

    def draw_circle(self, surface):
        pygame.draw.circle(surface, self.__COLOR, self.__center, self.__RADIUS, width=0)
