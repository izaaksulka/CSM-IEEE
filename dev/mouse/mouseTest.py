

import pygame
import time 

# Number of reading per second
POLL_RATE = 100
DELTA_TIME = 1 / float(POLL_RATE)

pygame.init()
screen_w = pygame.display.Info().current_w
screen_h = pygame.display.Info().current_h
screen = pygame.display.set_mode( ( 300, 300 ), pygame.NOFRAME )
width, height = screen.get_size()
pygame.mouse.set_pos( width/2, height/2 ) 
pos = (0, 0)


try:
    lastPolled = time.time()
    lastCount = time.time()
    count = 0 
    while True:
        #print( time.time() )
        if time.time() - lastPolled > DELTA_TIME:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mPos = pygame.mouse.get_pos()
    
            deltaPos = ( mPos[0] - width / 2, mPos[1] - height / 2 )
            print( "Delta Pos: ", deltaPos )
            print( "Cur Pos: ", pos )
            pos = ( pos[0] + deltaPos[0], pos[1] + deltaPos[1] )
            lastPolled = time.time()
            count += 1
            pygame.mouse.set_pos( [ width/2, height/2 ] )
            #print( "Delta: ", deltaPos )
            #print( "Cur Pos: ", pos )
        if time.time() - lastCount > 1.0:
            print( count )
            lastCount = time.time()
            count = 0
        
        
except KeyboardInterrupt:
    pass

