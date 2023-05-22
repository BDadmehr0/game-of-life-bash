import pygame
import numpy as np

# initialize pygame
pygame.init()

# set the size of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set the size of the grid
grid_width = 80
grid_height = 60

# create a random initial state for the grid
grid = np.random.randint(2, size=(grid_height, grid_width))

# set the size of each cell in the grid
cell_width = screen_width // grid_width
cell_height = screen_height // grid_height

# set the colors for the cells
alive_color = (255, 255, 255)
dead_color = (0, 0, 0)

# define a function to update the grid
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(grid_height):
        for j in range(grid_width):
            neighbors = (
                grid[(i-1)%grid_height][(j-1)%grid_width] +
                grid[(i-1)%grid_height][j] +
                grid[(i-1)%grid_height][(j+1)%grid_width] +
                grid[i][(j-1)%grid_width] +
                grid[i][(j+1)%grid_width] +
                grid[(i+1)%grid_height][(j-1)%grid_width] +
                grid[(i+1)%grid_height][j] +
                grid[(i+1)%grid_height][(j+1)%grid_width]
            )
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the grid
    grid = update_grid(grid)

    # draw the grid
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j] == 1:
                color = alive_color
            else:
                color = dead_color
            pygame.draw.rect(screen, color, (j*cell_width, i*cell_height, cell_width, cell_height))

    # update the display
    pygame.display.flip()

# quit pygame
pygame.quit()
