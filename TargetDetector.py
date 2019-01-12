import numpy as np
import cv2
class TargetDetector:
    lightblue = (255, 221, 0)                                   # variable that stands for the lightblue color
    contours = None                                             # variable that will hold the array of contours
    index = None                                                # index variable that will hold the index of the proper contour
    corners = None                                              # variable that holds the array of corner points
    leftRect = False
    rightRect = False
    isCorrectOrientation = False


    def __init__(self):
        pass

# method that converts frame to HSV and then returns new frame of thresholded values
    def threshold(self,min,max,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, min, max)
        return thresh

# method that finds and sets the contours to the variable contours for later usage
    def Contours(self,threshold):
        self.contours = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]

# method that iterates through each contour in the contours array and filters them by number and size
    def filterContours(self):
        for c in range(len(self.contours)):
            epsilon = 0.01 * cv2.arcLength(self.contours[c],True)
            approx = cv2.approxPolyDP(self.contours[c],epsilon, True)
            if(len(approx)==4 and cv2.contourArea(approx)>500):
                self.index = c
                self.corners = approx

    def isLeftRect(self, corners):
        firsthighestY = [0]*2
        secondhighestY = [0]*2
        for corner in corners[0]:
            if(corner[1]>firsthighestY[1]):
                firsthighestY = corner
            if(corner[1]>secondhighestY[1] and corner[1]!= firsthighestY[1]):
                secondhighestY = corner
        return firsthighestY[0]< secondhighestY[0]
    
    def isRightRect(self, corners):
        firsthighestY = [0]*2
        secondhighestY = [0]*2
        for corner in corners[0]:
            if(corner[1] > firsthighestY[1]):
                firsthighestY = corner
            if(corner[1] > secondhighestY[1] and corner[1] != firsthighestY[1]):
                secondhighestY = corner
        return (firsthighestY[0] < secondhighestY[0])


# getter method that returns the contours array, index of significant contour, and the corners array
    def getContours(self):
        return self.contours,self.index,self.corners, self.isCorrectOrientation
