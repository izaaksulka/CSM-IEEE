

import pyautogui as gui # Only used to get window dimensions
import pygame
import time 

# Number of reading per second
POLL_RATE = 1000
DELTA_TIME = 1 / float(POLL_RATE)
gui.FAILSAFE = False
width, height = gui.size()

pygame.init()
pygame.display.init()
pygame.mouse.set_pos( width/2, height/2 ) 
pos = (0, 0)


try:
    lastPolled = time.time()
    lastCount = time.time()
    count = 0 
    while True:
        #print( time.time() )
        if time.time() - lastPolled > DELTA_TIME:
            deltaPos = ( pygame.mouse.get_pos()[0] - width/2, pygame.mouse.get_pos()[1] - height/2 )
            #print( "Delta Pos: ", deltaPos )
            #print( "Cur Pos: ", pos )
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

