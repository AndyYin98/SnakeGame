import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GAME_SPEED = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control game speed
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def main():
    snake = [[160, 160], [140, 160], [120, 160]]
    direction = 'RIGHT'
    food = [random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE]
    game_over = False


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'


        # Move the snake
        if direction == 'RIGHT':
            head = [snake[0][0] + CELL_SIZE, snake[0][1]]
        elif direction == 'LEFT':
            head = [snake[0][0] - CELL_SIZE, snake[0][1]]
        elif direction == 'UP':
            head = [snake[0][0], snake[0][1] - CELL_SIZE]
        elif direction == 'DOWN':
            head = [snake[0][0], snake[0][1] + CELL_SIZE]

        # Check if snake hits the boundaries
        if head[0] >= WIDTH or head[0] < 0 or head[1] >= HEIGHT or head[1] < 0:
            game_over = True

        # Check if snake hits itself
        if head in snake:
            game_over = True

        snake.insert(0, head)
        
        # Check if snake eats the food
        if head == food:
            food = [random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE,
                    random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE]
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        pygame.display.update()

        clock.tick(GAME_SPEED)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
