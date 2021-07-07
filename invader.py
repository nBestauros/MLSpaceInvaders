import pygame
import random
class Invader(pygame.sprite.Sprite):
    def __init__(self, speed, centerx, centery):
        pygame.sprite.Sprite.__init__(self)

        #set Location on screen
        self.rect = pygame.Rect(0,0,15,15)
        self.rect.centerx = centerx
        self.rect.centery = centery

        #speed variable
        self.speed = speed
        
        directions = ["Right", "Left"]
        direcList = random.sample(directions, 2)
        self.direction = direcList[0]
        self.newDirection = direcList[1]
        
        self.downCount = 0

    #Moves the invader in the specified direction
    def update(self, SCREEN_WIDTH):
        if self.direction=="Right":
            self.rect.centerx += self.speed
            if self.rect.right>SCREEN_WIDTH:
                self.direction = "Down"
                self.newDirection = "Left"
        if self.direction == "Left":
            self.rect.centerx -= self.speed
            if self.rect.left<0:
                self.direction = "Down"
                self.newDirection = "Right"
        if self.direction == "Down":
            self.rect.centery += self.speed
            self.downCount +=1
            if self.downCount==4:
                self.direction = self.newDirection
                self.downCount = 0