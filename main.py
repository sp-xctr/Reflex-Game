import pygame
from random import randint

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
TARGET_SIZE = 200
TIMER_MIN, TIMER_MAX = 5000, 10000

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Reflex Game")

# Font
font = pygame.font.Font(None, 50)

# Create target surface once
target_surf = pygame.Surface((TARGET_SIZE, TARGET_SIZE))

# Fill the display surface with blue
screen.fill("blue")

# Helper functions to fill colors
def fill_target(color):
    target_surf.fill(color)

# Game variables
game_active = False
reflex_event = pygame.event.custom_type()
random_timer_int = randint(TIMER_MIN, TIMER_MAX)
pygame.time.set_timer(reflex_event, random_timer_int)

# Fill the target red at the start
fill_target("red")

# Main game loop
running = True
reaction_time = 0
start_time = 0

while running:
    for event in pygame.event.get():
        # Handle quitting the game
        if event.type == pygame.QUIT:
            running = False

        # Triggered when the reflex event timer expires
        if event.type == reflex_event:
            fill_target("green")
            pygame.display.update((WINDOW_WIDTH / 2 - TARGET_SIZE / 2, WINDOW_HEIGHT / 2 - TARGET_SIZE / 2, TARGET_SIZE, TARGET_SIZE))
            start_time = pygame.time.get_ticks()  # Record the time when the target turns green
            game_active = True

        # Handle key press events if the game is active
        if event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_SPACE:  # Check for space key press
                reaction_time = float(pygame.time.get_ticks()) - start_time  # Calculate reaction time
                message = f"Your time: {reaction_time} ms"
                font_surf = font.render(message, True, "black")
                screen.blit(font_surf, (WINDOW_WIDTH / 2 - font_surf.get_width() / 2, WINDOW_HEIGHT / 2 + 300))
                pygame.display.update()  # Only update the relevant part of the screen
                game_active = False

    # Draw the target surface at the center
    screen.blit(target_surf, (WINDOW_WIDTH / 2 - TARGET_SIZE / 2, WINDOW_HEIGHT / 2 - TARGET_SIZE / 2))

    # Avoid redundant updates; only update when needed
    pygame.display.update()

# Quit Pygame when the loop ends
pygame.quit()
