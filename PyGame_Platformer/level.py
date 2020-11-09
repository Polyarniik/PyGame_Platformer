import constants
from blocks import *


class Level:

    def __init__(self, surface):
        self.surface = surface

    def draw_level(self, number):
        folders = ['grass', 'planet']
        y = 0
        plat = folders[number - 1]
        self.surface.fill(constants.BACKGROUND_COLOR)
        for row in open(r'data/Levels/_{}_.txt'.format(number), 'r').readlines():
            x = 0
            for column in row:
                if column == '0':
                    constants.platforms_sprites.add(Platform(x, y, plat + 'Center', plat))
                    constants.platforms.append(Platform(x, y, plat + 'Center', plat))
                if column == '1':
                    constants.platforms_sprites.add(Platform(x, y, plat + 'Mid', plat))
                    constants.platforms.append(Platform(x, y, plat + 'Mid', plat))
                if column == '2':
                    constants.platforms_sprites.add(Platform(x, y, plat + 'Left', plat))
                    constants.platforms.append(Platform(x, y, plat + 'Left', plat))
                if column == '3':
                    constants.platforms_sprites.add(Platform(x, y, plat + 'Right', plat))
                    constants.platforms.append(Platform(x, y, plat + 'Right', plat))
                if column == '8':
                    constants.platforms_sprites.add(Platform(x, y, plat, plat))
                    constants.platforms.append(Platform(x, y, plat, plat))
                if column == '9':
                    constants.platforms_sprites.add(Platform(x, y, plat + 'Center_round', plat))
                    constants.platforms.append(Platform(x, y, plat + 'Center_round', plat))
                if column == 'w':
                    constants.water_sprites.add(Water(x, y, water=True))
                if column == 'T':
                    constants.water_sprites.add(Water(x, y, high=True))
                if column == 't':
                    constants.water_sprites.add(Water(x, y, low=True))
                if column == 'r':
                    constants.rock_sprites.add(Rock(x, y))
                if column == 'l':
                    constants.lava_sprites.add(Lava(x, y, lava=True))
                if column == 'Y':
                    constants.lava_sprites.add(Lava(x, y, high=True))
                if column == 'y':
                    constants.lava_sprites.add(Lava(x, y, low=True))
                if column == 's':
                    constants.ladder_sprites.add((Ladder(x, y, mid=True)))
                if column == 'S':
                    constants.ladder_sprites.add((Ladder(x, y, top=True)))
                if column == '$':
                    constants.ladder_sprites.add((Ladder(x, y, bottom=True)))
                if column == '_':
                    constants.spikes_sprites.add(Spikes(x, y))
                if column == 'd':
                    constants.door_sprites.add(Door(x, y, op=False, top=False))
                if column == 'D':
                    constants.door_sprites.add(Door(x, y, op=False, top=True))
                    constants.door_x = x
                    constants.door_y = y
                if column == "'":
                    constants.blue_coin_sprites.add(Coin(x, y, blue=True))
                if column == '\"':
                    constants.pink_coin_sprites.add(Coin(x, y, pink=True))
                if column == 'P':
                    constants.start_x = x
                    constants.start_y = y
                x += 40
            y += 40
