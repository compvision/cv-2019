import numpy as np
import cv2
class TargetDetector:
    lightblue = (255, 221, 0)                                   # variable that stands for the lightblue color
    contours = None                                             # variable that will hold the array of contours
    index = None                                                # index variable that will hold the index of the proper contour
    corners = None                                              # variable that holds the array of corner points
    isRect = False
    isCross = False

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
            if(len(approx)==4 and cv2.contourArea(approx)>1000):
                # and cv2.contourArea(approx)>300
                self.index = c
                self.corners = approx
                self.isRect = True
                self.isCross = False
            if(len(approx) == 12 and cv2.contourArea(approx) > 500):
                # and cv2.contourArea(approx)>300
                self.index = c
                self.corners = approx
                self.isCross = True
                self.isRect = False

# getter method that returns the contours array, index of significant contour, and the corners array
    def getContours(self):
        return self.contours,self.index,self.corners,self.isCross,self.isRect
