# import pygame, sys
# from pygame.locals import QUIT

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

'''Aqua Mermaids is a fun educational game for people to learn fun facts about the ocean environment and quiz to test their knowledge while trying to get as many coins as possible.

Used these tutorial videos to help with the project
-  https://www.youtube.com/watch?v=0fXe-ij2ehc&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=10&ab_channel=CodingWithRuss

-  https://www.youtube.com/watch?v=qYomF9p_SYM&ab_channel=ClearCode

-  https://www.youtube.com/watch?v=B6DrRN5z_uU&t=1964s&pp=ygUecHlnYW1lIHR1dG9yaWFsIHRoZSB3aG9sZSBnYW1l

-  Shout out to StackOverflow 
'''
import pygame
import random

from pygame.locals import *

# initializes pygame
pygame.init()

# background screen for width and height
BG_width = 700
BG_height = 500

# background screen object
background = pygame.display.set_mode((BG_width, BG_height))
pygame.display.set_caption("MarinaHack_Game")

# Frame Per Second
FPS = 60
# to ensure that the game runs on each computer at 60 frames per second
clock = pygame.time.Clock()

# trying out add a player
# playerImg = pygame.image.load("Drawing-1-PhotoRoom.png-PhotoRoom.png")
# player_w = 0
# player_h = 300
# PLAYER_VEL = 5
# playerImg = pygame.transform.rotate(playerImg, 90)

# player2Img = pygame.image.load("Drawing-1-PhotoRoom.png-PhotoRoom.png")
# player_w2 = 200
# player_h2 = 300
# player2Img = pygame.transform.rotate(player2Img, 45)

# adding a coral
coral = pygame.image.load("coral-PhotoRoom.png-PhotoRoom.png")
coral = pygame.transform.scale(coral, (100, 100))
coral_w = 200
coral_h = 400

coral1 = pygame.image.load("coral-PhotoRoom.png-PhotoRoom.png")
coral1 = pygame.transform.scale(coral, (100, 100))
coral_w1 = 500
coral_h1 = 400

# adding a turtle
turtle = pygame.image.load("turtle.png")
turtle = pygame.transform.scale(turtle, (100, 100))
turtle_w = 400
turtle_h = 400

# adding a crab
crap = pygame.image.load("crap.png")
crap = pygame.transform.scale(crap,(70,70))
crap_w = 600
crap_h = 400

# adding a starfish
starfish = pygame.image.load("start fish-PhotoRoom.png")
starfish = pygame.transform.scale(starfish,(150,150))
starfish_w = 360
starfish_h = 400

# coin = pygame.image.load("coin-PhotoRoom.png")
# coin = pygame.transform.scale(coin,(40,40))
# coin_w = 225
# coin_h = 200

# player 1
img1 = pygame.image.load("mermaid char1.png")
# player 2
img2 = pygame.image.load("mermaid char2.png")
#dead
dead = pygame.image.load("Drawing-1-PhotoRoom.png-PhotoRoom.png")

#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("turtle.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # turtle = pygame.transform.scale(self.image, (100, 100))
        # turtle_w = 400
        # turtle_h = 400
        
        
class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load("coin-PhotoRoom.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def coin_draw(self):    
        background.blit(self.image, self.rect)

    # def coin_count(num):
    
             
    
# making a class for players
class Player:
    def __init__(self, x, y, img):
        self.img = img
        # img = pygame.image.load("character-PhotoRoom.png")
        self.image = pygame.transform.scale(img, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        

    def update(self, player_num):
        dx = 0
        dy = 0
        if player_num == "1":
            # get keys pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                dy -= 7
            if keys[pygame.K_DOWN]:
                dy += 7

            if keys[pygame.K_LEFT]:
                dx -= 5

            if keys[pygame.K_RIGHT]:
                dx += 5

            self.rect.x += dx
            self.rect.y += dy
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                dy -= 7
            if keys[pygame.K_s]:
                dy += 7
            if keys[pygame.K_a]:
                dx -= 5
            if keys[pygame.K_d]:
                dx += 5

            self.rect.x += dx
            self.rect.y += dy

        background.blit(self.image, self.rect)

#players objects 
player = Player(0, 300, img1)
player2 = Player(200, 300, img2)

#display coins randomly
coins = []
num = random.randint(10, 20)
for i in range(num):    
    x = random.randint(0, 700)
    y  = random.randint(0, 500) 
    coins.append(Coin(x, y ))

#Start
active = True
while active:
    clock.tick(FPS)
  
    # looks at every event in the queue, i.e when user does something
    for event in pygame.event.get():
        if event.type == pygame.K_BACKSPACE:
            active = False
        # user clicks on window close button, stops loop
        elif event.type == pygame.QUIT:
            active = False

    # player.loop(FPS)
    # handle_move(player)
    # background screen is blue
    background.fill((30, 144, 255))

    # creates rectangle for the sand (ground of ocean)
    sand = pygame.Surface((700, 50))
    # color of rectangle
    sand.fill((250, 210, 135))
    rect = sand.get_rect()

    # handle_move(player)
    # drawsthe ground floor where the character is onto background
    background.blit(sand, (0, 460))
    # background.blit(playerImg, (player_w, player_h))
    # background.blit(player2Img, (player_w2, player_h2))
    # background.blit(coin, (coin_w, coin_h))
    for coin_display in coins:
        coin_display.coin_draw()
  
    
    background.blit(coral, (coral_w, coral_h))
    background.blit(coral1, (coral_w1, coral_h1))
    background.blit(turtle, (turtle_w, turtle_h))
    background.blit(crap,(crap_w,crap_h))
    background.blit(starfish,(starfish_w,starfish_h))
  
    player.update("1")
    player2.update("2")
    # Players character would change to dead if they exceed the screen size
    if player.rect.x > 510 or player.rect.x < -10 or player.rect.y > 710 or player.rect.y < -10:
        player.image = dead
    if player2.rect.x > 510 or player2.rect.x < -10 or player2.rect.y > 710 or player2.rect.y < -10:
        player2.image = dead

    #text
    font = pygame.font.SysFont("Lobster", 44)
    txt = font.render("Welcome to the Ocean", True, (0,0,0))
    background.blit(txt, (200, 50))
    
    # updates display
    # coin(2)
    pygame.display.flip()


pygame.quit()
