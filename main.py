import pygame as pyg

pyg.init()
window = pyg.display.set_mode(size = (700, 580)) #creates the window

#keeps the window opened
while True:
    #check events
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit() #close the window
            quit() #close Pygame
