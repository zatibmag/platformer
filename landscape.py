import pygame
from Person import man
from Skeleton import skeleton

bg1 = pygame.image.load('images/landscape/bg1.png')
bg1 = pygame.transform.scale(bg1, (1600, 800))
bg2 = pygame.image.load('images/landscape/bg2.png')
bg2 = pygame.transform.scale(bg2, (1600, 800))
bg3 = pygame.image.load('images/landscape/bg3.png')
bg3 = pygame.transform.scale(bg3, (1600, 800))
bg4 = pygame.image.load('images/landscape/bg4.png')
bg4 = pygame.transform.scale(bg4, (1600, 800))
bg5 = pygame.image.load('images/landscape/bg5.png')
bg5 = pygame.transform.scale(bg5, (1600, 800))
bg6 = pygame.image.load('images/landscape/bg6.png')
bg6 = pygame.transform.scale(bg6, (1600, 800))
bg7 = pygame.image.load('images/landscape/bg7.png')
bg7 = pygame.transform.scale(bg7, (1600, 800))
bg8 = pygame.image.load('images/landscape/bg8.png')
bg8 = pygame.transform.scale(bg8, (1600, 800))
bg = [bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8]
bgCount = 0

Welcome_pictures_tutorial = pygame.image.load('images/landscape/Welcome.png')
use_w_pictures_tutorial = pygame.image.load('images/landscape/use_w.png')
kill_pictures_tutorial = pygame.image.load('images/landscape/kill.png')
kill_agr_pictures_tutorial = pygame.image.load('images/landscape/kill_agr.png')
c_v_pictures_tutorial = pygame.image.load('images/landscape/c_v.png')
kill = [kill_pictures_tutorial, kill_agr_pictures_tutorial]

platform_grass = pygame.image.load('images/landscape/platform.png')


class platform_class():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        if tutorial.platform_grass_visible == 1:
            win.blit(platform_grass, (self.x, self.y))


class tutorial_class():
    def __init__(self, x, y, width, height):
        self.welcome = True
        self.use_w = False
        self.kill = False
        self.c_v = False
        self.tutorial1 = True
        self.tutorial2 = False
        self.tutorial3 = False
        self.tutorial4 = False
        self.tutorial_BLOCK = False
        self.platform_grass_visible = False
        self.boss_room = False
        self.kill_picture_count = 0
        self.skeleton_vision = 0
        self.Ogre_vision = 0


    def draw(self, win):
        if self.welcome == True and self.tutorial1 == True and self.tutorial_BLOCK == False:
            win.blit(Welcome_pictures_tutorial, (550, 100))

        if man.x and self.tutorial1 and self.tutorial2 == False and \
                self.tutorial_BLOCK == False and man.x < 550 or man.x > 850 and self.tutorial1 and \
                self.tutorial2 == False and self.tutorial_BLOCK == False:
            self.welcome = False
            self.use_w = True
            self.tutorial1 = False
            self.tutorial2 = True

        if self.use_w == True and self.tutorial1 == False and self.tutorial2 and self.tutorial_BLOCK == False:
            win.blit(use_w_pictures_tutorial, (550, 100))
            self.platform_grass_visible = True

        if man.isJump and self.tutorial2 == True and self.tutorial_BLOCK == False and man.x > 550  and man.x < 850:
            self.use_w = False
            self.tutorial2 = False
            self.tutorial3 = True

        if self.tutorial2 == False and self.tutorial3 and self.tutorial1 == False and self.tutorial_BLOCK == False:
            self.kill_picture_count += 1
            win.blit(kill[self.kill_picture_count // 60], (550, 100))
            if self.kill_picture_count + 1 == 60:
                self.skeleton_vision = 1
            if self.kill_picture_count + 1 == 120:
                    self.tutorial3 = False
                    self.tutorial4 = True
                    self.c_v = True
        if self.c_v == True and self.tutorial3 == False and self.tutorial4 and self.tutorial_BLOCK == False:
            win.blit(c_v_pictures_tutorial, (550, 100))
            if skeleton.dead == True:
                self.tutorial4 = False
                self.tutorial_BLOCK = True

        if skeleton.dead and self.Ogre_vision == 0:
            self.boss_room = True
            win.blit(pygame.image.load('images/landscape/boss_indicator.png'), (1200, 400))

        if man.x > 1550:
            self.skeleton_vision = 0
            self.platform_grass_visible = False
            self.Ogre_vision = 1
            self.platform_grass_vision = 0
            man.x = 20


platform = platform_class(550, 450, 488, 37)
tutorial = tutorial_class(1, 1, 1, 1)


