#pygame basic game loop from: https://realpython.com/pygame-a-primer
# Simple pygame program

# Import and initialize the pygame library
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import laser
import random
import invader

x = 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()


#Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
VELOCITY = 5
LASERVELOCITY = -14
DEFENDERY = 400
INVADERY = 50
INVADERVELOCITY = 4
SPAWN_TIMER = 1500

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
invaderGroup = pygame.sprite.Group()

#Pygame Custom Events
spawn_invader_event = pygame.USEREVENT + 1


# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Draws all graphics on screen, updates screen
def draw_window():
    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, DEFENDER)

    for laserObj in laserGroup.sprites():
        pygame.draw.rect(screen, RED, laserObj)

    for invaderObj in invaderGroup.sprites():
        pygame.draw.rect(screen, BLUE, invaderObj)

    pygame.display.update()


# will move the defender left or right depending on if the left or right arrow key is pressed
def player_input_handler(keys, defender):
    if keys[pygame.K_a] and defender.centerx - VELOCITY >0:
        defender.x -= VELOCITY

    if keys[pygame.K_d] and defender.centerx + VELOCITY <SCREEN_WIDTH:
        defender.x += VELOCITY

    if keys[pygame.K_w] and len(laserGroup.sprites())==0:
        laserObj = laser.Laser(LASERVELOCITY, defender.centerx, DEFENDERY)
        laserGroup.add(laserObj)

def spawnInvader(y):
    invaderObj = invader.Invader(INVADERVELOCITY, random.randint(0, SCREEN_WIDTH), 25)
    invaderGroup.add(invaderObj)

#Game Loop

running = True
clock = pygame.time.Clock()

pygame.time.set_timer(spawn_invader_event, SPAWN_TIMER)

while running:
    clock.tick(FPS)

    #Event Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_invader_event:
            spawnInvader(INVADERY)

    #boolean list of all pressed keys
    keys = pygame.key.get_pressed()
    player_input_handler(keys, DEFENDER)

    for laserObj in laserGroup.sprites():
        laserObj.update()

    for invaderObj in invaderGroup.sprites():
        invaderObj.update(SCREEN_WIDTH)

    for invaderObj in invaderGroup.sprites():
        if pygame.sprite.groupcollide(laserGroup, invaderGroup, True, True):
            points+=1
            print("Points: " + str(points))

        if invaderObj.rect.bottom>DEFENDER.bottom:
            print("Game lost!")
            running = False

    draw_window()

pygame.quit()
