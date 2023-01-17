import pygame
from Person import man
from Skeleton import skeleton
from Boss import Ogre
from landscape import platform
from landscape import bg
from landscape import bgCount
from landscape import tutorial

pygame.init()  # создание окна

pygame.display.set_caption("platformer")  # название окна

win = pygame.display.set_mode((1600, 800))


clock = pygame.time.Clock()

def redrawGameWindow():
    if tutorial.Ogre_vision == 1:
        Ogre.draw(win)
    if tutorial.skeleton_vision == 1:
        skeleton.draw(win)
    platform.draw(win)
    man.draw(win)
    tutorial.draw(win)
    if man.Dead == True:
        win.blit(pygame.image.load('images/player/dead_screen.jpg'), (0, 0))
    pygame.display.update()

run = True


while run:
    win.blit(bg[bgCount // 3], (0, 0))
    bgCount += 1
    if bgCount + 1 == 25:
        bgCount = 0
    clock.tick(30)         # скорость тиков

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if man.deadCount == 0 and man.Hit_True == False:
        if man.right and keys[pygame.K_c]:
            man.hitboxShieldRight = True
            man.defend = True
            man.isJump = False
            man.right = True
            man.left = False
            man.standing = False
        elif man.left and keys[pygame.K_c]:
            man.hitboxShieldLeft = True
            man.defend = True
            man.isJump = False
            man.right = False
            man.left = True
            man.standing = False
        else:
            man.defend = False
            man.hitboxShieldRight = False
            man.hitboxShieldLeft = False
            man.standing = True

        if not(man.defend == True):

            if man.right and keys[pygame.K_v]:
                man.hitboxAttackRight = True
                man.attack = True
                man.right = True
                man.left = False
                man.standing = False
            elif man.left and keys[pygame.K_v]:
                man.hitboxAttackLeft = True
                man.attack = True
                man.right = False
                man.left = True
                man.standing = False
            elif keys[pygame.K_a] and man.x > man.vel and man.deadCount == 0 and man.Hit_True == False and Ogre.death == False:
                man.x -= man.vel
                man.right = False
                man.left = True
                man.standing = False
                if man.x + 75 <= platform.x and man.y < 500 or man.x + 45 >= platform.x + platform.width and man.y < 500:
                    man.isJump = True
            elif tutorial.boss_room == True and keys[pygame.K_d] and man.x < 1800 - man.width - man.vel and man.deadCount == 0 and man.Hit_True == False and Ogre.death == False:
                    man.x += man.vel
                    man.right = True
                    man.left = False
                    man.standing = False
                    if man.x + 75 <= platform.x and man.y < 500 or man.x + 45 >= platform.x + platform.width and man.y < 500:
                        man.isJump = True
            elif keys[pygame.K_d] and man.x < 1550 - man.width - man.vel and man.deadCount == 0 and man.Hit_True == False and Ogre.death == False:   #невидимая стенка(сделал так же как я с платформой)
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
                if man.x + 75 <= platform.x and man.y < 500 or man.x + 45 >= platform.x + platform.width and man.y < 500:
                    man.isJump = True
            else:
                man.hitboxAttackRight = False
                man.hitboxAttackLeft = False
                man.attack = False
                man.attack = 0
                man.standing = True
                man.walkCount = 0

            if not(man.isJump):
                if keys[pygame.K_w]:
                    man.right = False
                    man.left = False
                    man.walkCount = 0
                    man.isJump = True
            if man.isJump == True:
                if man.jumpCount >= -10:                    # значение прыжка всегда становится на -1(т.е. выше)
                    neg = 1                                 # квадрат чтоб всегда было число +, но при этом чел не шёл вниз
                    if man.jumpCount <= 0:                  # деление чтоб хоть как то регулировать высоту прыжка
                        neg = -1                            # как только значение прыжка становиться -10,
                        if tutorial.platform_grass_visible == 1:
                            if man.x + 75 >= platform.x and man.x + 45 <= platform.x + platform.width and man.y >= 316:
                                man.isJump = False
                                if man.y > 320:
                                    man.isJump = True
                    if man.y >= 635:
                        man.isJump = False
                    man.y -= (man.jumpCount**2) / 1.2 * neg   # нег становиться -1 и прыжок спадает
                    man.jumpCount -= 1                      # нег 1 чтоб чел шёл вверх
                else:
                    man.isJump = False
                    man.jumpCount = 10
    redrawGameWindow()
    if man.Dead and keys[pygame.K_ESCAPE]:
        pygame.quit()
pygame.quit()
