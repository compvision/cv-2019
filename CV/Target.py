
class Target:
    Xmax = 0                                                # will hold the value of the maximum X value
    Ymax = 0                                                # will hold the value of the maximum Y value
    Xmin = 1000                                             # will hold the value of the minumum X value
    Ymin = 1000                                             # will hold the value of the minimum Y value
    Xmid = 0                                                # will hold the X value of the center point
    Ymid = 0                                                # will hold the Y value of the center point

# default initial method that initializes variables stated above
    def __init__(self,array):
        for corner in array:                                # for loop that iterates through each corner array in the given array
            if(self.Xmax<corner[0][0]):                     # series of if statements that get the minimum and maximum x and y values of the corners
                self.Xmax = corner[0][0]
            if(self.Xmin>corner[0][0]):
                self.Xmin = corner[0][0]
            if(self.Ymax<corner[0][1]):
                self.Ymax = corner[0][1]
            if(self.Ymin>corner[0][1]):
                self.Ymin = corner[0][1]
        self.Xmid = int((self.Xmax+self.Xmin)/2)
        self.Ymid = int((self.Ymax+self.Ymin)/2)


 # getter method for the center x and y values
    def getCenter(self):
        return(self.Xmid,self.Ymid)

 # getter method for the width of the target
    def getWidth(self):
        return(self.Xmax-self.Xmin)

 # getter method for the height of the target
    def getHeight(self):
        return(self.Ymax-self.Ymin)
