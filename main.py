import pygame
import math
from pygame.locals import *
from config import *
from features.button import *
from features.sound import *
from features.features import *
from features.SaveLoad import *
import time
from os import path

# ----------------------Create Button------------------
def create_button():
    '''
    Create Button Function
        Initialize All Buttons
            5 Button For Pause Function
            1 Button For Level Up Function
            3 Button For Game Over Function
            4 Button For Select Game Level Function
            4 Button For Menu Function
            3 Button For Setting Function
    '''
    # Pause Button
    button = Button('||', width - 30, 30, 30, 30, Color['black'], 'Pic/button2.png', 'Pic/button.png', Pause)
    buttons.add('pause', button)

    button = Button('Resume', width / 2, (height - 100) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', resume)
    buttons.add('resume', button)

    button = Button('Setting', width / 2, (height + 50) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', Setting)
    buttons.add('pause setting', button)
    
    button = Button('Main Menu', width / 2, (height + 200) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', return_menu)
    buttons.add('pause main menu', button)

    button = Button('Quit Game', width / 2, (height + 350) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', QuitGame)
    buttons.add('pause quit game', button)

    # Level Up Button
    button = Button('Level Up', width / 2, height / 4 * 3, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', resume)
    buttons.add('level up', button)

    # Button Game Over
    button = Button('Play Again', width / 4, height - 150, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', resume)
    buttons.add('play again', button)
    
    button = Button('Main Menu', width * 3 / 4, height - 150, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', return_menu)
    buttons.add('over main menu', button)
    
    button = Button('Quit Game', width / 2, height - 100, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', QuitGame)
    buttons.add('over quit game', button)

    # Button Select Level
    button = Button('Easy', width / 2, (height - 200) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', easy)
    buttons.add('easy', button)
    
    button = Button('Normal', width / 2, (height - 50) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', normal)
    buttons.add('normal', button)
    
    button = Button('Hard', width / 2, (height + 100) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', hard)
    buttons.add('hard', button)
    
    button = Button('Back', width / 2, (height + 250) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', return_menu)
    buttons.add('back', button)

    # Menu Buttons
    button = Button('Continue', width / 2, (height - 200) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', Continue)
    buttons.add('continue', button)
    
    button = Button('New Game', width / 2, (height - 50) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', NewGame)
    buttons.add('new game', button)
    
    button = Button('Setting', width / 2, (height + 100) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', Setting)
    buttons.add('menu setting', button)
    
    button = Button('Quit Game', width / 2, (height + 250) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', QuitGame)
    buttons.add('menu quit game', button)

    # Setting Buttons
    button = Button('Bật nhạc', width / 2, (height - 200) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png',bat)
    buttons.add('setting bat nhac', button)
    
    button = Button('Tắt nhạc', width / 2, (height - 50) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', tat)
    buttons.add('setting tat nhac', button)
    
    button = Button('Back', width / 2, (height + 100) / 2, 100, 50, Color['black'], 'Pic/button2.png', 'Pic/button.png', resume)
    buttons.add('setting back', button)

# ----------------------Resume Game------------------
def reset():
    '''
    Reset All Data When Game Over or Select New Game Mode
        Create New Player, Enemies, Projectitles
        Reset Time Of Game
    '''
    global player, projectiles, enemies, start, old_second, time_pause, start
    player = Player(width // 2, height // 2, 10, 10)
    projectiles = Projectliles()
    enemies = Enemies()
    old_second = 0
    time_pause = 0
    start = int(time.time())

# ----------------------Quit Game------------------
def QuitGame():
    '''
    Quit Game When Click "Quit Game" Button Or "X" Button
        Break Out All Loop
        Save The Game Before Quit
    '''
    global run, run_play, pause, level, lvlup, setting
    global player, enemies, projectiles, projectile_speed
    global reload_time, respawn_time, enemy_speed, time_pause, start
    run = False
    run_play = False
    pause = False
    level = False
    lvlup = False
    setting = False
    last_time = int(time.time())
    Save((player, enemies, projectiles,
    projectile_speed, reload_time, 
    respawn_time, enemy_speed, time_pause, start, last_time))

# ----------------------Return Menu------------------
def return_menu():
    '''
    Return To Menu When Click "Main Menu" Button
        Break Out All Loop To Back To The Main Menu Screen
        Save The Game Before Return To Menu Screen
    '''
    global run_play, pause, level, setting
    run_play = False
    pause = False
    level = False
    setting = False
    last_time = int(time.time())
    Save((player, enemies, projectiles,
    projectile_speed, reload_time, 
    respawn_time, enemy_speed, time_pause, start, last_time))

# ----------------------Resume Game------------------
def resume():
    '''
    Return To 1 screen before
    '''
    global pause, lvlup, setting
    if not setting:
        pause = False
    lvlup = False
    setting = False

# ----------------------trả về thời gian game------------------
def thoi_gian():
    '''
    Return time from the begining of game to now
    '''
    temp_time = int(time.time()) - start - time_pause
    return temp_time // 60, temp_time % 60

def draw1():
    global min_sec
    # Hình nền
    win.blit(bg, (0, 0))
    # Print Time
    time_text = '{}{}:{}{}'.format(min_sec[0] // 10, min_sec[0] % 10, min_sec[1] // 10, min_sec[1] % 10)
    show_text(time_text, 'consolas', 20, 0, 30, width, 0, Color['blue'])
    pygame.draw.rect(win, Color['black'], (10, 10, width - 20, height - 20), 10)
    # Projectiles
    projectiles.show_projectiles(win)
    # Enemies
    enemies.show_enemies(win)

# ----------------------Pause Game------------------
def Pause():
    global time_pause, clicked, pause
    pause = True
    s_pause = sound_pause()
    s_pause.play()
    start_pause = int(time.time())
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            if event.type == KEYUP:
                if event.key == K_p:
                    pause = False
        draw1()
        player.draw(win)
        rect = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, 180))
        win.blit(rect, (0, 0))
        show_text('PAUSE', 'consolas', 50, 0, 0, width, height - 250, Color['white'])
        buttons.draw(win, ['resume', 'pause setting', 'pause main menu', 'pause quit game'])
        if pygame.mouse.get_pressed()[0] and clicked == False:
            clicked = True
            buttons.clicked(['resume', 'pause setting', 'pause main menu', 'pause quit game'], pygame.mouse.get_pos())
        elif not pygame.mouse.get_pressed()[0]:
            clicked = False
        pygame.display.update()
    s_pause.stop()
    pygame.mixer.unpause()    
    time_pause += int(time.time()) - start_pause

# ----------------------Game Over------------------
def gameOver():
    global max_score, clicked, pause
    min_sec = thoi_gian()
    if (max_score[0] < min_sec[0]) or (max_score[0] == min_sec[0] and max_score[1] < min_sec[1]):
        max_score = min_sec
        show_text('New High Score', 'consolas', 50, 0, 0, width, height - 50, Color['green'])
    else:
        show_text('Game Over', 'consolas', 50, 0, 0, width, height - 50, Color['green'])
    score_text = 'Survival Time : {}{}:{}{}'.format(min_sec[0] // 10, min_sec[0] % 10, min_sec[1] // 10, min_sec[1] % 10)
    maxscore_text = 'Best Survival Time : {}{}:{}{}'.format(max_score[0] // 10, max_score[0] % 10, max_score[1] // 10, max_score[1] % 10)
    show_text(score_text, 'consolas', 30, 0, 0, width, height + 50, Color['green'])
    show_text(maxscore_text, 'consolas', 30, 0, 0, width, height + 150, Color['green'])
    sound_gameover()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        reset()
        buttons.draw(win, ['play again', 'over quit game', 'over main menu'])
        if pygame.mouse.get_pressed()[0] and clicked == False:
            clicked = True
            buttons.clicked(['play again', 'over quit game', 'over main menu'], pygame.mouse.get_pos())
        elif not pygame.mouse.get_pressed()[0]:
            clicked = False        
        pygame.display.update()

# ----------------------Show Stats------------------
def show_stat():
    global reload_time
    player.exp[0] %= player.maxexp
    player.maxexp *= 2
    show_text('Level: {}'.format(player.level), 'consolas', 20, 0, 0, width / 2, height / 3, Color['blue'])
    player.level += 1
    show_text('Level: {}'.format(player.level), 'consolas', 20, width / 2, 0, width / 2, height / 3, Color['red'])
    show_text('Hp: {}'.format(int(player.health)), 'consolas', 20, 0, 50, width / 2, height / 3, Color['blue'])
    if player.health + 1 <= player.maxhealth:
        show_text('Hp: {} + (1)'.format(int(player.health)), 'consolas', 20, width / 2, 50, width / 2, height / 3, Color['red'])
        player.health += 1
    else:
        show_text('Hp: {}'.format(int(player.health)), 'consolas', 20, width / 2, 50, width / 2, height / 3, Color['red'])
    #player.health = player.maxhealth
    show_text('Speed: {}'.format(player.speed), 'consolas', 20, 0, 100, width / 2, height / 3, Color['blue'])
    if player.speed < 5:
        show_text('Speed: {} + (1)'.format(player.speed), 'consolas', 20, width / 2, 100, width / 2, height / 3, Color['red'])
        player.speed += 1
    else:
        show_text('Speed: {}'.format(player.speed), 'consolas', 20, width / 2, 100, width / 2, height / 3, Color['red'])
    show_text('Fire Range: {}'.format(player.fire_range), 'consolas', 20, 0, 150, width / 2, height / 3, Color['blue'])
    if player.fire_range < 150:
        show_text('Fire Range: {} + (5)'.format(player.fire_range), 'consolas', 20, width / 2, 150, width / 2, height / 3, Color['red'])
        player.fire_range += 5
    else:
        show_text('Fire Range: {}'.format(player.fire_range), 'consolas', 20, width / 2, 150, width / 2, height / 3, Color['red'])
    show_text('Reload Time: {}'.format(reload_time), 'consolas', 20, 0, 200, width / 2, height / 3, Color['blue'])
    if reload_time > 20:
        show_text('Reload Time: {} - (5)'.format(reload_time), 'consolas', 20, width / 2, 200, width / 2, height / 3, Color['red'])
        reload_time -= 5
    else:
        show_text('Reload Time: {}'.format(reload_time), 'consolas', 20, width / 2, 200, width / 2, height / 3, Color['red'])

# ----------------------Level Up------------------
def LevelUp():
    global lvlup, clicked, time_pause
    if player.exp[0] >= player.maxexp:
        lvlup = True
        rect = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, 180))
        win.blit(rect, (0, 0))
        show_stat()
        start_pause = int(time.time())
        while lvlup:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    QuitGame()
            buttons.draw(win, ['level up'])
            if pygame.mouse.get_pressed()[0] and clicked == False:
                clicked = True
                buttons.clicked(['level up'], pygame.mouse.get_pos())
            elif not pygame.mouse.get_pressed()[0]:
                clicked = False
            pygame.display.update()
        time_pause += int(time.time()) - start_pause


# ----------------------Tạo giao diện------------------
def reDraw():
    global clicked, old_second, min_sec
    # Tạo quái
    min_sec = thoi_gian()
    if min_sec[0] * 60 + min_sec[1] - old_second > respawn_time:
        n = random.randint(1, 3)
        for i in range(n):
            enemies.create_enemy()
        old_second = min_sec[0] * 60 + min_sec[1]
    draw1()
    enemies.update_enemies((player.x, player.y), projectiles, player.exp)
    # Player
    pygame.draw.circle(win, (255, 255, 0), (player.x, player.y), player.fire_range, 2)
    player.draw(win)
    buttons.draw(win, ['pause'])
    if pygame.mouse.get_pressed()[0] and clicked == False:
        clicked = True
        buttons.clicked(['pause'], pygame.mouse.get_pos())
    elif not pygame.mouse.get_pressed()[0]:
        clicked = False
    LevelUp()
    pygame.display.update()

# ---------------------Movement---------------------
def Movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x > 40:
        player.x -= player.speed
        player.left = True
        player.right = False
    if keys[pygame.K_d] and player.x < width - 40:
        player.x += player.speed
        player.left = False
        player.right = True
    if keys[pygame.K_w] and player.y > 40:
        player.y -= player.speed
    if keys[pygame.K_s] and player.y < height - 40:
        player.y += player.speed
    if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
        player.left = False
        player.right = False

# ---------------------Shooting---------------------
def Shooting():
    if player.reloading < reload_time:
        player.reloading += 1
    elif enemies.get_len() > 0:
        x, y = enemies.get_close(player.x, player.y)
        player.fire(x, y, projectiles)

# ---------------------MAIN---------------------
def Play():
    global time_pause, max_score
    while run_play:
        pygame.time.delay(10)
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            if event.type == KEYUP:
                if event.key == K_p:
                    Pause()

        if run_play == False:
            break
        # Movement
        Movement()
        # Shooting
        Shooting()
        # Check Game Over
        if player.check(enemies):
            pygame.mixer.pause()
            s_over = sound_gameover()
            s_over.play()
            gameOver()
            pygame.mixer.unpause()
        reDraw()

# ---------------------Level Game---------------------
def level_game():
    global clicked, level, start_pause
    level = True
    start_pause = int(time.time())
    while level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        win.blit(bg, (0, 0))
        show_text('SURVIVALS', 'consolas', 50, 0, 0, width, height / 4, Color['blue'])
        buttons.draw(win, ['easy', 'normal', 'hard', 'back'])
        if pygame.mouse.get_pressed()[0] and clicked == False:
            clicked = True
            buttons.clicked(['easy', 'normal', 'hard', 'back'], pygame.mouse.get_pos())
        elif not pygame.mouse.get_pressed()[0]:
            clicked = False
        pygame.display.update()

# ---------------------Easy---------------------
def easy():
    global projectile_speed, reload_time, respawn_time, enemy_speed, time_pause
    # Chọn tốc độ bắn
    player.fire_range = 120
    projectile_speed = 4
    reload_time = 30
    # Quái
    respawn_time = 5
    enemy_speed = 100
    time_pause += int(time.time()) - start_pause
    Play()

# ---------------------Normal---------------------
def normal():
    global projectile_speed, reload_time, respawn_time, enemy_speed, time_pause
    # Chọn tốc độ bắn
    player.fire_range = 110
    projectile_speed = 4
    reload_time = 40
    # Quái
    respawn_time = 3
    enemy_speed = 120
    time_pause += int(time.time()) - start_pause
    Play()

# ---------------------Hard---------------------
def hard():
    global projectile_speed, reload_time, respawn_time, enemy_speed, time_pause
    # Chọn tốc độ bắn
    player.fire_range = 100
    projectile_speed = 4
    reload_time = 50
    # Quái
    respawn_time = 3
    enemy_speed = 150
    time_pause += int(time.time()) - start_pause
    Play()

# ---------------------New Game---------------------
def NewGame():
    reset()
    level_game()

# ---------------------Continue---------------------
def Continue():
    global player, enemies, projectiles, projectile_speed, reload_time, respawn_time, enemy_speed, time_pause, start
    (player, enemies, projectiles,
    projectile_speed, reload_time, 
    respawn_time, enemy_speed, time_pause, start, last_time) = Load()
    time_pause += int(time.time()) - last_time
    Play()

# ----------------------Setting--------------------
def Setting():
    global setting, clicked
    setting = True
    while setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        win.blit(bg, (0, 0))
        show_text('Âm Thanh', 'consolas', 50, 0, 0, width, height / 4, Color['blue'])
        buttons.draw(win, ['setting bat nhac', 'setting tat nhac', 'setting back'])
        if pygame.mouse.get_pressed()[0] and clicked == False:
            clicked = True
            buttons.clicked(['setting bat nhac', 'setting tat nhac', 'setting back'], pygame.mouse.get_pos())
        elif not pygame.mouse.get_pressed()[0]:
            clicked = False
        pygame.display.update()
        
def bat():
    s_bg.play(-1)
def tat():
    s_bg.stop()

# ---------------------MENU---------------------
def Menu():
    while run:
        global run_play, clicked
        run_play = True
        pygame.mixer.unpause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        win.blit(bg, (0, 0))
        show_text('SURVIVALS', 'consolas', 50, 0, 0, width, height / 4, Color['blue'])
        if path.exists('./data/game.dat'):
            buttons.draw(win, ['continue', 'new game', 'menu setting', 'menu quit game'])
            if pygame.mouse.get_pressed()[0] and clicked == False:
                clicked = True
                buttons.clicked(['continue', 'new game', 'menu setting', 'menu quit game'], pygame.mouse.get_pos())
            elif not pygame.mouse.get_pressed()[0]:
                clicked = False
        else:
            buttons.draw(win, ['new game', 'menu setting', 'menu quit game'])
            if pygame.mouse.get_pressed()[0] and clicked == False:
                clicked = True
                buttons.clicked(['new game', 'menu setting', 'menu quit game'], pygame.mouse.get_pos())
            elif not pygame.mouse.get_pressed()[0]:
                clicked = False
        pygame.display.update()


clicked = False
s_bg = sound_bg()
s_bg.play(-1)
buttons = Buttons()
create_button()
Menu()
pygame.quit()
