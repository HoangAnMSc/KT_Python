import pygame
from pygame import mixer

def sound_bg():
    return pygame.mixer.Sound("sound/sneak.mp3")
def sound_onii():
    return pygame.mixer.Sound("sound/onii.mp3")
def sound_pause():
    return pygame.mixer.Sound("sound/pause.mp3")
def sound_lazer():
    return pygame.mixer.Sound("sound/laser.wav")
def sound_gameover():
    return pygame.mixer.Sound("sound/baka.mp3")
def sound_enemy_hit():
    return pygame.mixer.Sound("sound/hit.mp3")