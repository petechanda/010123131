# Student ID : 6201012630029
# Threading ข้อ6

import threading
import time
import cmath
import pygame
from random import randint, randrange, random
from math import*

print( 'File:', __file__ )

def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 500, 500
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# Divided area
N = 2
ny = int(sqrt(N))
while N%ny != 0:
    ny += 1
nx = int(N/ny)

#threading
def thread_mandelbrot(nx,ny):
    w2, h2 = scr_w/nx, scr_h/ny
    scale = 0.010
    offset = complex(-0.55,0.0)
    for x in range(scr_w):
        for y in range(scr_h):
            re = scale*(x-w2) + offset.real
            im = scale*(y-h2) + offset.imag
            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            surface.set_at( (x,y), (255-r,255-g,255-b) )
            
list_threads = []
for ix in range(int(nx)):
    for iy in range(int(ny)):
        t = threading.Thread(target=thread_mandelbrot, args=(nx,ny))
        list_threads.append(t)

for t in list_threads:
    t.start()

for t in list_threads:
    t.join() 


running = True
while running:

    # draw the surface on the screen
    screen.blit( surface, (0,0) )
    # update the display
    pygame.display.update()

    clock.tick(1.0) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print('The main thread is finished...')
