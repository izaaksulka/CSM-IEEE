
import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )

GPIO.setup( 16, GPIO.IN )

try:
	while 1:
		print( "GPIO Has input: ", GPIO.input( 16 ) )

except KeyboardInterrupt:
	pass

GPIO.cleanup()

