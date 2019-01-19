import numpy as np
import cv2
class TargetDetector:
    lightblue = (255, 221, 0)                                   # variable that stands for the lightblue color
    corners = None                                              # variable that holds the array of corner points
    leftRect = None
    rightRect = None
    isCorrectOrientation = False


    def __init__(self):
        pass

# method that converts frame to HSV and then returns new frame of thresholded values
    def threshold(self, min, max, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, min, max)
        return thresh

# method that finds and sets the contours to the variable contours for later usage
    def contours(self, threshold):
        self.contours = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]

# method that iterates through each contour in the contours array and filters them by number and size
    def filterContours(self):
        for c in self.contours:
            epsilon = 0.01 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c ,epsilon, True)
            if(len(approx) == 4 and cv2.contourArea(approx) > 1000):
                self.corners = approx
                if self.isLeftRect(approx):
                    self.leftRect = approx
                if self.isRightRect(approx):
                    self.rightRect = approx

    def isLeftRect(self, corners):
        highest = [0] * 2
        lowest = [1000] * 2
        for corner in corners:
            if(corner[0][0] > highest[0]):
                highest = corner[0]
            if(corner[0][0] < lowest[0]):
                lowest = corner[0]
        return highest[1] < lowest[1]

    def isRightRect(self, corners):
        highest = [0] * 2
        lowest = [1000] * 2
        for corner in corners:
            if(corner[0][0] > highest[0]):
                highest = corner[0]
            if(corner[0][0] < lowest[0]):
                lowest = corner[0]
        return highest[1] > lowest[1]


# getter method that returns the contours array, index of significant contour, and the corners array
    def getCorners(self):
        return self.corners
