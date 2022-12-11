import pygame.display

# Settings for the game
fps = 60
default_x_size = 1000
default_y_size = 500
fullscreen = False

# timers info
fs_start_time = 0
fs_is_pressed = False
fs_delay = 20

# Different scenes
"""
0 = main
1 = settings
2 = level selector
10 - 99 = levels
"""
sc_selector = 0

# Colors
DARK_BLUE = (8, 19, 169)
GREEN = (8, 166, 11)
YELLOW = (255, 226, 10)