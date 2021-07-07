import pygame
class Laser(pygame.sprite.Sprite):
    def __init__(self, yspeed, defenderCenterx, y):
        pygame.sprite.Sprite.__init__(self)

        #set Location on screen
        self.rect = pygame.Rect(0,0,5,7.5)
        self.rect.centerx = defenderCenterx
        self.rect.bottom = y

        #speed variable
        self.yspeed = yspeed

    #Update moves the laser up by the given yspeed. if it goes to the top of the screen the laser is deleted
    def update(self):
        self.rect.top +=self.yspeed
        if self.rect.bottom <=0:
            self.kill()
