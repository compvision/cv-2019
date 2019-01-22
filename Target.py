import math

class Target:
    xMax = 0                                                # will hold the value of the maximum X value
    yMax = 0                                                # will hold the value of the maximum Y value
    xMin = 1000                                             # will hold the value of the minumum X value
    yMin = 1000                                             # will hold the value of the minimum Y value
    xMid = 0                                                # will hold the X value of the center point
    yMid = 0                                                # will hold the Y value of the center point

# default initial method that initializes variables stated above
    def __init__(self, corners, isLeft):
        for corner in corners:                                # for loop that iterates through each corner array in the given array
            x = corner[0][0]
            y = corner[0][1]
            if self.xMax < x:                     # series of if statements that get the minimum and maximum x and y values of the corners
                self.xMax = x
            if self.xMin > x:
                self.xMin = x
            if self.yMax < y:
                self.yMax = y
            if self.yMin > y:
                self.yMin = y
        self.hypotenuse = math.hypot(corners[0][0][0] - corners[2][0][0], corners[0][0][1] - corners[2][0][1])
        self.xMid = int((self.xMax + self.xMin)/2)
        self.yMid = int((self.yMax + self.yMin)/2)
        self.isLeft = isLeft

 # getter method for the center x and y values
    def getCenter(self):
        return (self.xMid, self.yMid)

 # getter method for the width of the target
    def getWidth(self):
        return self.xMax - self.xMin

 # getter method for the height of the target
    def getHeight(self):
        return self.yMax - self.yMin

    def calculateTargetCenter(self):
        delta = self.hypotenuse/math.hypot(2, 5.5) * 4
        if self.isLeft:
            return self.xMax + delta
        return self.xMin - delta
