# STUDENT NUMBER : 6201012630029
# Assignment 2

import pygame 
import random
import math

# initialize PyGame
pygame.init()

# set window caption
pygame.display.set_caption('Assignment2') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

#check for draw circle
pos_x = []
pos_y = []
radius = []
colors = []
V = []
n = 0
while n<10:
    booln = True
    # random radius
    r = random.randint(10,20)
    # random position (x,y)
    x,y = random.randint(r,scr_w-r), random.randint(r,scr_h-r)
    # random color 
    color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    # add position x,y and radius in list(n=0;first)
    if n == 0:
        pos_x.append(x)
        pos_y.append(y)
        radius.append(r)
        colors.append(color)
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
            colors.append(color)
            n += 1

# random direction of circle movememnt
for i in range(n):
    random_vx = [random.randint(-5,-1),random.randint(1,5)]
    vx = random.choice(random_vx)
    random_vy = [random.randint(-5,-1),random.randint(1,5)]
    vy = random.choice(random_vy)
    V.append([vx,vy])

# circle movement
def move_cir():
    for i in range(n):
        pos_x[i] = pos_x[i] + V[i][0]
        pos_y[i] = pos_y[i] + V[i][1]

# create circle 
def draw_cir():
    for i in range(n):
        pygame.draw.circle( screen, colors[i], (pos_x[i],pos_y[i]), radius[i] )

# circle hit the screen
def hit_scr():
    for i in range(n):
        if pos_x[i] <= radius[i] or pos_x[i] >= scr_w-radius[i]:
            V[i][0] = V[i][0] * (-1)
        if pos_y[i] <= radius[i] or pos_y[i] >= scr_h-radius[i]:
            V[i][1] = V[i][1] * (-1)

# circle hit other circle
def hit_other_cir():
    for i in range(n):
        for j in range(n):
            if i<j:
                d = math.sqrt((pos_x[i]-pos_x[j])**2 + (pos_y[i]-pos_y[j])**2)
                if d <= radius[i] + radius[j]:
                    if V[i][0] > 0 and V[i][1] > 0:
                        if (V[j][0]>0 and V[j][1]>0) or (V[j][0]<0 and V[j][1]<0):
                            V[i][0] = V[i][0] * (-1)
                            V[i][1] = V[i][1] * (-1)
                            V[j][0] = V[j][0] * (-1)
                            V[j][1] = V[j][1] * (-1)
                        elif V[j][0]>0 and V[j][1]<0:
                            V[i][1] = V[i][1] * (-1)
                            V[j][1] = V[j][1] * (-1)
                        elif V[j][0]<0 and V[j][1]>0:
                            V[i][0] = V[i][0] * (-1)
                            V[j][0] = V[j][0] * (-1)
                    elif V[i][0]>0 and V[i][1]<0:
                        if (V[j][0]>0 and V[j][1]<0) or (V[j][0]<0 and V[j][1]>0):
                            V[i][0] = V[i][0] * (-1)
                            V[i][1] = V[i][1] * (-1)
                            V[j][0] = V[j][0] * (-1)
                            V[j][1] = V[j][1] * (-1)
                        elif V[j][0]<0 and V[j][1]<0:
                            V[i][0] = V[i][0] * (-1)
                            V[j][0] = V[j][0] * (-1)
                        elif V[j][0]>0 and V[j][1]>0:
                            V[i][1] = V[i][1] * (-1)
                            V[j][1] = V[j][1] * (-1)
                    elif V[i][0]<0 and V[i][1]<0:
                        if (V[j][0]<0 and V[j][1]<0) or (V[j][0]>0 and V[j][1]>0):
                            V[i][0] = V[i][0] * (-1)
                            V[i][1] = V[i][1] * (-1)
                            V[j][0] = V[j][0] * (-1)
                            V[j][1] = V[j][1] * (-1)
                        elif V[j][0]>0 and V[j][1]<0:
                            V[i][0] = V[i][0] * (-1)
                            V[j][0] = V[j][0] * (-1)
                        elif V[j][0]<0 and V[j][1]>0:
                            V[i][1] = V[i][1] * (-1)
                            V[j][1] = V[j][1] * (-1)
                    elif V[i][0]<0 and V[i][1]<0:
                        if (V[j][0]<0 and V[j][1]>0) or (V[j][0]>0 and V[j][1]<0):
                            V[i][0] = V[i][0] * (-1)
                            V[i][1] = V[i][1] * (-1)
                            V[j][0] = V[j][0] * (-1)
                            V[j][1] = V[j][1] * (-1)
                        elif V[j][0]>0 and V[j][1]>0:
                            V[i][0] = V[i][0] * (-1)
                            V[j][0] = V[j][0] * (-1)
                        elif V[j][0]<0 and V[j][1]<0:
                            V[i][1] = V[i][1] * (-1)
                            V[j][1] = V[j][1] * (-1)

# look up the biggest circle
r_max = max(radius)
index_r_max = radius.index(r_max)                    

# Run until the user asks to quit
running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick(60)

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
                    colors[index_r_max] = (0,0,0)

    # fill the screen with the white color
    screen.fill((0,0,0))
    # call function
    move_cir()
    draw_cir()
    hit_scr()
    hit_other_cir()
    # update the screen display
    pygame.display.update()

pygame.quit()