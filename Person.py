import pygame
from Skeleton import skeleton
from Boss import Ogre

walkRight1 = pygame.image.load('images/player/Run1.png')
walkRight1 = pygame.transform.scale(walkRight1, (130, 130))
walkRight2 = pygame.image.load('images/player/Run2.png')
walkRight2 = pygame.transform.scale(walkRight2, (130, 130))
walkRight3 = pygame.image.load('images/player/Run3.png')
walkRight3 = pygame.transform.scale(walkRight3, (130, 130))
walkRight4 = pygame.image.load('images/player/Run4.png')
walkRight4 = pygame.transform.scale(walkRight4, (130, 130))
walkRight5 = pygame.image.load('images/player/Run5.png')
walkRight5 = pygame.transform.scale(walkRight5, (130, 130))
walkRight6 = pygame.image.load('images/player/Run6.png')
walkRight6 = pygame.transform.scale(walkRight6, (130, 130))
walkRight7 = pygame.image.load('images/player/Run7.png')
walkRight7 = pygame.transform.scale(walkRight7, (130, 130))
walkRight = [walkRight1, walkRight2, walkRight3, walkRight4, walkRight5, walkRight6, walkRight7]

walkLeft1 = pygame.image.load('images/player/Run11.png')
walkLeft1 = pygame.transform.scale(walkLeft1, (130, 130))
walkLeft2 = pygame.image.load('images/player/Run22.png')
walkLeft2 = pygame.transform.scale(walkLeft2, (130, 130))
walkLeft3 = pygame.image.load('images/player/Run33.png')
walkLeft3 = pygame.transform.scale(walkLeft3, (130, 130))
walkLeft4 = pygame.image.load('images/player/Run44.png')
walkLeft4 = pygame.transform.scale(walkLeft4, (130, 130))
walkLeft5 = pygame.image.load('images/player/Run55.png')
walkLeft5 = pygame.transform.scale(walkLeft5, (130, 130))
walkLeft6 = pygame.image.load('images/player/Run66.png')
walkLeft6 = pygame.transform.scale(walkLeft6, (130, 130))
walkLeft7 = pygame.image.load('images/player/Run77.png')
walkLeft7 = pygame.transform.scale(walkLeft7, (130, 130))
walkLeft = [walkLeft1, walkLeft2, walkLeft3, walkLeft4, walkLeft5, walkLeft6, walkLeft7]

JumpRignt1 = pygame.image.load('images/player/Jump1.png')
JumpRignt1 = pygame.transform.scale(JumpRignt1, (130, 130))
JumpRignt2 = pygame.image.load('images/player/Jump2.png')
JumpRignt2 = pygame.transform.scale(JumpRignt2, (130, 130))
JumpRignt3 = pygame.image.load('images/player/Jump3.png')
JumpRignt3 = pygame.transform.scale(JumpRignt3, (130, 130))
JumpRight = [JumpRignt1, JumpRignt2, JumpRignt3, JumpRignt3]

JumpLeft1 = pygame.image.load('images/player/Jump11.png')
JumpLeft1 = pygame.transform.scale(JumpLeft1, (130, 130))
JumpLeft2 = pygame.image.load('images/player/Jump22.png')
JumpLeft2 = pygame.transform.scale(JumpLeft2, (130, 130))
JumpLeft3 = pygame.image.load('images/player/Jump33.png')
JumpLeft3 = pygame.transform.scale(JumpLeft3, (130, 130))
JumpLeft = [JumpLeft1, JumpLeft2, JumpLeft3, JumpLeft3]

standingRight1 = pygame.image.load('images/player/standing1.png')
standingRight1 = pygame.transform.scale(standingRight1, (130, 130))
standingRight2 = pygame.image.load('images/player/standing2.png')
standingRight2 = pygame.transform.scale(standingRight2, (130, 130))
standingRight3 = pygame.image.load('images/player/standing3.png')
standingRight3 = pygame.transform.scale(standingRight3, (130, 130))
standingRight4 = pygame.image.load('images/player/standing4.png')
standingRight4 = pygame.transform.scale(standingRight4, (130, 130))
standingRight = [standingRight1, standingRight2, standingRight3, standingRight4]

standingLeft1 = pygame.image.load('images/player/standing11.png')
standingLeft1 = pygame.transform.scale(standingLeft1, (130, 130))
standingLeft2 = pygame.image.load('images/player/standing22.png')
standingLeft2 = pygame.transform.scale(standingLeft2, (130, 130))
standingLeft3 = pygame.image.load('images/player/standing33.png')
standingLeft3 = pygame.transform.scale(standingLeft3, (130, 130))
standingLeft4 = pygame.image.load('images/player/standing44.png')
standingLeft4 = pygame.transform.scale(standingLeft4, (130, 130))
standingLeft = [standingLeft1, standingLeft2, standingLeft3, standingLeft4]

defendRight1 = pygame.image.load('images/player/Defend1.png')
defendRight1 = pygame.transform.scale(defendRight1, (130, 130))
defendRight2 = pygame.image.load('images/player/Defend2.png')
defendRight2 = pygame.transform.scale(defendRight2, (130, 130))
defendRight3 = pygame.image.load('images/player/Defend3.png')
defendRight3 = pygame.transform.scale(defendRight3, (130, 130))
defendRight4 = pygame.image.load('images/player/Defend4.png')
defendRight4 = pygame.transform.scale(defendRight4, (130, 130))
defendRight5 = pygame.image.load('images/player/Defend5.png')
defendRight5 = pygame.transform.scale(defendRight5, (130, 130))
defendRight = [defendRight1, defendRight2, defendRight3,
               defendRight4, defendRight5]

defendLeft1 = pygame.image.load('images/player/Defend11.png')
defendLeft1 = pygame.transform.scale(defendLeft1, (130, 130))
defendLeft2 = pygame.image.load('images/player/Defend22.png')
defendLeft2 = pygame.transform.scale(defendLeft2, (130, 130))
defendLeft3 = pygame.image.load('images/player/Defend33.png')
defendLeft3 = pygame.transform.scale(defendLeft3, (130, 130))
defendLeft4 = pygame.image.load('images/player/Defend44.png')
defendLeft4 = pygame.transform.scale(defendLeft4, (130, 130))
defendLeft5 = pygame.image.load('images/player/Defend55.png')
defendLeft5 = pygame.transform.scale(defendLeft5, (130, 130))
defendLeft = [defendLeft1, defendLeft2, defendLeft3,
              defendLeft4, defendLeft5]

attackRight1 = pygame.image.load('images/player/Attack1.png')
attackRight1 = pygame.transform.scale(attackRight1, (240, 160))
attackRight2 = pygame.image.load('images/player/Attack2.png')
attackRight2 = pygame.transform.scale(attackRight2, (240, 160))
attackRight3 = pygame.image.load('images/player/Attack3.png')
attackRight3 = pygame.transform.scale(attackRight3, (240, 160))
attackRight4 = pygame.image.load('images/player/Attack4.png')
attackRight4 = pygame.transform.scale(attackRight4, (240, 160))
attackRight = [attackRight1, attackRight2, attackRight3, attackRight4]

attackLeft1 = pygame.image.load('images/player/Attack11.png')
attackLeft1 = pygame.transform.scale(attackLeft1, (240, 160))
attackLeft2 = pygame.image.load('images/player/Attack22.png')
attackLeft2 = pygame.transform.scale(attackLeft2, (240, 160))
attackLeft3 = pygame.image.load('images/player/Attack33.png')
attackLeft3 = pygame.transform.scale(attackLeft3, (240, 160))
attackLeft4 = pygame.image.load('images/player/Attack44.png')
attackLeft4 = pygame.transform.scale(attackLeft4, (240, 160))
attackLeft = [attackLeft1, attackLeft2, attackLeft3, attackLeft4]

DeadLeft1 = pygame.image.load('images/player/Dead11.png')
DeadLeft1 = pygame.transform.scale(DeadLeft1, (130, 130))
DeadLeft2 = pygame.image.load('images/player/Dead22.png')
DeadLeft2 = pygame.transform.scale(DeadLeft2, (130, 130))
DeadLeft3 = pygame.image.load('images/player/Dead33.png')
DeadLeft3 = pygame.transform.scale(DeadLeft3, (130, 130))
DeadLeft4 = pygame.image.load('images/player/Dead44.png')
DeadLeft4 = pygame.transform.scale(DeadLeft4, (130, 130))
DeadLeft5 = pygame.image.load('images/player/Dead55.png')
DeadLeft5 = pygame.transform.scale(DeadLeft5, (130, 130))
DeadLeft6 = pygame.image.load('images/player/Dead66.png')
DeadLeft6 = pygame.transform.scale(DeadLeft6, (130, 130))
DeadLeft = [DeadLeft1, DeadLeft2, DeadLeft3, DeadLeft4, DeadLeft5, DeadLeft6]

DeadLeft11 = pygame.image.load('images/player/Dead1.png')
DeadLeft11 = pygame.transform.scale(DeadLeft11, (130, 130))
DeadLeft22 = pygame.image.load('images/player/Dead2.png')
DeadLeft22 = pygame.transform.scale(DeadLeft22, (130, 130))
DeadLeft33 = pygame.image.load('images/player/Dead3.png')
DeadLeft33 = pygame.transform.scale(DeadLeft33, (130, 130))
DeadLeft44 = pygame.image.load('images/player/Dead4.png')
DeadLeft44 = pygame.transform.scale(DeadLeft44, (130, 130))
DeadLeft55 = pygame.image.load('images/player/Dead5.png')
DeadLeft55 = pygame.transform.scale(DeadLeft55, (130, 130))
DeadLeft66 = pygame.image.load('images/player/Dead6.png')
DeadLeft66 = pygame.transform.scale(DeadLeft66, (130, 130))
DeadRight = [DeadLeft11, DeadLeft22, DeadLeft33, DeadLeft44, DeadLeft55, DeadLeft66]

Hurt1 = pygame.image.load('images/player/Hurt1.png')
Hurt1 = pygame.transform.scale(Hurt1, (130, 130))
Hurt11 = pygame.image.load('images/player/Hurt11.png')
Hurt11 = pygame.transform.scale(Hurt11, (130, 130))
Hurt2 = pygame.image.load('images/player/Hurt2.png')
Hurt2 = pygame.transform.scale(Hurt2, (130, 130))
Hurt22 = pygame.image.load('images/player/Hurt22.png')
Hurt22 = pygame.transform.scale(Hurt22, (130, 130))
HurtRight = [Hurt1, Hurt2]
HurtLeft = [Hurt11, Hurt22]

Heart1 = pygame.image.load('images/player/Heart1.png')
Heart1 = pygame.transform.scale(Heart1, (200, 50))
Heart2 = pygame.image.load('images/player/Heart2.png')
Heart2 = pygame.transform.scale(Heart2, (200, 50))
Heart3 = pygame.image.load('images/player/Heart3.png')
Heart3 = pygame.transform.scale(Heart3, (200, 50))

class player():

    def __init__(self, x, y, width, height):  # готовность персонажа

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10  # скорость бега
        self.isJump = False
        self.left = False
        self.right = False
        self.defend = False
        self.attack = False
        self.walkCount1 = 0
        self.walkCount = 0
        self.jumpCount = 10
        self.standingCount = 0
        self.defendCount = 0
        self.attackCount = 4
        self.HurtCount = 0
        self.standing = True
        self.hitboxShieldRight = False
        self.hitboxShieldLeft = False
        self.hitboxHero = (self.x, self.y, 0, 0)
        self.hitboxAttackRight = False
        self.hitboxAttackLeft = False
        self.hitboxAttackLeft1 = False
        self.hitboxAttackRight1 = False
        self.Hurt = False
        self.Hit_True = False
        self.Dead = False
        self.HitCount = 0
        self.deadCount = 0


    def draw(self, win):

        if not (self.isJump) and self.deadCount == 0 and self.Hit_True == False:
            self.walkCount1 = 0
        if self.walkCount + 1 >= 28:
            self.walkCount = 0
        if self.standingCount + 1 == 80:
            self.standingCount = 0
        if self.defend == False:
            self.defendCount = 0
        if self.defendCount + 1 == 50:
            self.defendCount = 10
        if self.attackCount == 16:
            self.attackCount = 4
        if self.HurtCount == 12:
            self.HurtCount = 0

        elif not (self.standing) and self.deadCount == 0 and self.Hit_True == False:
            if self.right and self.hitboxShieldRight:
                win.blit(defendRight[self.defendCount // 10], (self.x, self.y))
                self.defendCount += 1
            elif self.left and self.hitboxShieldLeft:
                win.blit(defendLeft[self.defendCount // 10], (self.x, self.y))
                self.defendCount += 1
            elif self.attack and self.left:
                win.blit(attackLeft[self.attackCount // 4], (self.x - 75, self.y - 30))
                self.attackCount += 1

            elif self.attack:
                win.blit(attackRight[self.attackCount // 4], (self.x - 30, self.y - 30))
                self.attackCount += 1
            elif self.isJump and self.left and self.deadCount == 0 and self.Hit_True == False:
                win.blit(JumpLeft[self.walkCount1 // 6],
                         (self.x, self.y))  # раз в сколько кадров меняется картинка(win.blit наносить картинку)
                self.walkCount1 += 1
            elif self.isJump and self.right:
                win.blit(JumpRight[self.walkCount1 // 6], (self.x, self.y))
                self.walkCount1 += 1

            elif self.left:
                win.blit(walkLeft[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
                self.attackCount = 0
            elif self.right:
                win.blit(walkRight[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
                self.attackCount = 0
        if self.hitboxShieldLeft == False and self.x > skeleton.x:
            if self.Hurt == True and self.left and skeleton.True_attack or self.Hurt == True and self.left and self.Hit_True and self.left:
                self.standing = False
                self.Hit_True = True
                win.blit(HurtLeft[self.HurtCount // 6], (self.x, self.y))
                self.HurtCount += 1
                if self.HurtCount == 12 and self.left:
                    self.standing = False
                    self.Hit_True = False
                    self.Hurt = False
                    self.HurtCount = 0
                    self.HitCount += 1

        if self.Hurt == True and self.right and skeleton.True_attack or self.Hurt == True and self.right and self.Hit_True and self.right:
            self.standing = False
            self.Hit_True = True
            win.blit(HurtRight[self.HurtCount // 6], (self.x, self.y))
            self.HurtCount += 1
            if self.HurtCount == 12 and self.right:
                self.standing = False
                self.Hit_True = False
                self.Hurt = False
                self.HurtCount = 0
                self.HitCount += 1

        if self.HitCount == 0:
            win.blit(Heart3, (25, 25))
        if self.HitCount == 1:
            win.blit(Heart2, (25, 25))
        if self.HitCount == 2:
            win.blit(Heart1, (25, 25))

        if self.HitCount == 3 and self.left:
            self.deadCount += 1
            win.blit(DeadLeft[self.deadCount // 8], (self.x, self.y))
            if self.deadCount + 1 == 48:
                self.HitCount += 1
                self.Dead = True

        if self.HitCount == 3 and self.right:
            self.deadCount += 1
            win.blit(DeadRight[self.deadCount // 8], (self.x, self.y))
            if self.deadCount + 1 == 48:
                self.HitCount += 1
                self.Dead = True

        if self.standing and self.Dead == False:
            self.attackCount = 0

            if self.left and self.deadCount == 0 and self.Hit_True == False:
                win.blit(standingLeft[self.standingCount // 20], (self.x, self.y))
                self.standingCount += 1
            elif self.right and self.deadCount == 0 and self.Hit_True == False:
                win.blit(standingRight[self.standingCount // 20], (self.x, self.y))
                self.standingCount += 1

            elif self.isJump and self.deadCount == 0 and self.Hit_True == False:
                win.blit(JumpRight[3], (self.x, self.y))

            else:
                win.blit(standingRight[self.standingCount // 20], (self.x, self.y))
                self.standingCount += 1

        if skeleton.x + 350 > self.x and self.deadCount == 0 and self.Hit_True == False:
            self.Hurt = True

        self.hitboxHero = (self.x + 20, self.y, 80, 130)  # размер и расположение хитбокса
        pygame.draw.rect(win, (255, 0, 0), self.hitboxHero, 2)  # цвет хитбокса (толщина линии)
        if self.deadCount == 0 and self.Hit_True == False:
            if self.hitboxShieldRight == True:
                self.hitboxShieldRight = (self.x + 100, self.y - 5, 15, 135)
                self.hitboxShieldRightX = self.x + 100
                pygame.draw.rect(win, (0, 0, 0), self.hitboxShieldRight, 2)
            if self.hitboxShieldRight == False:
                self.hitboxShieldRight = (0, 0, 0)
            if self.hitboxShieldLeft == True:
                self.hitboxShieldLeft = (self.x + 12, self.y - 5, 15, 135)
                self.hitboxShieldLeftX = self.x + 100
                pygame.draw.rect(win, (0, 0, 0), self.hitboxShieldLeft, 2)
            if self.hitboxShieldLeft == False:
                self.hitboxShieldLeft = (0, 0, 0)

            if self.hitboxAttackRight == True and self.attackCount == 12:
                self.hitboxAttackRight1 = True
                self.hitboxAttackRight = (self.x + 50, self.y + 8, 140, 100)
                pygame.draw.rect(win, (0, 0, 0), self.hitboxAttackRight, 1)
            if self.hitboxAttackRight == False:
                self.hitboxAttackRight1 = False
                self.hitboxAttackRight = (0, 0, 0)
            if self.hitboxAttackLeft == True and self.attackCount == 12:
                self.hitboxAttackLeft1 = True
                self.hitboxAttackRight = (self.x - 50, self.y + 8, 140, 100)
                pygame.draw.rect(win, (0, 0, 0), self.hitboxAttackRight, 1)
            if self.hitboxAttackLeft == False:
                self.hitboxAttackLeft1 = False
                self.hitboxAttackRight = (0, 0, 0)

        ######################## For Skeleton ########################
        skeleton.manX = self.x
        skeleton.manY = self.y
        if self.hitboxAttackLeft1 == True:
            skeleton.ManHitboxAttackLeft1 = True
        if self.hitboxAttackRight1 == True:
            skeleton.ManHitboxAttackRight1 = True
        if self.hitboxAttackLeft1 == False:
            skeleton.ManHitboxAttackLeft1 = False
        if self.hitboxAttackRight1 == False:
            skeleton.ManHitboxAttackRight1 = False

        ######################## For Ogre ########################
        Ogre.manX = self.x
        Ogre.manY = self.y
        if self.hitboxAttackLeft1 == True:
            Ogre.ManHitboxAttackLeft1 = True
        if self.hitboxAttackRight1 == True:
            Ogre.ManHitboxAttackRight1 = True
        if self.hitboxAttackLeft1 == False:
            Ogre.ManHitboxAttackLeft1 = False
        if self.hitboxAttackRight1 == False:
            Ogre.ManHitboxAttackRight1 = False


man = player(700, 635, 130, 130)  # где появляется(х, у, width, height)