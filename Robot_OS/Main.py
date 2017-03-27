import ACDetectorReader
import Navigation
import Drive
import RPi.GPIO as GPIO
import Vector
import Transform
import MovementFeedback


acDetectorPort = 16
#GPIO.cleanup()
print("Start")

#Initialize ACDetectorReader
reader = ACDetectorReader.ACDetectorReader(acDetectorPort)

#initialize Drive
#drive = Drive.Drive("/dev/ttyACM0")
driveBoard = "/dev/ttyACM0"
mapBoard = "/dev/ttyUSB0"

#Initialize navigation
startPosition = Vector.Vector(0.5, 6.5)#measured in feet
startRotation = 0.0
nav = Navigation.Navigation(startPosition, startRotation, driveBoard, mapBoard)

#Initialize MovementFeedback
#movementFeedback = MovementFeedback.MovementFeedback(drive)
#drive.SetMotors(Transform.Transform(Vector.Vector(0.0, 0.0), 050.0))

# However long we have to map the whole thing
duration = 360.0

try:
    #Start main loop
    while(1):
        # Update all sensor input
        reader.Update()
        nav.Update(reader.GetSensorValue())
    
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



