import pygame
import random
import math
from abc import ABC, abstractmethod
from config import *
from features.sound import sound_enemy_hit, sound_onii
from characters.projectile import *

monster_hp = {
    "Slime_Blue": 1,
    "Slime_Green": 2
}

class monster():
    """
    Class monster
    attr:
        __speed, spriteCount, pos, maxhp, hp
    method:
        __init__(self, pos)
        move_to(self, target_pos)
        set_pos(self, pos)
        get_pos(self)
        get_hp(self)
        hit(self)
        check(self, pos)
        show(self, win)
    """
    def __init__(self, pos):
        """
        Khoi tao voi vi tri (pos) duoc cho
        input:
            pos: vị trí (x, y)
        """
        self.__speed = 1
        self.spriteCount = 0
        self.pos = pos
        # self.__animation = []
        self.maxhp = self.hp

    def move_to(self, target_pos):
        """
        thay doi x, y cua obj sao cho huong toi vi tri cua doi tuong (target_pos) voi viec tinh tan()
        input:
            target_pos: vị trí đích (x, y)
        """
        # tính góc
        x = self.pos[0]
        y = self.pos[1]
        dx = target_pos[0] - x
        dy = target_pos[1] - y
        angle = math.atan2(dy, dx)
        # di chuyển theo góc
        x += self.__speed * math.cos(angle)
        y += self.__speed * math.sin(angle)
        return tuple([x, y])

    def set_pos(self, pos):
        """
        set lai vi tri cua obj
        input:
            pos: vị trí (x, y)
        """
        self.pos = pos

    def get_pos(self):
        """
        tra ve vi tri cua obj
        output:
            pos: vị trí (x, y)
        """
        return self.pos

    def get_hp(self):
        """
        tra ve gia tri mau cua obj
        output:
            hp: máu
        """
        return self.hp

    def hit(self):
        """
        giam gia tri hp cua obj
        """
        self.hp -= 1

    def check(self, pos2):
        """
        kiem tra obj voi vi tri cua doi tuong co giao nhau hay khong?
        output:
            True/False: có giao nhau hay không
        """
        r1 = 12
        r2 = 12
        pos1 = self.get_pos()
        (x1, y1), (x2, y2) = pos1, pos2
        distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        radSumSq = (r1 + r2) * (r1 + r2)
        if (distSq > radSumSq):
            return True
        else:
            return False
    
    @abstractmethod
    def show(self, win):
        """
        hien thi obj len man hinh
        """
        animate = []
        for i in self.animation:
            animate.append(pygame.image.load(i))
        win.blit(animate[self.spriteCount // 10], (self.pos[0] - 32, self.pos[1] - 32))
        self.spriteCount += 1
        if self.spriteCount + 1 > len(animate) * 10:
            self.spriteCount = 0

class Slime_Blue(monster):
    def __init__(self, pos):
        self.hp = monster_hp["Slime_Blue"]
        monster.__init__(self, pos)
        self.animation = ['Pic/monsters/slime_blue_0.png', 'Pic/monsters/slime_blue_1.png', 'Pic/monsters/slime_blue_2.png', 'Pic/monsters/slime_blue_3.png',
                          'Pic/monsters/slime_blue_4.png', 'Pic/monsters/slime_blue_5.png', 'Pic/monsters/slime_blue_6.png', 'Pic/monsters/slime_blue_7.png']

    def show(self, win):
        monster.show(self, win)

class Slime_Green(monster):
    def __init__(self, pos):
        self.hp = monster_hp["Slime_Green"]
        monster.__init__(self, pos)
        self.animation = ['Pic/monsters/slime_green_0.png', 'Pic/monsters/slime_green_1.png', 'Pic/monsters/slime_green_2.png', 'Pic/monsters/slime_green_3.png',
                          'Pic/monsters/slime_green_4.png', 'Pic/monsters/slime_green_5.png', 'Pic/monsters/slime_green_6.png', 'Pic/monsters/slime_green_7.png']

    def show(self, win):
        monster.show(self, win)

class Enemies:
    """
    Class Enemies: tap hop tat ca obj enemy
    attr:
        enemies
    method:
        __init__(self)
        get_len(self)
        create_enemy(self)
        show_enemies(self, win)
        update_enemies(self, pos, projectiles, score)
        get_close(self, x, y)
    """
    def __init__(self):
        """
        khoi tao tap hop enemies rong
        """
        self.enemies = []
    def get_len(self):
        """
        tra ve so luong enemies dang co
        output:
            số lượng enemy
        """
        return len(self.enemies)
    def create_enemy(self):
        """
        tao ngau nhien enemy voi vi tri ngoai cua so game va them vao tap hop enemies
        """
        size = pygame.display.get_window_size()
        pos = (random.randint(-20,size[0] + 20), random.randint(-20,size[1] + 20))
        while pos[0] in range(size[0]) and pos[1] in range(size[1]):
            pos = (random.randint(-20,size[0] + 20), random.randint(-20,size[1] + 20))
        i = random.randint(0, 1)
        if i==0:
            enemy = Slime_Blue(pos)
        elif i==1:
            enemy = Slime_Green(pos)
        self.enemies.append(enemy)
        
    def show_enemies(self, win):
        """
        hien thi tat ca enemies len win
        input:
            win: cửa sổ cần hiển thị
        """
        for e in self.enemies:
            e.show(win)
        
    def update_enemies(self, pos, projectiles, score):
        """
        cap nhat lai vi tri cua tat ca enemy va xoa di nhung enemy nao bi trung dan cua player
        input:
            pos: vị trí của player
            projectiles: list các projectile
            score: điểm số
        """
        for i, x in enumerate(self.enemies):
            x_pos = x.get_pos()
            x_pos1 = x.move_to(pos)
            if len(self.enemies) > 1:
                for j, y in enumerate(self.enemies):
                    y_pos = y.get_pos()
                    ch = x.check(y_pos)
                    if i != j and ch:
                        x.set_pos(x_pos1)
                    elif i !=j and not ch:
                        pos1 = tuple([3 * x_pos[0] - 2 * y_pos[0], x_pos[1] - y_pos[1]])
                        x.set_pos(x.move_to((pos1[0], pos[1])))
                        x.set_pos(x.move_to((pos[0], pos1[1])))
            else:
                x.set_pos(x_pos1)
            for projectile in projectiles.projectiles:
                y_pos = projectile.get_pos()
                ch = x.check(y_pos)
                if not ch:
                    s_hit = sound_enemy_hit()
                    s_hit.play()
                    x.hit()
                    if x.get_hp()==0:
                        self.enemies.remove(x)
                        score[0] += x.maxhp
                    projectiles.remove(projectile)

    def get_close(self, x, y):
        """
        tra ve vi tri cua enemy gan nhat
        input:
            x, y: điểm cần kiểm tra
        output:
            xt, yt: vị trí của quái vật gần nhất
        """
        dist = 9999999
        xt = 0
        yt = 0
        for i in self.enemies:
            xx, yy = i.get_pos()
            d = (xx-x)**2 + (yy-y)**2
            if d<dist:
                dist = d
                xt = xx
                yt = yy
        return xt, yt