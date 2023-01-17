import pygame

skeleton_standing1 = pygame.image.load('images/skeleton/skeleton_standing1.png')
skeleton_standing1 = pygame.transform.scale(skeleton_standing1, (210, 160))
skeleton_standing2 = pygame.image.load('images/skeleton/skeleton_standing2.png')
skeleton_standing2 = pygame.transform.scale(skeleton_standing2, (210, 160))
skeleton_standing3 = pygame.image.load('images/skeleton/skeleton_standing3.png')
skeleton_standing3 = pygame.transform.scale(skeleton_standing3, (210, 160))
skeleton_standing = [skeleton_standing1, skeleton_standing2, skeleton_standing3]

atack1 = pygame.image.load('images/skeleton/atack1.png')
atack1 = pygame.transform.scale(atack1, (500, 250))
atack2 = pygame.image.load('images/skeleton/atack2.png')
atack2 = pygame.transform.scale(atack2, (500, 250))
atack3 = pygame.image.load('images/skeleton/atack3.png')
atack3 = pygame.transform.scale(atack3, (500, 250))
atack4 = pygame.image.load('images/skeleton/atack4.png')
atack4 = pygame.transform.scale(atack4, (500, 250))
atack5 = pygame.image.load('images/skeleton/atack5.png')
atack5 = pygame.transform.scale(atack5, (500, 250))
atack6 = pygame.image.load('images/skeleton/atack6.png')
atack6 = pygame.transform.scale(atack6, (500, 250))
atack7 = pygame.image.load('images/skeleton/atack7.png')
atack7 = pygame.transform.scale(atack7, (500, 250))
atack8 = pygame.image.load('images/skeleton/atack8.png')
atack8 = pygame.transform.scale(atack8, (500, 250))
atack9 = pygame.image.load('images/skeleton/atack9.png')
atack9 = pygame.transform.scale(atack9, (500, 250))
atack10 = pygame.image.load('images/skeleton/atack10.png')
atack10 = pygame.transform.scale(atack10, (500, 250))
atack11 = pygame.image.load('images/skeleton/atack11.png')
atack11 = pygame.transform.scale(atack11, (500, 250))
atack12 = pygame.image.load('images/skeleton/atack12.png')
atack12 = pygame.transform.scale(atack12, (500, 250))
atack13 = pygame.image.load('images/skeleton/atack13.png')
atack13 = pygame.transform.scale(atack13, (500, 250))
atack14 = pygame.image.load('images/skeleton/atack14.png')
atack14 = pygame.transform.scale(atack14, (500, 250))
atack15 = pygame.image.load('images/skeleton/atack15.png')
atack15 = pygame.transform.scale(atack15, (500, 250))
atack16 = pygame.image.load('images/skeleton/atack16.png')
atack16 = pygame.transform.scale(atack16, (500, 250))
atack17 = pygame.image.load('images/skeleton/atack17.png')
atack17 = pygame.transform.scale(atack17, (500, 250))
atack = [atack1, atack2, atack3, atack4, atack5, atack6, atack7, atack8, atack9, atack10, atack11, atack12, atack13,
         atack14, atack15, atack16, atack17]

deadStart = pygame.image.load('images/skeleton/deadStart.png')
deadStart = pygame.transform.scale(deadStart, (500, 250))
dead1 = pygame.image.load('images/skeleton/dead1.png')
dead1 = pygame.transform.scale(dead1, (500, 250))
dead2 = pygame.image.load('images/skeleton/dead2.png')
dead2 = pygame.transform.scale(dead2, (500, 250))
dead3 = pygame.image.load('images/skeleton/dead3.png')
dead3 = pygame.transform.scale(dead3, (500, 250))
dead4 = pygame.image.load('images/skeleton/dead4.png')
dead4 = pygame.transform.scale(dead4, (500, 250))
dead5 = pygame.image.load('images/skeleton/dead5.png')
dead5 = pygame.transform.scale(dead5, (500, 250))
dead6 = pygame.image.load('images/skeleton/dead6.png')
dead6 = pygame.transform.scale(dead6, (500, 250))
dead7 = pygame.image.load('images/skeleton/dead7.png')
dead7 = pygame.transform.scale(dead7, (500, 250))
dead8 = pygame.image.load('images/skeleton/dead8.png')
dead8 = pygame.transform.scale(dead8, (500, 250))
dead9 = pygame.image.load('images/skeleton/dead9.png')
dead9 = pygame.transform.scale(dead9, (500, 250))
dead10 = pygame.image.load('images/skeleton/dead10.png')
dead10 = pygame.transform.scale(dead10, (500, 250))
dead11 = pygame.image.load('images/skeleton/dead11.png')
dead11 = pygame.transform.scale(dead11, (500, 250))
dead12 = pygame.image.load('images/skeleton/dead12.png')
dead12 = pygame.transform.scale(dead12, (500, 250))
dead13 = pygame.image.load('images/skeleton/dead13.png')
dead13 = pygame.transform.scale(dead13, (500, 250))
dead = [dead4, dead5, dead6, dead7, dead8, dead9, dead10, dead11, dead12, dead13]
hit = [deadStart, dead1, dead2, dead3]
hp_full = pygame.image.load('images/landscape/hp_full.png')
hp_full = pygame.transform.scale(hp_full, (100, 40))
hp_medium = pygame.image.load('images/landscape/hp_medium.png')
hp_medium = pygame.transform.scale(hp_medium, (100, 40))
hp_low = pygame.image.load('images/landscape/hp_low.png')
hp_low = pygame.transform.scale(hp_low, (100, 40))

class skeleton_enemy():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.standing = True
        self.atack = False
        self.hit = False
        self.dead = False
        self.hitbox = (self.x, self.y, 0, 0)
        self.hitbox_atack = True
        self.atackCount = 0
        self.standingCount = 0
        self.hitCount = 0
        self.deadCount = 0
        self.killCount = 0
        self.True_attack = False
        ###### from person ####
        self.manX = 0
        self.manY = 0
        self.ManHitboxAttackLeft1 = False
        self.ManHitboxAttackRight1 = False

    def draw(self, win):
        if self.killCount == 0:
            win.blit(hp_full, (self.x + 90, self.y - 50))
        if self.killCount == 1:
            win.blit(hp_medium, (self.x + 90, self.y - 50))
        if self.killCount == 2:
            win.blit(hp_low, (self.x + 90, self.y - 50))

        if self.atackCount == 28:
            self.True_attack = True
        if self.atackCount != 28:
            self.True_attack = False

        if  self.manX  > self.x and self.manX > self.x and self.x + 220 > self.manX and self.ManHitboxAttackLeft1 == True and self.dead == False and\
                self.manY + 50 > self.y or self.hit == True and self.dead == False:
            self.standing = False
            self.hit = True
            self.ManHitboxAttackLeft1 = True
            self.hitCount += 1
            if self.hitCount + 1 == 13:
                win.blit(dead2, (self.x - 130, self.y - 100))
                self.killCount += 1
                self.hit = False
                self.standing = True
                if self.standing == True and self.hit == False:
                    self.hitCount = 0
                self.ManHitboxAttackLeft1 = False
            if self.ManHitboxAttackLeft1 == True or self.hit == True:
                win.blit(hit[self.hitCount // 3], (self.x - 130, self.y - 100))

        elif  self.manX + 110 > self.x and self.manX < self.x and self.ManHitboxAttackRight1 == True and self.dead == False and\
                self.manY + 50 > self.y or self.hit == True and self.dead == False:
            self.standing = False
            self.hit = True
            self.ManHitboxAttackRight1 = True
            self.hitCount += 1
            if self.hitCount + 1 == 13:
                win.blit(dead2, (self.x - 130, self.y - 100))
                self.killCount += 1
                self.hit = False
                self.standing = True
                if self.standing == True and self.hit == False:
                    self.hitCount = 0
                self.ManHitboxAttackRight1 = False
            if self.ManHitboxAttackRight1 == True or self.hit == True:
                win.blit(hit[self.hitCount // 3], (self.x - 130, self.y - 100))

        if self.killCount + 1 == 4:
            self.standing = False
            self.atack = False
            self.dead = True
            self.deadCount += 1
            if self.deadCount + 1 < 31:
                win.blit(dead[self.deadCount // 3], (self.x - 130, self.y - 100))
            if self.deadCount + 1 == 31:
                win.blit(dead13, (self.x - 130, self.y - 100))

        self.hitbox = (self.x + 100, self.y - 10, 80, 160)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if self.x <= self.manX and self.x + 200 >= self.manX:
            self.standing = False
            self.atack = True

        if self.x + 80 >= self.manX and self.atack == True:
            if self.atackCount + 1 == 69:
                self.atackCount = 0
                self.standing = True
                self.atack = False
            win.blit(atack[self.atackCount // 4], (self.x - 130, self.y - 100))

        if self.hit == True:
            self.atackCount = 0


        if self.atack == True and self.hit == False and self.dead == False:
            self.atackCount += 1
            self.standing = False
            if self.atackCount + 1 == 69:
                self.atackCount = 0
            win.blit(atack[self.atackCount // 4], (self.x - 130, self.y - 100))

        if self.standing == True:
            self.standingCount += 1
            if self.standingCount + 1 == 61:
                self.standingCount = 0
            win.blit(skeleton_standing[self.standingCount // 20], (self.x, self.y - 7 ))

skeleton = skeleton_enemy(20, 620, 130, 130)