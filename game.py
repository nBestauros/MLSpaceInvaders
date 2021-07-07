#pygame basic game loop from: https://realpython.com/pygame-a-primer
# Simple pygame program

# Import and initialize the pygame library
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import laser

pygame.init()


#Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
VELOCITY = 5
LASERVELOCITY = -12.5
DEFENDERY = 400

#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Fonts
testFont = pygame.font.SysFont("Calibri", 25, False, False)

#Characters
DEFENDER = pygame.Rect(250, 250, 25, 10)
DEFENDER.center = (250, DEFENDERY)

#Variables
hasQuit = False
scene1 = True
timer = 0
points = 0

#Sprite Groups
laserGroup = pygame.sprite.Group()



# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Draws all graphics on screen, updates screen
def draw_window():
    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, DEFENDER)

    for laserObj in laserGroup.sprites():
        pygame.draw.rect(screen, RED, laserObj)

    pygame.display.update()


# will move the defender left or right depending on if the left or right arrow key is pressed
def player_input_handler(keys, defender):
    if keys[pygame.K_LEFT] and defender.centerx - VELOCITY >0:
        defender.x -= VELOCITY

    if keys[pygame.K_RIGHT] and defender.centerx + VELOCITY <SCREEN_WIDTH:
        defender.x += VELOCITY

    if keys[pygame.K_SPACE] and len(laserGroup.sprites())==0:
        laserObj = laser.Laser(LASERVELOCITY, defender.centerx, DEFENDERY)
        laserGroup.add(laserObj)


#Game Loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    
    #Event Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #boolean list of all pressed keys
    keys = pygame.key.get_pressed()
    player_input_handler(keys, DEFENDER)

    for laserObj in laserGroup.sprites():
        laserObj.update()

    draw_window()

pygame.quit()
