
import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )
GPIO.setup( 36, GPIO.IN )

try:
    while(1):
       print( "AC val: ", GPIO.input( 36 ) )
except KeyboardInterrupt:
    pass

GPIO.cleanup() 
