import pygame
import math
from config import *

class Projectile(object):
    """
           Class Projectile
           attr:
               x, y, angle, speed, spriteCount, animation
           method:
               __init__(self, x, y, width, height)
               draw(self, win)
               check(self, enemies)
               fire(self, x, y, projectiles)
    """
    def __init__(self, x, y, angle):
        """
        Khởi tạo một projectile
        input:
            x, y: vị trí tạo
            angle: góc di chuyển
        """
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 4
        self.spriteCount = 0
        self.animation = ['Pic/fireball.png']
    def draw(self, win):
        """
        Vẽ lên màn hình
        input:
            win: cửa sổ cần hiển thị
        """
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        animate = [pygame.image.load(self.animation[0])]
        win.blit(animate[self.spriteCount], (self.x-16, self.y-16))
        self.spriteCount += 1
        if self.spriteCount+1 > len(animate):
            self.spriteCount = 0
    def get_pos(self):
        """
        Lấy giá trị vị trí hiện tại
        output:
            tuple([x, y]): vị trí
        """
        return tuple([self.x, self.y])

class Projectliles(object):
    """
        Class Projectliles: Tập hợp tất cả projectile
        attr:
            enemies
        method:
            __init__(self)
            get_arr(self)
            create_projectile(self, x, y, target_x, target_y)
            show_projectiles(self, win)
            remove(self, projectile)
    """
    def __init__(self):
        """
        Khởi tạo list rỗng
        """
        self.projectiles = []
    def get_arr(self):
        """
        Lấy danh sách projectiles
        output:
            projectiles: list cách projectile
        """
        return self.projectiles
    def create_projectile(self, x, y, target_x, target_y):
        """
        Tạo projectile
        input:
            x, y: Vị trí tạo
            target_x, target_y: Vị trí đích
        """
        dx = target_x - x
        dy = target_y - y
        angle = math.atan2(dy, dx)
        projectile = Projectile(x, y, angle)
        self.projectiles.append(projectile)
    def show_projectiles(self, win):
        """
        Vẽ tất cả projectile lên màn hình
        input:
            win: cửa sổ cần hiển thị
        """
        for i in self.projectiles:
            i.draw(win)
    def remove(self, projectile):
        """
        Xóa một projectile khỏi list
        input:
            projectile: projectile cần xóa
        """
        self.projectiles.pop(self.projectiles.index(projectile))