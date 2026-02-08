import pygame
import random
import sys


# Initialize pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game (Pygame)")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)


# Colors

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (100, 255, 100)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


# Game variables

snake = [(300, 300)]
direction = (0, 0)

food = (
    random.randrange(0, WIDTH, BLOCK_SIZE),
    random.randrange(0, HEIGHT, BLOCK_SIZE)
)

score = 0


# Drawing functions

def draw_snake():
    for block in snake:
        pygame.draw.rect(
            screen,
            LIGHT_GREEN,
            (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
        )

def draw_food():
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
    )

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


# Input handling

def handle_input():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)


# Main game loop

while True:
    clock.tick(10)
    handle_input()

    if direction != (0, 0):
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Wall or self collision
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # Food collision
        if new_head == food:
            score += 10
            food = (
                random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE)
            )
        else:
            snake.pop()

    screen.fill(BLACK)
    draw_food()
    draw_snake()
    draw_score()
    pygame.display.update()
