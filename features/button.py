import pygame
from features.text import *

class Button():
    '''
        Class Button
        attr:
            x, y, text, width, height, text_color, button_color, hovered_color, action
        method:
            draw(self, win)
            click(self)
    '''
    def __init__(self, text, x, y, width, height, text_color, button_color, hovered_color, action = None, text_size = 20):
        """Initialize Button
            Args:
                text: noi dung trong button - string
                x, y: vi tri cua button tren window - (int, int)
                width, height: kich co cua button - (int, int)
                text_color: mau cua text - color (int, int, int)
                button_color: mau cua button khi khong tro chuot - string, color(int, int, int)
                hovered_color: mau cua button khi tro chuot - string, color(int, int, int)
                action: method, funtion
                text_size: text size - int - default = 20
            Return:
                Button: object of Button class
        """
        self.x = x - width / 2
        self.y = y - height / 2
        self.text = Text(text, 'consolas', text_size, self.x, self.y, width, height, text_color)
        self.width = width
        self.height = height
        self.text_color = text_color
        self.button_color = button_color
        self.hovered_color = hovered_color
        self.action = action

    def draw(self, win):
        """Draw Button on window
            Args:
                win: khung anh can ve len - pygame.display
            Return:
                None
        """
        mouse = pygame.mouse.get_pos()
        if (self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height):
            if type(self.hovered_color) == str:
                button = pygame.image.load(self.hovered_color)
                button = pygame.transform.scale(button, (self.width, self.height))
                win.blit(button, (self.x, self.y))
            else:
                pygame.draw.rect(win, self.hovered_color, (self.x, self.y, self.width, self.height))
        else:
            if type(self.button_color) == str:
                button = pygame.image.load(self.button_color)
                button = pygame.transform.scale(button, (self.width, self.height))
                win.blit(button, (self.x, self.y))
            else:
                pygame.draw.rect(win, self.button_color, (self.x, self.y, self.width, self.height))
        self.text.draw(win)

    def clicked(self):
        """Check button is clicked
            Args:
                None
            Return:
                None
        """
        if self.action != None:
            self.action()


class Buttons():
    '''
        Class Buttons
        attr:
            buttons
        method:
            add(self, name_button, button)
            draw(self, win, name_button)
            clicked(self, name_buttons, mouse)
    '''
    def __init__(self):
        """Initialize Button
            Args:
            Return:
                Buttons: object of Buttons class
        """
        self.buttons = {}
    
    def add(self, name_button, button):
        """Draw All Chosen Button on window
            Args:
                name_buttons: ten cua button muon duoc ve - string, list of string
                button: class Button
            Return:
                None
        """
        self.buttons[name_button] = button

    def draw(self, win, name_buttons):
        """Draw All Chosen Button on window
            Args:
                win: khung anh can ve len - pygame.display
                name_buttons: ten cua button muon duoc ve - string, list of string
            Return:
                None
        """
        for i in name_buttons:
            self.buttons[i].draw(win)

    def clicked(self, name_buttons, mouse):
        """Check All Chosen Button on window is clicked
            Args:
                name_buttons: ten cua button muon duoc chon de check - string, list of string
                mouse: vi tri cua con tro - (int, int)
            Return:
                None
        """
        for i in name_buttons:
            if self.buttons[i].x <= mouse[0] <= self.buttons[i].x + self.buttons[i].width and self.buttons[i].y <= mouse[1] <= self.buttons[i].y + self.buttons[i].height:
                self.buttons[i].clicked()
                break