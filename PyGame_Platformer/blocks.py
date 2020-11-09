import pygame
import constants
import player


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, position, package):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = constants.scale_img(r'data/Sprites/' + str(package) + r'/' + str(position) + '.png',
                                         constants.block_height)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.x = x
        self.rect.y = y


class Water(pygame.sprite.Sprite):
    def __init__(self, x, y, water=False, high=False, low=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if high:
            self.image = constants.scale_img(r'data/Sprites/Tiles/waterHigh.png', constants.block_height)
        elif low:
            self.image = constants.scale_img(r'data/Sprites/Tiles/waterLow.png', constants.block_height)
        else:
            self.image = constants.scale_img(r'data/Sprites/Tiles/water.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)

    @staticmethod
    def hit(pl: player.Player):
        pl.health -= 1
        pl.teleporting()


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, lava=False, high=False, low=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if high:
            self.image = constants.scale_img(r'data/Sprites/Tiles/lavaHigh.png', constants.block_height)
        elif low:
            self.image = constants.scale_img(r'data/Sprites/Tiles/lavaLow.png', constants.block_height)
        else:
            self.image = constants.scale_img(r'data/Sprites/Tiles/lava.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)

    @staticmethod
    def hit(pl: player.Player):
        pl.health -= 1
        pl.teleporting()


class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = constants.scale_img(r'data/Sprites/Tiles/rock.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, mid=False, top=False, bottom=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if top:
            self.image = constants.scale_img(r'data/Sprites/Tiles/ladderTop.png', constants.block_height)
        elif bottom:
            self.image = constants.scale_img(r'data/Sprites/Tiles/ladderBottom.png', constants.block_height)
        else:
            self.image = constants.scale_img(r'data/Sprites/Tiles/ladderMid.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)


class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = constants.scale_img(r'data/Sprites/Tiles/spikes.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)

    @staticmethod
    def hit(pl: player.Player):
        pl.health -= 1
        pl.teleporting()


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, blue=False, pink=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.blue = blue
        if blue:
            self.image = constants.scale_img(r'data/Sprites/HUD/hudPlayer_blue.png', constants.block_height)
        else:
            self.image = constants.scale_img(r'data/Sprites/HUD/hudPlayer_pink.png', constants.block_height)
        self.rect = pygame.Rect(x, y, 40, 40)


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, op, top=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if op:
            if top:
                self.image = constants.scale_img(r'data/Sprites/Tiles/doorOpen_top.png', constants.block_height)
            else:
                self.image = constants.scale_img(r'data/Sprites/Tiles/doorOpen_mid.png', constants.block_height)
        else:
            if top:
                self.image = constants.scale_img(r'data/Sprites/Tiles/doorClosed_top.png', constants.block_height)
            else:
                self.image = constants.scale_img(r'data/Sprites/Tiles/doorClosed_mid.png', constants.block_height)

        self.rect = pygame.Rect(x, y, 40, 40)
