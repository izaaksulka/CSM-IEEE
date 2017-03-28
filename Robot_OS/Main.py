import RPi.GPIO as GPIO
import Navigation
import Vector

import time

#GPIO.cleanup()
print("Start")

#Initialize navigation
startPosition = Vector.Vector(0.5, 6.5)#measured in feet
startRotation = 45.0
nav = Navigation.Navigation(startPosition, startRotation )

# However long we have to map the whole thing
duration = 360.0

counter = 0
lastTime = time.time()
POLL_RATE = 1.0
DELTA_TIME = 1/POLL_RATE 

try:
    #Start main loop
    while(1):
        # Update all sensor input
        nav.Update(reader.GetSensorValue())
        
        counter += 1
        if time.time() - lastTime > DELTA_TIME:
            print( "Times run: ", counter )
            counter = 0
            lastTime = time.time()        

        if(reader.GetAge() > duration):
            break

        #print(str(reader.GetSensorValue()))
except KeyboardInterrupt:
    pass

# Clean up everything once we're done
nav.StopAllMotors()
GPIO.cleanup()

print("Called Update() " + str(reader.updateCounter) + " times in " + str(duration) + " seconds.")
print("For " + str(reader.updateCounter / duration) + " updates per second.")
print("\nFinish")



