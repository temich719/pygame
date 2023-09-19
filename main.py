import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

start_frame_mario_position = pygame.image.load('images/0.png')
mario_x = 20
mario_y = 20

left_animations_list = [pygame.image.load(f'images/l{i}.png') for i in range(1, 6)]
right_animations_list = [pygame.image.load(f'images/r{i}.png') for i in range(1, 6)]

frame_counter = 0
running = True
current_hero_frame = start_frame_mario_position
speed = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_hero_frame = left_animations_list[frame_counter // 12]
                mario_x -= speed

            elif event.key == pygame.K_RIGHT:
                current_hero_frame = right_animations_list[frame_counter // 12]
                mario_x += speed

    screen.fill((0, 0, 0))
    screen.blit(current_hero_frame, (mario_x, mario_y))
    frame_counter += 1

    if frame_counter == 60:
        frame_counter = 0

    pygame.display.flip()
    clock.tick(60)
