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
FPS_CL = pygame.time.Clock

#Character (Player) position will 
#be tracked by vector in X and Y direction
vec_PL =pygame.math.Vector2

#Set pygame window
winDisplay = pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption("RPG_Slasher")

#For the game loop (acts as a true boolean value)
running = 1
