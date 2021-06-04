import pygame
import time

# Chọn background
bg = pygame.image.load('Pic/map1.jpg')
# Chọn resolution
width = 630
height = 630
# Chọn tốc độ bắn
reload_time = 50
# Quái
respawn_time = 3

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
max_score = [0, 0]
old_second = 0
time_pause = 0

from characters.projectile import *
from characters.player import *
from characters.Enemies import *

player = Player(width // 2, height // 2, 10, 10)
projectiles = Projectliles()
enemies = Enemies()

start = int(time.time())
min_sec = (0,0)

Color = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

run = True
run_play = True
setting = False
pause = False
lvlup = False
level = False
clicked = False