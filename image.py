import pygame
class Image(pygame.sprite.Sprite):
	def __init__(self, fileName, left=0, top=0):
		pygame.sprite.Sprite.__init__(self)

		#Load Image
		self.image = pygame.image.load(fileName)
		self.image = self.image.convert()
		
		#set transparent
		self.image.set_colorkey((255,255,255))

		#Set Location on Screen
		self.rect = self.image.get_rect()
		self.rect.left =left 
		self.rect.top = top