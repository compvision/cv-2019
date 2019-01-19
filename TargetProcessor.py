import math

class TargetProcessor:
    distance  = 0                                       # variable for distance
    azimuth = -1.0                                         # variable for azimuth
    altitude = -1.0                                        # variable for altitude

    def __init__(self):
        pass

# method that calculates Distance, Azimuth, and Altitude
    def calculate(self,f,w,iw,x,y):
        self.distance = (f*w)/iw
        self.azimuth = math.atan(x/f)*180/math.pi
        self.altitude = math.atan(y/f)*180/math.pi

# getter method that returns distance rounded to two decimal places
    def getDistance(self):
        return round(self.distance,2)

# getter method that returns altitude rounded to four decimal places
    def getAltitude(self):
        return round(self.altitude,4)

# getter method that returns azimuth rounded to four decimal places
    def getAzimuth(self):
        return round(self.azimuth,4)
