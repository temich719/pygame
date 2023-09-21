import pygame
import sys
from models import Cannon, Bullet, Target
from utils import point_in_circle, place_circle, Circle
from snake import Snake, Fruit
from pygame.math import Vector2

pygame.mixer.init(22050, -16, 2, 64)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

start_frame_mario_position = pygame.image.load('images/0.png')
circle_center = place_circle()
shot = pygame.mixer.Sound('sounds/shot.wav')
score = 0
mario_x = 20
mario_y = 60

left_animations_list = [pygame.image.load(f'images/l{i}.png') for i in range(1, 6)]
right_animations_list = [pygame.image.load(f'images/r{i}.png') for i in range(1, 6)]

frame_counter = 0
running = True
current_hero_frame = start_frame_mario_position
speed = 10

cannon = Cannon(SCREEN_WIDTH, SCREEN_HEIGHT)
bullet = Bullet(list(cannon.get_main_point()))
target = Target()
circle = Circle(circle_center)

start_time = pygame.time.get_ticks()
end_time = None

score_font = pygame.font.Font(None, 36)
crosshair_color = pygame.color.THECOLORS['red']
pygame.mouse.set_visible(False)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

snake = Snake()
fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)


def terminate():
    pygame.quit()
    sys.exit()


while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if point_in_circle((mouse_x, mouse_y), circle.get_center(), circle.get_radius()):
                end_time = pygame.time.get_ticks()
                if end_time - start_time <= 1000:
                    score += 100
                elif end_time - start_time <= 2000:
                    score += 50
                else:
                    score += 1

                shot.play()
                circle.set_center(place_circle())
                start_time = pygame.time.get_ticks()
                end_time = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.change_direction(Vector2(-1, 0))

            elif event.key == pygame.K_RIGHT:
                snake.change_direction(Vector2(1, 0))

            elif event.key == pygame.K_UP:
                snake.change_direction(Vector2(0, -1))

            elif event.key == pygame.K_DOWN:
                snake.change_direction(Vector2(0, 1))

    screen.fill((0, 0, 0))
    snake.draw_snake(screen)
    fruit.draw_fruit(screen)
    snake_rect = snake.get_rect()
    fruit_rect = fruit.get_rect()
    if snake_rect.colliderect(fruit_rect):
        fruit.change_pos()

    frame_counter += 1

    if frame_counter == 60:
        frame_counter = 0

    pygame.display.flip()
    clock.tick(60)
