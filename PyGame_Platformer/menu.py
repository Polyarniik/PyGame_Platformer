import time

import pygame

import constants


class Menu:
    COLOR_ENABLE_BTN = (255, 255, 0)
    COLOR_DISABLE_BTN = (255, 255, 255)

    def __init__(self, surface):
        self.surface = surface

    def write_text(self, surface, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        text_rect = textobj.get_rect(center=(x, y))
        surface.blit(textobj, text_rect)

    def menu_loop(self):
        menu = True
        btn = 0
        btn_names = ['Start', 'Quit']
        buttons = {'Start': self.COLOR_DISABLE_BTN, 'Quit': self.COLOR_DISABLE_BTN}
        while menu:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                buttons[btn_names[btn]] = self.COLOR_DISABLE_BTN
                btn = (btn + 1) % 2
                # time.sleep(0.3)
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                buttons[btn_names[btn]] = self.COLOR_DISABLE_BTN
                btn = (btn - 1) % 2
                # time.sleep(0.3)
            buttons[btn_names[btn]] = self.COLOR_ENABLE_BTN
            self.surface.fill(constants.BACKGROUND_COLOR)
            self.write_text(self.surface, 'MAIN MENU', pygame.font.Font(None, 120), (255, 255, 255),
                            constants.WIDTH / 2, constants.HEIGHT / 8)
            k = 0
            for i in buttons:
                self.write_text(self.surface, i, pygame.font.Font(None, 100), buttons[i],
                                constants.WIDTH / 2, constants.HEIGHT / 2.2 + k)
                k += 80
            if keys[pygame.K_RETURN]:
                if btn == 0:
                    return True
                if btn == 1:
                    pygame.quit()

            pygame.display.update()
            constants.clock.tick(10)
