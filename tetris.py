## tetris game


import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
ROWS = SCREEN_HEIGHT // GRID_SIZE
COLS = SCREEN_WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Tetrominoes
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]], # Z
    [[0, 1, 0], [1, 1, 1]], # J
    [[1, 0, 0], [1, 1, 1]], # L
    [[1, 1, 1], [0, 1, 0]]  # T
]
COLORS = [CYAN, YELLOW, GREEN, RED, BLUE, MAGENTA, WHITE]

# Game variables
grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
current_piece = random.choice(SHAPES)
current_color = random.choice(COLORS)
current_x, current_y = COLS // 2 - len(current_piece[0]) // 2, 0

# Functions
def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
            pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_piece(piece, x, y, color):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j]:
                pygame.draw.rect(screen, color, ((x + j) * GRID_SIZE, (y + i) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(screen, WHITE, ((x + j) * GRID_SIZE, (y + i) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def check_collision(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j]:
                if x + j < 0 or x + j >= COLS or y + i >= ROWS:
                    return True
                if grid[y + i][x + j] != BLACK:
                    return True
    return False

def clear_lines():
    global grid
    full_lines = [y for y, row in enumerate(grid) if all(cell != BLACK for cell in row)]
    for line in full_lines:
        del grid[line]
        grid.insert(0, [BLACK for _ in range(COLS)])

# Main loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
fps = 4

running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collision(current_piece, current_x - 1, current_y):
                current_x -= 1
            if event.key == pygame.K_RIGHT and not check_collision(current_piece, current_x + 1, current_y):
                current_x += 1
            if event.key == pygame.K_DOWN and not check_collision(current_piece, current_x, current_y + 1):
                current_y += 1
            if event.key == pygame.K_UP:
                rotated = [list(row) for row in zip(*current_piece[::-1])]
                if not check_collision(rotated, current_x, current_y):
                    current_piece = rotated

    # Move piece down
    if not check_collision(current_piece, current_x, current_y + 1):
        current_y += 1
    else:
        for i in range(len(current_piece)):
            for j in range(len(current_piece[i])):
                if current_piece[i][j]:
                    grid[current_y + i][current_x + j] = current_color
        clear_lines()
        current_piece = random.choice(SHAPES)
        current_color = random.choice(COLORS)
        current_x, current_y = COLS // 2 - len(current_piece[0]) // 2, 0

    # Check for game over
    if check_collision(current_piece, current_x, current_y):
        running = False

    # Drawing
    draw_grid()
    draw_piece(current_piece, current_x, current_y, current_color)
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
