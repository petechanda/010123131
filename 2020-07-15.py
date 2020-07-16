### STUDENT NUMBER : 6201012630029
### ASSIGNMENT 1

import pygame 
import random
import math

# initialize PyGame
pygame.init()

# set window caption
pygame.display.set_caption('Assign1') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (500 x 500 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

pos_x = []
pos_y = []
radius = []
n = 0
while n<10:
    booln = True
    # randomize an integer value between 5..40 for the radius
    r = random.randint(10,20)
    # randomize an integer value for the position
    x,y = random.randint(r,scr_w-r), random.randint(r,scr_h-r)
    # add position x,y and radius in list(n=0;first)
    if n == 0:
        pos_x.append(x)
        pos_y.append(y)
        radius.append(r)
        n += 1
    else:
        #check for create circle
        for i in range(n):
            d = math.sqrt((pos_x[i]-x)**2 + (pos_y[i]-y)**2)
            if  d >= radius[i]+r:
                booln = booln and True
            else:
                booln = booln and False
        if booln == True:
            pos_x.append(x)
            pos_y.append(y)
            radius.append(r)
            n += 1

for j in range(n):
    # random color 
    color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    # randomize a position (x,y)
    pygame.draw.circle( surface, color, (pos_x[j],pos_y[j]), radius[j] )

# look up the biggest circle
r_max = max(radius)
index_r_max = radius.index(r_max)

# Run until the user asks to quit
running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick( 30 ) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click
            click = pygame.mouse.get_pressed()
            # get mouse position
            pos_mouse = pygame.mouse.get_pos()
            pos_mouse = list(pos_mouse)
            # check to delete the biggest circle
            if click == (True,False,False):
                d = math.sqrt((pos_mouse[0]-pos_x[index_r_max])**2 + (pos_mouse[1]-pos_y[index_r_max])**2)
                if d <= r_max:
                    pygame.draw.circle( surface, (0,0,0), (pos_x[index_r_max],pos_y[index_r_max]), r_max )

    # fill the screen with the white color
    screen.fill((0,0,0))
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    # update the screen display
    pygame.display.update()

pygame.quit()