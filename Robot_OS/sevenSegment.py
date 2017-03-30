import RPi.GPIO as GPIO
from random import randrange
from time import sleep

#PORTS =[ 21,24,26,29,31,23,22 ]
PORTS =[ 23,22,21,24,26,29,31 ]


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

        for port in PORTS:
            GPIO.output(port, GPIO.LOW)

    def SetRandomNumber(self):

        displayNum = 4
        print ( displayNum + 1 )
        bitPattern = NUMBERS[displayNum]

        for i in range(7):
            if bitPattern[i] == '1':
                GPIO.output(PORTS[i], GPIO.HIGH)
            else:
                GPIO.output(PORTS[i], GPIO.LOW)
            

'''
sevenSegment = SevenSegment()


for k in range(10):
    for port in PORTS:
        GPIO.output(port, GPIO.HIGH)
        print (port)
        sleep(0.5)
        GPIO.output(port, GPIO.LOW)

sevenSegment.SetRandomNumber()
input( "cake?" )
GPIO.cleanup()
'''
