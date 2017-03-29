import RPi.GPIO as GPIO
import Navigation
import Vector

import time

#GPIO.cleanup()
print("Start")

#Initialize navigation
startPosition = Vector.Vector(0.5, 6.5)#measured in feet
startRotation = 35.0
nav = Navigation.Navigation(startPosition, startRotation )

# However long we have to map the whole thing
duration = 360.0
startTime = time.time()


counter = 0
lastTime = time.time()
POLL_RATE = 1.0
DELTA_TIME = 1/POLL_RATE 

GPIO.setmode(GPIO.BOARD)

try:
    #Start main loop
    while True:
        # Update the robot state
        nav.Update()
        
        counter += 1
        if time.time() - lastTime > DELTA_TIME:
            print( "Times run: ", counter )
            counter = 0
            lastTime = time.time()        

        # Stop the program once we've hit 6 minutes
        if( time.time() - startTime > duration ):
            endTime = time.time()
            break

        #print(str(reader.GetSensorValue()))
except KeyboardInterrupt:
    pass

# Clean up everything once we're done
nav.Cleanup()
GPIO.cleanup()

print("Called Update() " + str(reader.updateCounter) + " times in " + str(duration) + " seconds.")
print("For " + str(reader.updateCounter / (endTime - startTime)) + " updates per second.")
print("\nFinish")



