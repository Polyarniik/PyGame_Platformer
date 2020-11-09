import os

import pygame


def scale_img(path, width_height):
    return pygame.transform.scale(pygame.image.load(path), width_height)


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
blue_player_sprites = pygame.sprite.Group()
pink_player_sprites = pygame.sprite.Group()
blue_coin_sprites = pygame.sprite.Group()
pink_coin_sprites = pygame.sprite.Group()
platforms_sprites = pygame.sprite.Group()
water_sprites = pygame.sprite.Group()
lava_sprites = pygame.sprite.Group()
ladder_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
door_sprites = pygame.sprite.Group()
spikes_sprites = pygame.sprite.Group()
platforms = []
spike = []
BLUE = (0, 191, 255)
PINK = (255, 20, 147)
FPS = 30
start_x = -1
start_y = -1
door_x = -1
door_y = -1
close = True
BACKGROUND_COLOR = (152, 219, 233)
WIDTH, HEIGHT = 1200, 880
SPEED = 5
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
JUMP_HEIGHT = 142
JUMP_SPEED = 24
currentLevel = 1
block_height = (40, 40)
folder = 'data/Sprites/HUD/'
NUMBERS = (scale_img(os.path.join(folder, 'hud0.png'), block_height),
           scale_img(os.path.join(folder, 'hud1.png'), block_height),
           scale_img(os.path.join(folder, 'hud2.png'), block_height),
           scale_img(os.path.join(folder, 'hud3.png'), block_height),
           scale_img(os.path.join(folder, 'hud4.png'), block_height),
           scale_img(os.path.join(folder, 'hud5.png'), block_height),
           scale_img(os.path.join(folder, 'hud6.png'), block_height),
           scale_img(os.path.join(folder, 'hud7.png'), block_height),
           scale_img(os.path.join(folder, 'hud8.png'), block_height),
           scale_img(os.path.join(folder, 'hud9.png'), block_height))
