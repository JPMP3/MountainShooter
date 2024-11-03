#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pyg
from pygame import surface, rect, image
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, GAME_NAME


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pyg.image.load('./Assets/MenuBg.png') #background image
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):

        # pyg.mixer_music.load('musica')
        # pyg.mixer_music.play(-1)  #-1 deixa em looping

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            #IMPRIME NOME
            for i in range(len(GAME_NAME)):
                self.menu_text(50, GAME_NAME[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 50 + 30 * i))
            #IMPRIME OPTIONS
            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 20 * i))

            pyg.display.flip()

            #check events
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()  # close the window
                    quit()  # close Pygame

        pass

    def menu_text(self, txt_sz: int, txt: str, txt_color: tuple, txt_center_pos: tuple):
        txt_font: Font = pyg.font.SysFont('Roboto', txt_sz)
        txt_surface: surface = txt_font.render(txt, True, txt_color).convert_alpha()
        txt_rect: rect = txt_surface.get_rect(center=txt_center_pos)
        self.window.blit(txt_surface, txt_rect)