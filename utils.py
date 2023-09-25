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


def draw_button(x, y, width, height, text, surface):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, (77, 97, 98), button_rect, border_radius=10)
    label_font = pygame.font.Font(None, 32)
    text_surface = label_font.render(text, True, THECOLORS['white'])
    text_rect = text_surface.get_rect(center=button_rect.center)
    surface.blit(text_surface, text_rect)


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
