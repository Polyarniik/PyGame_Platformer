import datetime
import os
import time
import pygame

import constants


class Player(pygame.sprite.Sprite):
    path = r'data/Sprites/Players/'
    walk = 0
    gravitation = 2
    slow = 2
    jumpCor = [35, 30, 25, 20, 15, 10, 5]

    def __init__(self, surface, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.height = constants.PLAYER_HEIGHT + 5
        self.width = constants.PLAYER_WIDTH
        self.isJumping = False
        self.falling = False
        self.hitRight = False
        self.hitLeft = False
        self.currentHeight = 0
        self.goLeft = False
        self.goRight = False
        self.climb = False
        self.climbUp = False
        self.climbDown = False
        self.time = float(datetime.datetime.now().strftime('%S.%f'))
        self.health = 3
        self.coins = 0
        if color == constants.BLUE:
            folder = os.path.join(self.path, 'Blue')
        else:
            folder = os.path.join(self.path, 'Pink')
        self.leftSprites = []
        self.rightSprites = []
        self.climbSpites = []
        self.leftSprites.append(constants.scale_img(os.path.join(folder, 'left1.png'), (self.width, self.height)))
        self.leftSprites.append(constants.scale_img(os.path.join(folder, 'left2.png'), (self.width, self.height)))
        self.rightSprites.append(constants.scale_img(os.path.join(folder, 'right1.png'), (self.width, self.height)))
        self.rightSprites.append(constants.scale_img(os.path.join(folder, 'right2.png'), (self.width, self.height)))
        self.climbSpites.append(constants.scale_img(os.path.join(folder, 'climb1.png'), (self.width, self.height)))
        self.climbSpites.append(constants.scale_img(os.path.join(folder, 'climb2.png'), (self.width, self.height)))
        self.standSprite = constants.scale_img(os.path.join(folder, 'front.png'), (self.width, self.height))
        self.jumpLeftSprite = constants.scale_img(os.path.join(folder, 'jump_left.png'), (self.width, self.height))
        self.jumpRightSprite = constants.scale_img(os.path.join(folder, 'jump_right.png'), (self.width, self.height))
        self.rect = pygame.Rect(self.standSprite.get_rect())
        self.rect.x = x
        self.rect.y = y

    def __sprite_num__(self):
        now_time = float(datetime.datetime.now().strftime('%S.%f'))
        if abs(now_time - self.time) > 0.08:
            self.walk = (self.walk + 1) % 2
            self.time = now_time

    def go_right(self):
        if not self.hitRight:
            self.x += constants.SPEED
        self.hitRight = False
        self.goRight = False

    def go_left(self):
        if not self.hitLeft:
            self.x -= constants.SPEED
        self.hitLeft = False
        self.goLeft = False

    def jump(self):
        if self.currentHeight < len(self.jumpCor):
            self.y -= self.jumpCor[self.currentHeight]
            self.currentHeight += 1
            self.isJumping = True
        else:
            self.isJumping = False
            self.falling = True

    def fall(self):
        if self.falling:
            self.y += self.slow
            self.slow += self.gravitation
        else:
            self.slow = self.gravitation
            self.slow = self.gravitation
            self.currentHeight = 0
            self.isJumping = False
            constants.JUMP_SPEED = 23

    def do_climb(self):
        if self.climbUp:
            self.y -= 5
        if self.climbDown:
            self.y += 5
        if self.climbDown or self.climbUp:
            self.surface.blit(self.climbSpites[self.walk % 2], (self.x, self.y))
            self.__sprite_num__()
        else:
            self.surface.blit(self.standSprite, (self.x, self.y))
        self.climbUp = self.climbDown = False

    def move(self):
        if self.isJumping and not self.climb:
            if self.goRight:
                self.jump()
                self.go_right()
                self.surface.blit(self.jumpRightSprite, (self.x, self.y))
            elif self.goLeft:
                self.jump()
                self.go_left()
                self.surface.blit(self.jumpLeftSprite, (self.x, self.y))
            else:
                self.jump()
                self.surface.blit(self.standSprite, (self.x, self.y))
        elif self.goRight:
            self.go_right()
            self.surface.blit(self.rightSprites[self.walk % 2], (self.x, self.y))
            self.__sprite_num__()
        elif self.goLeft:
            self.go_left()
            self.surface.blit(self.leftSprites[self.walk % 2], (self.x, self.y))
            self.__sprite_num__()
        elif self.climb:
            self.do_climb()
        else:
            self.surface.blit(self.standSprite, (self.x, self.y))
        if (not self.isJumping or not self.falling) and not self.climb:
            self.fall()
        self.rect.x = self.x
        self.rect.y = self.y

    def teleporting(self):
        if self.color == constants.BLUE:
            self.x = constants.start_x
        else:
            self.x = constants.start_x + 80
        self.y = constants.start_y - 100
        time.sleep(0.7)

    def hit(self):
        self.health -= 1
        self.teleporting()
