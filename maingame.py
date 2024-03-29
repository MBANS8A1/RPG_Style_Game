#!/usr/bin/env python3
#restarting game development
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
FPS =28
FPS_CL = pygame.time.Clock()

#Character (Player) position will 
#be tracked by vector in X and Y direction
vector_ =pygame.math.Vector2

#Set pygame window
winDisplay = pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption("RPG_Slasher")

#For the game loop (acts as a true boolean value)
running = 1

#Running animations
run_anim_R = [pygame.image.load("Hero_Sprite_R.png"), pygame.image.load("Hero_Sprite2_R.png"), pygame.image.load("Hero_Sprite3_R.png"),
pygame.image.load("Hero_Sprite4_R.png"), pygame.image.load("Hero_Sprite5_R.png"), pygame.image.load("Hero_Sprite6_R.png"),
pygame.image.load("Hero_Sprite_R.png")]

run_anim_L = [pygame.image.load("Hero_Sprite_L.png"), pygame.image.load("Hero_Sprite2_L.png"), pygame.image.load("Hero_Sprite3_L.png"),
pygame.image.load("Hero_Sprite4_L.png"), pygame.image.load("Hero_Sprite5_L.png"), pygame.image.load("Hero_Sprite6_L.png"),
pygame.image.load("Hero_Sprite_L.png")]

#Attack (Sword Swipe)animations 
attack_anim_R = [pygame.image.load("Hero_Sprite_R.png"),pygame.image.load("Hero_Attack_R.png"), 
pygame.image.load("Hero_Attack2_R.png"), pygame.image.load("Hero_Attack2_R.png"), 
pygame.image.load("Hero_Attack3_R.png"), pygame.image.load("Hero_Attack3_R.png"), 
pygame.image.load("Hero_Attack4_R.png"), pygame.image.load("Hero_Attack4_R.png"), 
pygame.image.load("Hero_Attack5_R.png"), pygame.image.load("Hero_Attack5_R.png"), 
pygame.image.load("Hero_Attack_R.png")]


attack_anim_L = [pygame.image.load("Hero_Sprite_L.png"), pygame.image.load("Hero_Attack_L.png"), 
pygame.image.load("Hero_Attack2_L.png"), pygame.image.load("Hero_Attack2_L.png"),
pygame.image.load("Hero_Attack3_L.png"), pygame.image.load("Hero_Attack3_L.png"),
pygame.image.load("Hero_Attack4_L.png"), pygame.image.load("Hero_Attack4_L.png"),
pygame.image.load("Hero_Attack5_L.png"),pygame.image.load("Hero_Attack5_L.png"),
pygame.image.load("Hero_Attack_L.png")]


#Important classes


class Scenery(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        NEW_SCENERY_SIZE = (710, 480)
        self.sceneryImage = pygame.transform.scale(pygame.image.load ("Background.png"),NEW_SCENERY_SIZE)
        self.rect = self.sceneryImage.get_rect(center=(355,240))
        self.scX = 0
        self.scY = 0
        
    def renderingS(self):
        winDisplay.blit(self.sceneryImage, (self.scX,self.scY))


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.floorImage = pygame.image.load ("Ground.png")
        self.rect = self.floorImage.get_rect(center=(355,440))
        self.floorX = 0
        self.floorY = 420
        
    
     def renderingF(self):
        winDisplay.blit(self.floorImage, (self.floorX,self.floorY))   

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imageH = pygame.image.load("Hero_Sprite_R.png")
        self.rectH = self.imageH.get_rect()
        self.vecX =0
        self.position_H = vector_(50,390)
        self.velocity_H = vector_(0,0)
        self.accel_H = vector_(0,0)
        self.left = False
        self.right = False
        self.run = True
        self.isJumping = False
        self.jumpCount = 10

    def move_H(self):
        self.accel_H = vector_(0,0.5)
      
      if abs(self.velocity_H.x) > 0.3:
            self.run = True
      else:
            self.run = False

      k_buttons = pygame.key.get_pressed()

      if k_buttons[pygame.K_LEFT] and self.position_H.x > self.velocity_H.x:
            self.left = True
            self.right = False
            self.accel_H.x = -ACCEL_
    
      if k_buttons[pygame.K_RIGHT] and self.position_H.x <WIDTH - self.getHeroWidth()-self.velocity_H.x:
            self.right = True
            self.left  = False
            self.accel_H.x = ACCEL_
      
      #Acceleration's hortizonal component reduced by negative frictional quantity
      self.accel_H.x += self.velocity_H.x * FRIC_
       #Now the velocity vector is updated by the acceleration vector to reflect changes
      self.velocity_H += self.accel_H
       #Position vector updated with velocity vector and half the acceleration vector
      self.position_H += self.velocity_H + (0.5*self.accel_H)

      self.rect.topleft = self.position_H
       
      def getHeroWidth (self):
        return self.imageH.get_width()
    
      def getHeroHeight (self):
        return self.imageH.get_height()

    def update_H(self):
        pass

    def attack_H(self):
        pass

    def jump_H(self):
        self.rect.x += 1
 
        # Check to see if player (sprite) is in contact with the ground
        hits = pygame.sprite.spritecollide(self, floor_group, False)
     
        self.rect.x -= 1
        if self.isJumping == False:
               self.isJumping = True
               self.velocity_H.y = -10
               
               
        else:
           if self.jumpCount >= -10:
              negVal = 1
              if self.jumpCount < 0:
                 negVal = -1
              self.position_H.y -= (self.jumpCount ** 2) *0.5*negVal
              self.jumpCount -= 1
           else:
              self.isJumping = False
              self.jumpCount = 10
      
    
    def updateF_H (self):
       if self.mv_frame > 6:
          self.mv_frame = 0
       if self.isJumping == False and self.run == True:
          if self.velocity_H.x >0:
              self.imageH = run_anim_R[self.mv_frame]
              self.right = True
              self.left = False
          else:
              self.imageH = run_anim_L[self.mv_frame]
              self.right = False
              self.left = True
          self.mv_frame += 1
       
       if abs(self.velocity_H.x) < 0.2 and self.mv_frame != 0:
          self.mv_frame = 0
          if self.right == True:
             self.imageH = run_anim_R[self.mv_frame]
          if self.left == True:
             self.imageH = run_anim_L[self.mv_frame]
     
    
    def attack_H (self):
        if self.a_Frame > 10:
            self.a_Frame = 0
            self.attacking = False
        
        # Check direction for correct animation to display  
        if self.right == True:
             self.imageH = attack_anim_R[self.a_Frame]
        elif self.left == True:
             self.turn_Correction()
             self.imageH = attack_anim_L[self.a_Frame] 
        
        self.a_Frame += 1
     
    def turn_Correction (self):
        if self.a_Frame == 1:
            self.position_H.x -= 10
        if self.a_Frame== 10:
            self.position_H.x += 10
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



#creating objects of classes
scenery = Scenery()
floor = Floor()
floor_group = pygame.sprite.Group()
floor_group.add(floor)
hero = Hero()

def drawGameWindow():
    #Whole screen needs to be updated in frame transition
    pygame.display.update()

#Game loop
while running :
    pygame.time.delay (110)
    hits = pygame.sprite.spritecollide(hero,floor_group,False)
    if hero.velocity_H.y > 0:
         if hits:
            lowest_point = hits[0]
            if hero.position_H.y < lowest_point.rect.bottom:
               hero.position_H.y = lowest_point.rect.top + 1
               hero.velocity_H.y = 0
               hero.isJumping = False
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = 0
        
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               if not hero.isJumping:
                   hero.right = False
                   hero.left = False
                   hero.jump_H()
           if event.key == pygame.K_a:
                if hero.attacking == False:
                   hero.attack_H()
                   hero.attacking = True  
    
    hero.move_H()
    scenery.renderingS()
    floor.renderingF()
    winDisplay.blit(hero.imageH, hero.rectH)
    
    #Whole screen needs to be updated in frame transition
    pygame.display.update()
    drawGameWindow()
    if hero.attacking == True:
       hero.attack_H() 
    FPS_CL.tick_busy_loop(FPS) 

pygame.quit()

