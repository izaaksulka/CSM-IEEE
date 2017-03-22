import RPi.GPIO as GPIO

class holoMotor:

    # Normal class variables
    # ... python's weird    
    # pwmPort
    # dirPort
    # motorPWM

    def __init__( self, E, M ):
        self.pwmPort = E
        self.dirPort = M
        
        GPIO.setup( self.pwmPort, GPIO.OUT )
        GPIO.setup( self.dirPort, GPIO.OUT )
            
        self.motorPWM = GPIO.PWM( self.pwmPort, 50 )
        
        self.running = False;

    def setSpeed( self, speed ): 
    
        print( speed )
    
        # When we start the PWM from a stopped state we
        # need to turn the PWM on   
        if self.running == False:
            self.motorPWM.start(1)
            self.running = True
                
        if( speed > 0.0 ):
            self.motorPWM.ChangeDutyCycle( abs( speed ) )
            GPIO.output( self.dirPort, GPIO.LOW )
        elif( speed < 0.0 ):
            self.motorPWM.ChangeDutyCycle( abs( speed ) )
            GPIO.output( self.dirPort, GPIO.HIGH )
        else:
            self.motorPWM.stop()
            self.running = False
