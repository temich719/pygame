import pygame
import sys
import json
from snake import Snake, Fruit
from pygame.math import Vector2
from utils import draw_button

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
RUNNING = True
SCREEN_UPDATE = pygame.USEREVENT
GAME_OVER = False
BEST_SCORE_JSON = 'best_score.json'

pygame.mixer.init(22050, -16, 2, 64)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
snake_eat_sound = pygame.mixer.Sound('sounds/snakeEat.mp3')
total_score = 0
best_score = int()
score_font = pygame.font.Font(None, 80)
best_score_font = pygame.font.Font(None, 60)
game_over_font = pygame.font.Font(None, 100)
text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
pygame.mouse.set_visible(False)
pygame.time.set_timer(SCREEN_UPDATE, 120)
snake = Snake()
fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)
play_again_button = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 80)
exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 135, 400, 80)


def terminate():
    pygame.quit()
    sys.exit()


def set_start_best_score():
    try:
        with open(BEST_SCORE_JSON, 'r') as file:
            global best_score
            best_score = json.load(file)
    except FileNotFoundError:
        best_score = 0


def set_new_best_score():
    global total_score, best_score
    if total_score > best_score:
        best_score = total_score
        with open(BEST_SCORE_JSON, 'w') as file:
            json.dump(best_score, file)


def change_cursor(x, y):
    if SCREEN_WIDTH // 2 - 200 <= x <= SCREEN_WIDTH // 2 + 200 and SCREEN_HEIGHT // 2 + 50 <= y <= SCREEN_HEIGHT // 2 + 215:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def play_again():
    global GAME_OVER, snake, fruit
    GAME_OVER = False
    snake = Snake()
    fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)


def eat_fruit():
    global total_score
    distance = (snake_pos - fruit.get_pos()).length()
    if distance < snake.get_cell_size():
        total_score += 1
        snake_eat_sound.play()
        fruit.change_pos()
        snake.add_block()


def game_over():
    global text, text_rect
    set_start_best_score()
    set_new_best_score()
    bs_text = best_score_font.render(f"Best score: {best_score}", True, (255, 255, 255))
    bs_rect = bs_text.get_rect()
    bs_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 250)
    score_text = score_font.render(f"Score is: {total_score}", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    screen.blit(bs_text, bs_rect)
    draw_button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, 400, 80, 'Play again', screen)
    draw_button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 135, 400, 80, 'Exit', screen)
    pygame.mouse.set_visible(True)


def check_game_over_condition():
    global GAME_OVER
    if ((snake_pos.x < 0
            or snake_pos.x > SCREEN_WIDTH - snake.get_cell_size()
            or snake_pos.y < 0 or snake_pos.y > SCREEN_HEIGHT - snake.get_cell_size())
            or (snake.check_head_and_body_collision() and snake.get_snake_len() > 3)):
        GAME_OVER = True


while RUNNING:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    change_cursor(mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_again_button.collidepoint(event.pos):
                play_again()
            elif exit_button.collidepoint(event.pos):
                terminate()

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
        game_over()
    else:
        snake.draw_snake(screen)
        fruit.draw_fruit(screen)
        snake_pos = snake.get_head_pos()
        eat_fruit()
        check_game_over_condition()

    pygame.display.flip()
    clock.tick(60)
