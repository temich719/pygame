import pygame
import sys
from snake import Snake, Fruit
from pygame.math import Vector2
from utils import draw_button

pygame.mixer.init(22050, -16, 2, 64)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

snake_eat_sound = pygame.mixer.Sound('sounds/snakeEat.mp3')

running = True

score_font = pygame.font.Font(None, 36)

game_over_font = pygame.font.Font(None, 100)
text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

pygame.mouse.set_visible(False)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

snake = Snake()
fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)


def terminate():
    pygame.quit()
    sys.exit()


GAME_OVER = False


while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if SCREEN_WIDTH // 2 - 200 <= mouse_x <= SCREEN_WIDTH // 2 + 200 and SCREEN_HEIGHT // 2 + 50 <= mouse_y <= SCREEN_HEIGHT // 2 + 215:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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

    if GAME_OVER:
        screen.blit(text, text_rect)
        draw_button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 80, 'Play again', screen)
        draw_button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 135, 400, 80, 'Exit', screen)
        pygame.mouse.set_visible(True)
    else:
        snake.draw_snake(screen)
        fruit.draw_fruit(screen)

    snake_pos = snake.get_head_pos()

    # this is shit in def
    distance = (snake_pos - fruit.get_pos()).length()
    if distance < snake.get_cell_size():
        snake_eat_sound.play()
        fruit.change_pos()
        snake.add_block()

    if snake_pos.x < 0 or snake_pos.x > SCREEN_WIDTH - snake.get_cell_size() or snake_pos.y < 0 or snake_pos.y > SCREEN_HEIGHT - snake.get_cell_size():
        GAME_OVER = True

    pygame.display.flip()
    clock.tick(60)
