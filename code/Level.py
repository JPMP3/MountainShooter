#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import choice, random

import pygame.display
import pygame as pyg
from pygame import mixer_music
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, TIMER_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, gameMode):
        self.timeout = 20000  # 20s
        self.window = window
        self.name = name
        self.gameMode = gameMode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if gameMode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, TIMER_ENEMY)


    def run(self, ):
        pyg.mixer_music.load(f'./Assets/{self.name}.mp3') #seleciona a musica
        pyg.mixer_music.play(-1) #looping na musica
        pyg.mixer_music.set_volume(0.3)
        clock = pyg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity('Choice'))

            #printed text
            self.lvl_txt(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10,5))
            self.lvl_txt(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.lvl_txt(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()


    def lvl_txt(self, txt_sz: int, txt: str, txtColor: tuple, txt_pos: tuple):
        txtfont: Font = pyg.font.SysFont('roboto', txt_sz)
        txtSurf: Surface = txtfont.render(txt, True, txtColor).convert_alpha()
        txt_rect: Rect = txtSurf.get_rect(left=txt_pos[0], top=txt_pos[1])
        self.window.blit(txtSurf, txt_rect)
