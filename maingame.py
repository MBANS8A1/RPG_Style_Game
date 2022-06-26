#!/usr/bin/env python3

#Add file imports
import pygame
from pygame.locals import *
import sys
import random

#Allow initialization of pygame
pygame.init()

#setting the window size along with some physics quantities to control
#movement of the player and prevent player moving unhinged
#Variables
WIDTH = 710
HEIGHT =  480
#Acceleration (change in velocity)
ACCEL_ = 0.35
#Friction (can change depending on game ground surface)
FRIC_ = -0.12
#Cap the game at 60 frames per second for smooth transitions
FPS =60
FPS_CL = pygame.time.Clock()

#Character (Player) position will 
#be tracked by vector in X and Y direction
vec_PL =pygame.math.Vector2

#Set pygame window
winDisplay = pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption("RPG_Slasher")

#For the game loop (acts as a true boolean value)
running = 1


#Important classes

class Scenery(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sceneryImage = pygame.image.load ("Background.png")
        self.rect = self.image.get_rect(center=(355,480))
        self.scX = 0
        self.scY = 0
        
    def renderingS(self):
        winDisplay.blit(self.sceneryImage, (self.scX,self.scY))

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.floorImage = pygame.image.load ("Ground.png")
        self.rect = self.image.get_rect(center=(355,480))
        self.floorX = 0
        self.floorY = 0
        
    
     def renderingF(self):
        winDisplay.blit(self.floorImage, (self.floorX,self.floorY))   

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



#creating objects of classes
scenery = Scenery()
floor = Floor()



#Game loop
while running :
    pygame.time.delay (110)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = 0

    k_buttons = pygame.key.get_pressed()

    if k_buttons[pygame.K_LEFT]:
        pass
    
    if k_buttons[pygame.K_RIGHT]:
        pass
    
    if k_buttons[pygame.K_UP]:
        pass

    if k_buttons[pygame.K_DOWN]:
        pass
    
    
    scenery.renderingS()
    floor.renderingF()
    
    #Whole screen needs to be updated in frame transition
    pygame.display.update()
    FPS_CL.tick_busy_loop(FPS) 

pygame.quit()

