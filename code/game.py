#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
import pygame as pyg
from code.Level import Level

class Game:
    def __init__(self):
        pyg.init()
        self.window = pyg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # creates the window

    def run(self, ):

        # keeps the window opened
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pyg.quit()
                quit()
            else:
                pass
