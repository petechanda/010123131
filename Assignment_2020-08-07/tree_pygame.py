import pygame
from math import *

pygame.init()
pygame.display.set_caption('Boolean Expression Tree')
clock = pygame.time.Clock()
scr_w, scr_h = 800, 500
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

pygame.font.init() 
text_font = pygame.font.SysFont('FreesiaUPC', 40)


exp_lst = ['+', ['&', 'l0', 'l1'], ['!', None, ['&', 'l1', 'l2']]]
def creat_node_tree(exp_lst):
    r = 30
    x,y = int(scr_w/2), int(r)
    for i in range(len(exp_lst)):
        # root
        if i == 0:
            x,y = x,y
            # circle
            pygame.draw.circle(surface, (0,0,0), (x,y), r, 2)
            # text
            text_surface = text_font.render( exp_lst[i], False, (0,0,0) )
            text_width, text_height = x-8,y-8
            surface.blit(text_surface, (text_width, text_height))
        # left
        elif i == 1:
            if exp_lst[i] == 'None':
                continue
            # line
            x_start_left,y_start_left = int(x-r/sqrt(2)), int(y+r/sqrt(2))
            x_end_left,y_end_left = int(x-r*sqrt(2)), int(y+r*sqrt(2))
            pygame.draw.line(surface, (0,0,0), (x_start_left,y_start_left), (x_end_left,y_end_left), 5)
            # position
            x,y = int(x-(r/sqrt(2))*3), int(y+(r/sqrt(2))*3)
            check_lst = str(type(exp_lst[i]))
            if check_lst == "<class 'list'>":
                creat_node_tree(exp_lst[i])
            else:
                # circle
                pygame.draw.circle(surface, (0,0,0), (x,y), r, 2)
                # text
                text_surface = text_font.render( exp_lst[i], False, (0,0,0) )
                text_width, text_height = x-8,y-8
                surface.blit(text_surface, (text_width, text_height))
        # right
        elif i == 2:
            # line
            x_start_right,y_start_right = int(x+r/sqrt(2)), int(y+r/sqrt(2))
            x_end_right,y_end_right = int(x+r*sqrt(2)), int(y+r*sqrt(2))
            pygame.draw.line(surface, (0,0,0), (x_start_right,y_start_right), (x_end_right,y_end_right), 5)
            # position
            x,y = int(x+(r/sqrt(2))*3), int(y+(r/sqrt(2))*3)
            check_lst = str(type(exp_lst[i]))
            if check_lst == "<class 'list'>":
                creat_node_tree(exp_lst[i])
            else:
                # circle
                pygame.draw.circle(surface, (0,0,0), (x,y), r, 2)
                # text
                text_surface = text_font.render( exp_lst[i], False, (0,0,0) )
                text_width, text_height = x-8,y-8
                surface.blit(text_surface, (text_width, text_height))
        
creat_node_tree(exp_lst)

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(surface, (0,0))
    pygame.display.update()
    
pygame.image.save(screen, 'boolean_tree.jpg')
pygame.quit()