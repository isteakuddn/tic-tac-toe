import sys
import pygame as pg
from random import randint

WIN_SIZE = 450

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()            
            pg.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()