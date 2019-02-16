import math

class TargetProcessor:
    distance  = 0                                       # variable for distance
    azimuth = -100                                         # variable for azimuth
    altitude = -100                                        # variable for altitude

    def __init__(self):
        pass

    def calculateAzimuth(self, f, x):
        self.azimuth = math.atan(x/f) * 180/math.pi

    def calculateDistance(self, f, ahyp, ihyp):
        self.distance = (f * ahyp)/ihyp

# getter method that returns distance rounded to two decimal places
    def getDistance(self):
        return round(self.distance, 2)

# getter method that returns azimuth rounded to four decimal places
    def getAzimuth(self):
        return round(self.azimuth, 4)

# getter method that returns altitude rounded to four decimal places
    def getAltitude(self):
        return round(self.altitude, 4)
