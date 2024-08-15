import pygame as py
from constants import *
from first_screen import *
pygame.init()

class Game:
    def __init__(self):
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = py.time.Clock()
        self.runing = True
        self.initial_screen = Initial_Screen(self.screen)
        self.event_unicode = ""

    def events(self) :
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                self.event_unicode += event.unicode
            if event.type == py.QUIT:
                self.runing = False
        
    def draw(self):
        self.screen.fill("black")
        self.initial_screen.player_input(self.event_unicode)
        self.clock.tick(60)
        py.display.update()
    
    def main_loop(self):
        while self.runing:
            self.draw()
            self.events()
            print(py.mouse.get_pos())

    def update(self):
        self.main_loop()
        
        

game = Game()
game.update()