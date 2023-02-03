import math
import numpy as np

#class servo:
    #def __init__(self,x):
        #self.x=0
        #xmax=90
        #xmin=-90
    #def change(self):
        #change=x+change
        #if change>90:
            #change=90
        #elif change<-90:
            #change =-90
def distancex(angcorrection):
    angcorrection=np.radians(angcorrection)
    if angcorrection>0:
        distance=5*5+5*5-2*5*5*math.cos(angcorrection)
    else:
        distance = -(5*5+5*5-2*5*5*math.cos(angcorrection))
    print(f"this is the distance{distance}")
    return distance
def degreechange(distance):
    costeta=(3**2-distance**2)/(3**2)
    servoanglechange=np.degrees(np.arccos(costeta))
    if distance<0:#change costeta here it is not able to convert from degrees to radians
        servoanglechange=-servoanglechange
    print(f"this is cos teta {costeta}")
    #print(f"this is the distance{distance}")
    #print(f"this is the servoanglechange{servoanglechange}")
    return servoanglechange
def getservodegree(anglecorrection):
    distance=distancex(anglecorrection)
    angle=degreechange(distance)
    print(angle)
    return angle



