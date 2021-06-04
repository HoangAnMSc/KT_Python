import pygame
import math
from features.sound import sound_lazer

class Player(object):
    """
        Class Player
        attr:
            x, y, width, height, speed, walkCount, left, right, animation_r, animation_l, stay,
            health, maxhealth, exp, maxexp, level, fire_range, reloading
        method:
            __init__(self, x, y, width, height)
            draw(self, win)
            check(self, enemies)
            fire(self, x, y, projectiles)
    """
    def __init__(self, x, y, width, height):
        """
        Khởi tạo một player
        input:
            x, y: vị trí cần tạo
            width, height: chiều rộng chiều dài của player
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 2
        self.walkCount = 0
        self.left = False
        self.right = False
        self.animation_l = ['Pic/mage1.png', 'Pic/mage2.png', 'Pic/mage3.png', 'Pic/mage4.png']
        self.animation_r = ['Pic/m1l.png', 'Pic/m2l.png', 'Pic/m3l.png', 'Pic/m4l.png']
        self.stay = 'Pic/mage1.png'
        self.health = 30
        self.maxhealth = self.health
        self.exp = [0]
        self.maxexp = 10
        self.level = 0
        self.fire_range = 100
        self.reloading = 0

    def draw(self, win):
        """
        Vẽ nhân vật lên màn hình
        input:
            win: cửa sổ cần vẽ
        """
        #=========================health=======================
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.maxhealth / 2, self.y-40, self.maxhealth, 5)) #thanh máu
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x - self.health / 2, self.y- 40, self.health, 5))
        #=====================================================
        left = []
        for i in self.animation_l:
            left.append(pygame.image.load(i))
        right = []
        for i in self.animation_r:
            right.append(pygame.image.load(i))
        s = pygame.image.load(self.stay)
        if self.walkCount + 1 >= len(left)*15:
            self.walkCount = 0
        if self.left:
            win.blit((right[self.walkCount//15]), (self.x-32, self.y-32))
            self.walkCount += 1
        elif self.right:
            win.blit((left[self.walkCount//15]), (self.x-32, self.y-32))
            self.walkCount += 1
        else:
            win.blit(s, (self.x-32, self.y-32))
        pygame.draw.rect(win, (0, 0, 255), (0, 0, self.exp[0] / self.maxexp * pygame.display.get_window_size()[0], 5)) #thanh exp
            
    def check(self, enemies):
        """
        Kiểm tra có chạm phải enemy không
        input:
            enemies: list các enemy
        output:
            True/False: có chạm bất kì enemy nào không
        """
        for enemy in enemies.enemies:
            if self.health> 0:
                y_pos = tuple([self.x, self.y])
                ch = enemy.check(y_pos)
                if not ch:
                    self.health -= 0.2
                    return False
            else:
                return True

    def fire(self, x, y, projectiles):
        """
        Tạo các projectile theo hướng x,y
        input:
            x, y: vị trí bắn đạn đến
            projectiles: danh sách projectile hiện tại
        """
        if math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.fire_range:
            self.reloading = 0
            s_lazer = sound_lazer()
            s_lazer.play()
            projectiles.create_projectile(self.x, self.y, x, y)
