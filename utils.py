import pygame
from math import sqrt
import random


def calc_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def point_in_circle(p, circle_center, circle_radius):
    distance = calc_distance(p, circle_center)
    return distance <= circle_radius


def place_circle():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    return x, y
