###################################################################
# Student ID : 6201012630029
# Pygame_Camera_Assignment 1
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

scr_w, scr_h = 1280, 720
pygame.init()
camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

# try to capture the next image from the camera 
img = camera.get_image()
pygame.image.save( img, 'image2.jpg' )

# close the camera
camera.stop()

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# get the image size
img_rect = img.get_rect()
img_w, img_h = img_rect.w, img_rect.h

# draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        # draw a green frame (tile)
        rect = (i*rw, j*rh, rw, rh)
        pygame.draw.rect( img, (0,255,0), rect, 1)
        surface.blit( img, rect, rect )

is_running = True 
while is_running:
    
# ---------------------------------------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # check button click
            click = pygame.mouse.get_pressed()
            # get mouse position when click
            pos_mouse_down = pygame.mouse.get_pos()
            pos_mouse_down = list(pos_mouse_down)
            # check to delete the biggest circle
            if click == (True,False,False):
                for i in range(M):
                    for j in range(N):
                        if pos_mouse_down[0]>=i*rw and pos_mouse_down[0]<(i+1)*rw:
                            if pos_mouse_down[1]>=j*rh and pos_mouse_down[1]<(j+1)*rh:
                                pos_mouse_down = [i,j]
        elif e.type == pygame.MOUSEBUTTONUP:
            pos_mouse_up = pygame.mouse.get_pos()
            pos_mouse_up = list(pos_mouse_up)
            if click == (True,False,False):
                for i in range(M):
                    for j in range(N):
                        if pos_mouse_up[0]>=i*rw and pos_mouse_up[0]<(i+1)*rw:
                            if pos_mouse_up[1]>=j*rh and pos_mouse_up[1]<(j+1)*rh:
                                pos_mouse_up = [i,j]
                                surface.blit(img, (pos_mouse_up[0]*rw,pos_mouse_up[1]*rh), (pos_mouse_down[0]*rw,pos_mouse_down[1]*rh,rw,rh))
                                surface.blit(img, (pos_mouse_down[0]*rw,pos_mouse_down[1]*rh), (pos_mouse_up[0]*rw,pos_mouse_up[1]*rh,rw,rh))
# --------------------------------------------------------------------------------

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

pygame.quit()
print('Done....')
###################################################################
