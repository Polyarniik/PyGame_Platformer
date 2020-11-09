import datetime

import blocks
import constants
import level
import menu
import player
from constants import *

constants.pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.blit(constants.scale_img(r'data/Sprites/Backgrounds/blue_shroom.png', (WIDTH, HEIGHT)), (0, 0))
music = constants.pygame.mixer.music.load(r'data/music.mp3')
constants.pygame.mixer.music.play(-1, 0.0)
bluePlayer = player.Player(win, constants.start_x, constants.start_y - 100, BLUE)
pinkPlayer = player.Player(win, constants.start_x + 80, constants.start_y - 100, PINK)
blue_player_sprites.add(bluePlayer)
pink_player_sprites.add(pinkPlayer)
run = False

def draw_level(number):
    level.Level(win).draw_level(number)


# draw_level(constants.currentLevel)
# all_sprites.add(blue_coin_sprites, pink_coin_sprites, platforms_sprites, water_sprites, lava_sprites,
#                     rock_sprites, door_sprites, ladder_sprites, spikes_sprites)


def start_level(next_level=False):
    blue_coin_sprites.empty()
    pink_coin_sprites.empty()
    platforms_sprites.empty()
    platforms.clear()
    water_sprites.empty()
    lava_sprites.empty()
    rock_sprites.empty()
    door_sprites.empty()
    ladder_sprites.empty()
    spikes_sprites.empty()
    all_sprites.empty()
    blue_player_sprites.empty()
    blue_player_sprites.empty()
    if next_level:
        constants.currentLevel += 1
    if constants.currentLevel == 3:
        exit()
    draw_level(constants.currentLevel)
    win.blit(constants.scale_img(r'data/Sprites/Backgrounds/blue_shroom.png', (WIDTH, HEIGHT)), (0, 0))
    all_sprites.add(blue_coin_sprites, pink_coin_sprites, platforms_sprites, water_sprites, lava_sprites,
                    rock_sprites, door_sprites, ladder_sprites, spikes_sprites)

    bluePlayer.health = 3
    pinkPlayer.health = 3
    bluePlayer.teleporting()
    pinkPlayer.teleporting()
    blue_player_sprites.add(bluePlayer)
    pink_player_sprites.add(pinkPlayer)
    pygame.display.update()


if menu.Menu(win).menu_loop():
    start_level()
    run = True


def check_game():
    if bluePlayer.health == 0 or pinkPlayer.health == 0:
        start_level()
    if bluePlayer.coins == 3 and pinkPlayer.coins == 3:
        if constants.close:
            all_sprites.remove(door_sprites)
            door_sprites.empty()
            door_sprites.add(blocks.Door(constants.door_x, constants.door_y, op=True, top=True))
            door_sprites.add(blocks.Door(constants.door_x, constants.door_y + 40, op=True, top=False))
            all_sprites.add(door_sprites)
            constants.close = False
        if (pygame.sprite.spritecollide(bluePlayer, door_sprites, False) and
                pygame.sprite.spritecollide(pinkPlayer, door_sprites, False)):
            start_level(True)


def collides(pl: player.Player):
    pl.falling = True
    pl.climb = False
    if pygame.sprite.spritecollide(pl, spikes_sprites, False):
        blocks.Spikes.hit(pl)
    if pygame.sprite.spritecollide(pl, rock_sprites, False):
        pl.hit = True
    if HEIGHT - 10 <= pl.rect.bottom <= HEIGHT + 10:
        pl.y = HEIGHT - pl.height
        pl.falling = False
    for plat in platforms:
        # нахождение на земле
        if plat.rect.top - 15 <= pl.rect.bottom <= plat.rect.top + 15 \
                and plat.rect.left - 5 <= pl.rect.centerx <= plat.rect.right + 5 and not pl.climb:
            pl.y = plat.rect.top - pl.height
            pl.falling = False
        # удар головой об платформу
        if plat.rect.bottom - 15 <= pl.rect.top <= plat.rect.bottom + 15 \
                and plat.rect.left + 10 <= pl.rect.right and pl.rect.left < plat.rect.right - 10:
            pl.y = plat.rect.bottom
            pl.isJumping = False
            pl.falling = True
        # препятствие справа
        if plat.rect.left - 10 <= pl.rect.right <= plat.rect.left + 10 \
                and pl.rect.top < plat.rect.centery < pl.rect.bottom and pl.goRight:
            pl.x = plat.rect.left - pl.width
            pl.hitRight = True
        # препятствие слева
        if plat.rect.right - 10 <= pl.rect.left <= plat.rect.right + 10 and \
                pl.rect.top < plat.rect.centery < pl.rect.bottom and pl.goLeft:
            pl.x = plat.rect.right
            pl.hitLeft = True
    if pygame.sprite.spritecollide(pl, ladder_sprites, False):
        pl.climb = True
        pl.falling = False
    else:
        pl.climb = False


def info():
    x = 1080
    for i in range(1, 4):
        if i <= bluePlayer.health:
            win.blit(constants.scale_img(r'data/Sprites/HUD/blueHeart.png', (40, 40)), (x, 0))
        else:
            win.blit(constants.scale_img(r'data/Sprites/HUD/heart_empty.png', (40, 40)), (x, 0))
        x += 40
    x = 0
    for i in range(1, 4):
        if i <= pinkPlayer.health:
            win.blit(constants.scale_img(r'data/Sprites/HUD/pinkHeart.png', (40, 40)), (x, 0))
        else:
            win.blit(constants.scale_img(r'data/Sprites/HUD/heart_empty.png', (40, 40)), (x, 0))
        x += 40
    x = WIDTH / 2 - 90
    for i in datetime.datetime.now().strftime('%M:%S'):
        if i == ':':
            win.blit(constants.scale_img(r'data/Sprites/HUD/hudX.png', (20, 20)), (x, 0))
            win.blit(constants.scale_img(r'data/Sprites/HUD/hudX.png', (20, 20)), (x, 20))
            x += 20
        else:
            win.blit(NUMBERS[int(i)], (x, 0))
            x += 40


while run:
    collides(bluePlayer)
    collides(pinkPlayer)
    check_game()
    if pygame.sprite.spritecollide(bluePlayer, blue_coin_sprites, True):
        bluePlayer.coins += 1
    if pygame.sprite.spritecollide(pinkPlayer, pink_coin_sprites, True):
        pinkPlayer.coins += 1
    if pygame.sprite.spritecollide(bluePlayer, lava_sprites, False):
        blocks.Water.hit(bluePlayer)
    if pygame.sprite.spritecollide(pinkPlayer, water_sprites, False):
        blocks.Lava.hit(pinkPlayer)
    win.blit(constants.scale_img(r'data/Sprites/Backgrounds/blue_shroom.png', (WIDTH, HEIGHT)), (0, 0))
    all_sprites.draw(win)
    bluePlayer.move()
    pinkPlayer.move()
    info()
    pygame.display.update()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_LEFT]:
        bluePlayer.goLeft = True
    if keys[pygame.K_RIGHT]:
        bluePlayer.goRight = True
    if keys[pygame.K_UP] and bluePlayer.climb:
        bluePlayer.climbUp = True
    elif keys[pygame.K_UP] and not bluePlayer.falling:
        bluePlayer.isJumping = True
    if keys[pygame.K_DOWN] and bluePlayer.climb:
        bluePlayer.climbDown = True
    if keys[pygame.K_a]:
        pinkPlayer.goLeft = True
    if keys[pygame.K_d]:
        pinkPlayer.goRight = True
    if keys[pygame.K_w] and pinkPlayer.climb:
        pinkPlayer.climbUp = True
    elif keys[pygame.K_w] and not pinkPlayer.falling:
        pinkPlayer.isJumping = True
    if keys[pygame.K_s] and pinkPlayer.climb:
        pinkPlayer.climbDown = True
    clock.tick(FPS)

pygame.quit()
