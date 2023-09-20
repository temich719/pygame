import pygame
import sys
from models import Cannon, Bullet, Target
from utils import point_in_circle, place_circle, Circle

pygame.mixer.init(22050, -16, 2, 64)
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

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

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
                current_hero_frame = left_animations_list[frame_counter // 12]
                mario_x -= speed

            elif event.key == pygame.K_RIGHT:
                current_hero_frame = right_animations_list[frame_counter // 12]
                mario_x += speed

            elif event.key == pygame.K_UP:
                current_hero_frame = left_animations_list[frame_counter // 12]
                mario_y -= speed

            elif event.key == pygame.K_DOWN:
                current_hero_frame = right_animations_list[frame_counter // 12]
                mario_y += speed

    screen.fill((0, 0, 0))
    score_label = score_font.render(f'Score: {score}', True, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (100, 100))
    screen.blit(current_hero_frame, (mario_x, mario_y))
    circle.draw_circle(screen)
    pygame.draw.line(screen, crosshair_color, (mouse_x - 10, mouse_y), (mouse_x + 10, mouse_y), 2)
    pygame.draw.line(screen, crosshair_color, (mouse_x, mouse_y - 10), (mouse_x, mouse_y + 10), 2)
    cannon.draw(screen)

    if bullet.get_center()[1] + bullet.get_radius() <= 0:
        bullet = Bullet(list(cannon.get_main_point()))
    else:
        bullet.move(screen)

    target.move(screen, SCREEN_WIDTH)

    frame_counter += 1

    if frame_counter == 60:
        frame_counter = 0

    pygame.display.flip()
    clock.tick(60)
