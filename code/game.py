#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Menu import Menu
import pygame as pyg

class Game:
    def __init__(self):
        pyg.init()
        self.window = pyg.display.set_mode(size=(700, 580))  # creates the window

    def run(self, ):

        # keeps the window opened
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # check events
            # for event in pyg.event.get():
            #     if event.type == pyg.QUIT:
            #         pyg.quit()  # close the window
            #         quit()  # close Pygame
