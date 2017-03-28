
import RPi.GPIO as GPIO
import time

POLL_RATE = 1000.0
DELTA_TIME = 1 / POLL_RATE

ENC_A = 15
ENC_B = 16

GPIO.setmode( GPIO.BOARD )
GPIO.setup( ENC_A, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
GPIO.setup( ENC_B, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )

counter = 0
aLastState = GPIO.input( ENC_A )

lastPoll = time.time()

try: 

    while True:
        aState = GPIO.input( ENC_A )
        bState = GPIO.input( ENC_B )

        if time.time() - lastPoll > DELTA_TIME:
            if aState != aLastState:
                if bState != aState:
                    counter += 1
                else:
                    counter -= 1

                print( counter )
        aLastState = aState
except KeyboardInterrupt:
    pass

GPIO.cleanup()
