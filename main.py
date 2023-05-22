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
