import ACDetectorReader
import Navigation
import Drive
import DriveVector
import RPi.GPIO as GPIO
import Vector
import Transform
import MovementFeedback

def UpdateAll():
    reader.Update();
    deltaTransform = movementFeedback.Update();

    
    nav.Update(reader.GetSensorValue(), deltaTransform);

    
acDetectorPort = 16;
#GPIO.cleanup();
print("Start");

#Initialize ACDetectorReader
reader = ACDetectorReader.ACDetectorReader(acDetectorPort);

#initialize Drive
drive = Drive.Drive("/dev/ttyACM1");

#Initialize navigation
startPosition = Vector.Vector(0.5, 6.4999);#measured in feet
startRotation = 0.0;
nav = Navigation.Navigation(startPosition, startRotation, drive);

#Initialize MovementFeedback
movementFeedback = MovementFeedback.MovementFeedback(drive);
#drive.SetMotors(Transform.Transform(Vector.Vector(0.0, 0.0), 050.0));
duration = 20.0;
#Start main loop
while(1):
    #reader.Update(); #Update has to get called a lot, otherwise this tool doesn't work very well.
    UpdateAll();
    
    if(reader.GetAge() > duration):
        break;

    #print(str(reader.GetSensorValue()));


GPIO.cleanup();

print("Called Update() " + str(reader.updateCounter) + " times in " + str(duration) + " seconds.")
print("For " + str(reader.updateCounter / duration) + " updates per second.");
print("\nFinish");



