import pygame
from pygame.locals import *
import math

class Ball(object):

    def __init__(self, radius, color, pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def bounce_player(self):
        self.vx = abs(self.vx) # bounce ball back
        
    def move(self, delta_t, display, player):
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t
        if(self.vy > 0):
            self.vy += 1
        else:
            self.vy -+ 1
        if(self.vx > 0):
            self.vx += 1
        else:
            self.vx -+ 1

        # make ball bounce if hitting wall
        if self.x < self.radius:
            self.vx = abs(self.vx)
            game_over = True # game over when ball hits left wall
        if self.y < self.radius:
            self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self, color, wide , height):
        self.wide = wide
        self.height = height
        self.x = 320
        self.y = 260
        self.color = color
        self.pos = (self.x,self.y)

    def can_hit(self, ball):
        return math.fabs(self.y-ball.y) < 18 and math.fabs(ball.x-self.x) < 18

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5

    def render(self, surface):
        self.pos = (self.x,self.y)
        pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.wide,self.height),2)
        
