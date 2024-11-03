#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDTH
import pygame as pyg

class Game:
    def __init__(self):
        pyg.init()
        self.window = pyg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # creates the window

    def run(self, ):

        # keeps the window opened
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
