#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pyg
from pygame import surface, rect, image
from pygame.font import Font
from pygame import event, mixer_music

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, GAME_NAME


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pyg.image.load('./Assets/MenuBg.png').convert_alpha() #background image
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):

        menuOpt = 0

        pyg.mixer_music.load('./Assets/Menu.mp3') #seleciona a musica
        pyg.mixer_music.play(-1)  #-1 deixa em looping

        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            #IMPRIME NOME
            for i in range(len(GAME_NAME)):
                self.menu_text(50, GAME_NAME[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 50 + 30 * i))
            #IMPRIME OPTIONS
            for i in range(len(MENU_OPTION)):
                if i == menuOpt:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 190 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 190 + 25 * i))
            pyg.display.flip()


            #check events
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()  # close the window
                    quit()  # close Pygame

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_DOWN: #DIRECIONA OPT PRA BAIXO DE FORMA CICLICA
                        if menuOpt < len(MENU_OPTION) - 1:
                            menuOpt+=1
                        else:
                            menuOpt = 0
                    if event.key == pyg.K_UP: #DIRECIONA OPT PRA CIMA DE FORMA CICLICA
                        if menuOpt > 0:
                            menuOpt-=1
                        else:
                            menuOpt = len(MENU_OPTION) - 1
                    if event.key == pyg.K_RETURN: #ENTER
                        return MENU_OPTION[menuOpt]


    def menu_text(self, txt_sz: int, txt: str, txt_color: tuple, txt_center_pos: tuple):
        txt_font: Font = pyg.font.SysFont('Roboto', txt_sz)
        txt_surface: surface = txt_font.render(txt, True, txt_color).convert_alpha()
        txt_rect: rect = txt_surface.get_rect(center=txt_center_pos)
        self.window.blit(txt_surface, txt_rect)