import pygame
from pygame.locals import *

import gamelib
from elements import Ball, Player

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(SquashGame, self).__init__('Dodgers', SquashGame.BLACK)
        self.balls = []
        self.balls.append(Ball(radius=10,color=SquashGame.WHITE,pos=(self.window_size[0]/2+100 ,self.window_size[1]/2+40),speed=(200,50)))
        self.balls.append(Ball(radius=10,color=SquashGame.WHITE,pos=(self.window_size[0]/2+100 ,self.window_size[1]/2+40),speed=(100,50)))
        self.balls.append(Ball(radius=10,color=SquashGame.WHITE,pos=(self.window_size[0]/2+100 ,self.window_size[1]/2+40),speed=(50,100)))
        self.balls.append(Ball(radius=10,color=SquashGame.WHITE,pos=(self.window_size[0]/2+100 ,self.window_size[1]/2+40),speed=(50,200)))
        self.player = Player(wide = 30,height = 30,
                             color=SquashGame.GREEN)


    def init(self):
        super(SquashGame, self).init()

    def update(self):
        for i in range(4):
            self.balls[i].move(1./self.fps, self.surface, self.player)
            if self.player.can_hit(self.balls[i]):
                self.is_terminated = True

        if self.is_key_pressed(K_LEFT) and self.player.x>100:
            self.player.move_left()
        if self.is_key_pressed(K_RIGHT) and self.player.x <510:
            self.player.move_right()
        if self.is_key_pressed(K_UP) and self.player.y>100:
            self.player.move_up()
        if self.is_key_pressed(K_DOWN) and self.player.y <330:
            self.player.move_down()


    def render(self, surface):
        for i in range(4):
            self.balls[i].render(surface)
        self.player.render(surface)
        pygame.draw.rect(surface,SquashGame.WHITE,pygame.Rect(100,100,441,261),2)

def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()
