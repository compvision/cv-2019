from Target import Target
from TargetDetector import TargetDetector as Detector
from TargetProcessor import TargetProcessor as Processor
from networktables import NetworkTables
import numpy as np
import cv2

minThreshold = np.array([80, 35, 85], np.uint8)
maxThreshold = np.array([255, 255, 255], np.uint8)
lightblue = (255, 221, 0)                                                       # variable for the lightblue color
focalLength = 720                                                               # focal length of camera
NetworkTables.initialize(server = "roboRIO-3341-FRC.local")
table = NetworkTables.getTable("cv")

leftCenter = 0
rightCenter = 0
targetCenter = 0

# method that prints out the values in a nice format
def displayValues():
    cv2.putText(frame, "Distance: " + str(proc.getDistance()) + " inches", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    cv2.putText(frame, "Azimuth: " + str(proc.getAzimuth()), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    cv2.putText(frame, "Altitude: " + str(proc.getAltitude()), (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

#------------------------------- FOR LIVE VIDEO -------------------------------#
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_BRIGHTNESS, 0)
cam.set(cv2.CAP_PROP_CONTRAST, 0)
cam.set(cv2.CAP_PROP_SATURATION, 1)

while(True):                                                                    # while loop for continuous analyzation of frames through video capture
    ret, frame = cam.read()
    if not ret:                                                                 # checks if boolean value ret is false
        continue
    h, w = frame.shape[:2]                                                       # gets the height and width of the frame for analyzation purposes
    imgXcenter = w/2
    imgYcenter = h/2
    det = Detector()                                                            # makes a new TargetDetector object
    proc = Processor()                                                          # makes a new TargetProcessor object

    threshold = det.threshold(minThreshold, maxThreshold, frame)                  # getting thresholded frame
    det.contours(threshold)                                                     # finding contours based on thresholded frame
    det.filterContours()                                                        # filtering the contours by size and number

    #cv2.line(frame, (xMid, yMid), (xMid, yMid), lightblue, 5)
    if det.foundCorners():                                                   # checking if the corners array returned is not null
        if det.leftRect is not None:
            leftRect = Target(det.leftRect, True)
            targetCenter = leftRect.calculateTargetCenter()
            cv2.putText(frame, "left: " + str(targetCenter), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

            leftCenter = (int)((det.leftRect[0][0][0] + det.leftRect[2][0][0])/2)
            cv2.line(frame, (det.leftRect[0][0][0], det.leftRect[0][0][1]), (det.leftRect[2][0][0], det.leftRect[2][0][1]), lightblue, 5)

            proc.calculateDistance(focalLength, leftRect.ahypotenuse, leftRect.hypotenuse)
        if det.rightRect is not None:
            rightRect = Target(det.rightRect, False)
            targetCenter = rightRect.calculateTargetCenter()
            cv2.putText(frame, "right: " + str(targetCenter), (0, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

            rightCenter = (int)((det.rightRect[0][0][0] + det.rightRect[2][0][0])/2)
            cv2.line(frame, (det.rightRect[0][0][0], det.rightRect[0][0][1]), (det.rightRect[2][0][0], det.rightRect[2][0][1]), lightblue, 5)
            
            proc.calculateDistance(focalLength, rightRect.ahypotenuse, rightRect.hypotenuse)
        if det.leftRect is not None and det.rightRect is not None:
            targetCenter = (leftCenter + rightCenter)/2
            cv2.line(frame, ((int)(targetCenter), 0), ((int)(targetCenter), h), lightblue, 10)

        proc.calculateAzimuth(focalLength, imgXcenter - targetCenter)

    table.putValue("rectAzimuth", proc.getAzimuth())
    table.putValue("rectDistance", proc.getDistance())

    displayValues()                                                             # method displays values in terminal
    cv2.imshow("frame", frame)
    cv2.imshow("threshold", threshold)
    cv2.moveWindow("frame", 0, 20)
    cv2.moveWindow("threshold", 650, 20)

    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        break
