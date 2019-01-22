import math

class Target:
    Xmax = 0                                                # will hold the value of the maximum X value
    Ymax = 0                                                # will hold the value of the maximum Y value
    Xmin = 1000                                             # will hold the value of the minumum X value
    Ymin = 1000                                             # will hold the value of the minimum Y value
    Xmid = 0                                                # will hold the X value of the center point
    Ymid = 0                                                # will hold the Y value of the center point

# default initial method that initializes variables stated above
    def __init__(self, corners, isLeft):
        for corner in corners:                                # for loop that iterates through each corner array in the given array
            x = corner[0][0]
            y = corner[0][1]
            if self.Xmax < x:                     # series of if statements that get the minimum and maximum x and y values of the corners
                self.Xmax = x
            if self.Xmin > x:
                self.Xmin = x
            if self.Ymax < y:
                self.Ymax = y
            if self.Ymin > y:
                self.Ymin = y
        self.hypotenuse = math.hypot(corners[0][0][0] - corners[2][0][0], corners[0][0][1] - corners[2][0][1])
        self.Xmid = int((self.Xmax + self.Xmin)/2)
        self.Ymid = int((self.Ymax + self.Ymin)/2)
        self.isLeft = isLeft

 # getter method for the center x and y values
    def getCenter(self):
        return (self.Xmid, self.Ymid)

 # getter method for the width of the target
    def getWidth(self):
        return self.Xmax - self.Xmin

 # getter method for the height of the target
    def getHeight(self):
        return self.Ymax - self.Ymin

    def calculateTargetCenter(self):
        delta = self.hypotenuse/math.hypot(2, 5.5) * 4
        if self.isLeft:
            return self.Xmax + delta
        return self.Xmin - delta
