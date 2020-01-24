# Necessary imports
from pygame.locals import *
from objects.orange import *
import pygame
import sys
import time
import random
from init.gameinitializers import *
from objects.click_box import *
from objects.background import *
from objects.cat_carrier import *
from objects.cat import *
from objects.menu import *
from objects.nanner import *

ohno = input(bcolors.WARNING +
             "File 'game.py', \n line 34 goal = Carrier() \n ^ \n SyntaxError: invalid syntax \n " + bcolors.ENDC + "Joshuas-MacBook-Pro:pygame joshuabevers$ ")

ohno = input(bcolors.WARNING +
             "File 'game.py', \n line 34 goal = Carrier() \n ^ \n SyntaxError: invalid syntax \n " + bcolors.ENDC + "Joshuas-MacBook-Pro:pygame joshuabevers$ ")


pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!")
SPAWN_SPEED = 1000

# timer var

spawn_orange = pygame.USEREVENT + 1

pygame.time.set_timer(spawn_orange + 1, SPAWN_SPEED)

# Space allocated for creating and adding variables.
bg = Background()
cat = Cat()
goal = Carrier()
orange = Orange(POWER, 40, 40)
bannana = Nanner(BANNANA, 50, 50)


menu = Menu('images/title-scren.png')

top_left = Click_Box('top_left')
top_right = Click_Box('top_right')
bottom_left = Click_Box('bottom_left')
bottom_right = Click_Box('bottom_right')

clock = pygame.time.Clock()

# all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(cat)
all_sprites.add(goal)
all_sprites.add(orange)
all_sprites.add(bannana)

# obstacle
obstacle = pygame.sprite.Group()
obstacle.add(orange)
obstacle.add(bannana)

# P Player
player = pygame.sprite.Group()
player.add(cat)

# clickboxes
click_boxes = pygame.sprite.Group()
click_boxes.add(top_left, top_right, bottom_left, bottom_right)

# Cat Carrier
carrier = pygame.sprite.Group()
carrier.add(goal)

# Start music!
bg.start_music()

# Create functions


def angerRises():
    cat.anger += 10
    cat.screech.play(fade_ms=1).fadeout(1000)
    print(cat.anger)


def angerCheck():
    if cat.anger >= 100:
        print("This rage cannot be contained!")


def cattitude(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 160
    BAR_HEIGHT = 30
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x + 3, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


    ### Game loop ###
running = True
menu_screen = True

while running:
    # variables being kept track of at the start of the game.
    start_ticks = pygame.time.get_ticks()
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)

    if menu_screen:
        menu.show_menu_screen(screen, clock)
        menu_screen = False

    for event in pygame.event.get():
        if event.type == spawn_orange + 1:
            for i in range(cat.level):
                if cat.level > (len(obstacle)-(cat.anger // 5)):
                    print(i)
                    o = Orange(POWER, 20, 15)
                    b = Nanner(BANNANA, 25, 24)
                    all_sprites.add(o)
                    obstacle.add(o)
                    all_sprites.add(b)
                    obstacle.add(b)

                # calling the function wheever we get timer event.

        # check for closing window
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

        # clicking on cat
        if event.type == pygame.MOUSEBUTTONDOWN:
            attitude = random.randint(1, 30)
            x, y = event.pos
            if top_left.rect.collidepoint(x, y):
                cat.change_direction('top_left')
                if attitude == 1:
                    cat.anger += 5
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if top_right.rect.collidepoint(x, y):
                cat.change_direction('top_right')
                if attitude == 1:
                    cat.anger += 5
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_left')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if bottom_left.rect.collidepoint(x, y):
                cat.change_direction('bottom_left')
                if attitude == 1:
                    cat.anger += 5
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if bottom_right.rect.collidepoint(x, y):
                cat.change_direction('bottom_right')
                if attitude == 1:
                    cat.anger += 5
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('top_left')

    if cat.anger >= 100:
        print("The cat has fucked off; as has your screen.")

    # Update
    all_sprites.update()
    click_boxes.update(cat)

    # Draw / render

    screen.blit(bg.background, bg.rect)
    cattitude(screen, 350, 10, cat.anger)
    all_sprites.draw(screen)
    click_boxes.draw(screen)
    screen.blit(goal.sprite, goal.rect)

    screen.blit(cat.running_sprite, cat.rect)

    # Collision Check for obsticals

    for unit in pygame.sprite.groupcollide(player, obstacle, False, True):
        print("OWCH!")
        angerRises()

    for unit in pygame.sprite.groupcollide(player, carrier, False, True):
        cat.level += 1
        print(cat.level)
        goal.respawn()
        carrier.add(goal)

    # *after* drawing everything, flip the display
    pygame.display.flip()


# Pygame end
pygame.mixer.quit()
pygame.quit()
