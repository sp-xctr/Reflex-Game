import pygame
from random import randint

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
TARGET_SIZE = 200
TIMER_MIN, TIMER_MAX = 5000, 10000

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Reflex Game")

font = pygame.font.Font(None, 50)

target_surf = pygame.Surface((TARGET_SIZE, TARGET_SIZE))

screen.fill("blue")

def fill_target(color):
    target_surf.fill(color)

game_active = False
reflex_event = pygame.event.custom_type()
random_timer_int = randint(TIMER_MIN, TIMER_MAX)
pygame.time.set_timer(reflex_event, random_timer_int)

fill_target("red")

running = True
reaction_time = 0
start_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == reflex_event:
            fill_target("green")
            pygame.display.update((WINDOW_WIDTH / 2 - TARGET_SIZE / 2, WINDOW_HEIGHT / 2 - TARGET_SIZE / 2, TARGET_SIZE, TARGET_SIZE))
            start_time = pygame.time.get_ticks()
            game_active = True

        if event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_SPACE:
                reaction_time = float(pygame.time.get_ticks()) - start_time
                message = f"Your time: {reaction_time} ms"
                font_surf = font.render(message, True, "black")
                screen.blit(font_surf, (WINDOW_WIDTH / 2 - font_surf.get_width() / 2, WINDOW_HEIGHT / 2 + 300))
                pygame.display.update()
                game_active = False

    screen.blit(target_surf, (WINDOW_WIDTH / 2 - TARGET_SIZE / 2, WINDOW_HEIGHT / 2 - TARGET_SIZE / 2))

    pygame.display.update()

pygame.quit()
