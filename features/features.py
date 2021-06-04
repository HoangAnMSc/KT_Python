import pygame
from config import *

# ----------------------Text------------------
def show_text(txt, font, size, x, y, width, height, color):
    """Draw Text on window
        Args:
            txt: chu muon ve - string
            font: font chu - string
            size: kich co cua chu - int
            x, y: vi tri bat dau cua chu - (int, int)
            widht, heigth: vi tri ke thuc cua chu - (int, int)
            color: mau cua chu - (int, int, int)
        Return:
            None
    """
    sfont = pygame.font.SysFont(font, size)
    ssurf = sfont.render(txt, True, color)
    srect = ssurf.get_rect()
    srect.center = ((x + width / 2, y + height / 2))
    win.blit(ssurf, srect)
