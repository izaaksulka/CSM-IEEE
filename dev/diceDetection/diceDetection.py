import cv2 as cv
import numpy as np

cap = cv.VideoCapture();

if not cap.open(0):
    print ("Camera could not be opened.");
    #exit();


while (True):
    #capture frame
    ret, frame = cap.read();

    #Operations on the frame start here

    #convert to gray for better edge detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY);

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                              100,#minDistance
                              200,#edgePrecision
                              30,#edgesNeeded 
                              0,#minRadius
                              50#maxRadius
                              );

    if circles is not None:
        print (len(circles));
        circles = np.uint16(np.around(circles));
        for i in circles[0,:]:
            #draw the outer circle to the screen
            cv.circle(frame,(i[0],i[1]), i[2] , (0,255,0), 2);
            #draw the center of the circle
            cv.circle(frame, (i[0],i[1]), 2, (0,0,255),3);
            

    cv.imshow('frame', frame);

    if cv.waitKey(10) & 0xFF == ord('q'):
        break;

cap.release();
cv.destroyAllWindows();
