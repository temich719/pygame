import pygame
import sys
from snake import Snake, Fruit
from pygame.math import Vector2

pygame.mixer.init(22050, -16, 2, 64)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

snake_eat_sound = pygame.mixer.Sound('sounds/snakeEat.mp3')

running = True

score_font = pygame.font.Font(None, 36)
pygame.mouse.set_visible(False)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

snake = Snake()
fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)


def terminate():
    pygame.quit()
    sys.exit()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

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

    distance = (snake.get_head_pos() - fruit.get_pos()).length()
    if distance < snake.get_cell_size():
        snake_eat_sound.play()
        fruit.change_pos()
        snake.add_block()

    pygame.display.flip()
    clock.tick(60)
