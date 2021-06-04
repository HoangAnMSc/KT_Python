import pygame

class Text():
    def __init__(self, text, font, size, x, y, width, height, color):
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect()
        self.rect.center = ((x + width / 2, y + height / 2))

    def draw(self, win):
        win.blit(self.text, self.rect)
