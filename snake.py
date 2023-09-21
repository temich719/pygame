import pygame
import random
from pygame.math import Vector2
from pygame.color import THECOLORS


class Snake:
    __CELL_SIZE = 40
    __rect = None

    def __init__(self):
        self.__body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.__direction = Vector2(1, 0)

    def draw_snake(self, surface):
        for block in self.__body:
            x = int(block.x * self.__CELL_SIZE)
            y = int(block.y * self.__CELL_SIZE)
            block_rect = pygame.Rect(x, y, self.__CELL_SIZE, self.__CELL_SIZE)
            pygame.draw.rect(surface, THECOLORS['green'], block_rect)
            self.__rect = block_rect

    def move_snake(self):
        body_copy = self.__body[:-1]
        body_copy.insert(0, body_copy[0] + self.__direction)
        self.__body = body_copy[:]

    def change_direction(self, direction):
        self.__direction = direction

    def get_head_pos(self):
        return self.__body[0]

    def get_rect(self):
        return self.__rect

    @staticmethod
    def get_cell_size(self):
        return self.__CELL_SIZE


class Fruit:
    __FRUIT_SIZE = 40
    __rect = None

    def __init__(self, screen_width, screen_height):
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__pos = self.__generate_pos()

    def __generate_pos(self):
        x = random.randint(0, self.__screen_width - self.__FRUIT_SIZE)
        y = random.randint(0, self.__screen_height - self.__FRUIT_SIZE)
        return Vector2(x, y)

    def draw_fruit(self, surface):
        rect = pygame.Rect(self.__pos.x, self.__pos.y, self.__FRUIT_SIZE, self.__FRUIT_SIZE)
        pygame.draw.rect(surface, THECOLORS['yellow'], rect, width=0)
        self.__rect = rect

    def get_rect(self):
        return self.__rect

    def change_pos(self):
        self.__pos = self.__generate_pos()

    def get_pos(self):
        return self.__pos
