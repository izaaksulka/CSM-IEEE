import RPi.GPIO as GPIO
from random import randrange


PORTS =[ 21,22,23,24,26,27,28 ]

NUMBERS = [ "0110000","1101101","1111001", "0110011", "1011011", "1011111" ]

class SevenSegment:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(PORTS[0], GPIO.OUT ) 
        GPIO.setup(PORTS[1], GPIO.OUT )        
        GPIO.setup(PORTS[2], GPIO.OUT )        
        GPIO.setup(PORTS[3], GPIO.OUT )        
        GPIO.setup(PORTS[4], GPIO.OUT )        
        GPIO.setup(PORTS[5], GPIO.OUT )        
        GPIO.setup(PORTS[6], GPIO.OUT )

    def SetRandomNumber(self):

        displayNum = randrange(0,6)
        bitPattern = NUMBERS[displayNum]

        for i in range(7):
            if bitPattern[i] == '1':
                GPIO.output(PORTS[i], GPIO.HIGH)
            else:
                GPIO.output(PORTS[i], GPIO.LOW)
            


sevenSegment = SevenSegment()

sevenSegment.SetRandomNumber()

GPIO.cleanup()
