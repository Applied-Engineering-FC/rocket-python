import math
from variables import getmass,getthrust
from matplotlib import pyplot as plt
class rocket:#defining the rocket itself and it's variables
    def __init__(self,speed,altitude,acceleration,first_motor,second_motor,thrust,mass,phase,time,land):
        self.speed=speed
        self.altitude=altitude
        self.acceleration=acceleration
        self.first_motor=first_motor
        self.second_motor=second_motor
        self.thrust=thrust
        self.mass=mass
        self.phase=phase
        self.time=time
        self.land=land
def rocketacceleration(thrust,mass):#getting the acceleration of the rocket
    a = (thrust - (mass * (9.81))) / mass
    return a
def rocketspeed(acceleration,speed):#getting the speed of the rocket
    speed=acceleration*0.01+speed
    return speed
def rocketheight(acceleration,altitude,velocity):#getting the height of the rocket
    altitude = 0.5 * acceleration*((0.01)**2)+velocity*0.01+ altitude
    return altitude
def startsecondengine(mass,speed,altitude,thrust,time):
    otime=time
    phase=4
    mass = getmass(mass, phase)  # getting the mass of the rocket
    thrust = getthrust(phase, thrust)  # getting the thrust of the rocket
    acceleration = rocketacceleration(thrust, mass)  # getting acceleration
    speed = rocketspeed(acceleration, speed)  # getting speed
    altitude = rocketheight(acceleration, altitude, speed)  # getting altitude
    phase=5
    while altitude>-2:
        time=time+1
        mass=getmass(mass, phase)  # getting the mass of the rocket
        thrust = getthrust(phase,thrust)  # getting the thrust of the rocket
        acceleration =rocketacceleration(thrust, mass)  # getting acceleration
        speed =rocketspeed(acceleration, speed)  # getting speed
        altitude = rocketheight(acceleration, altitude, speed)  # getting altitude
        if time-otime==350:
            phase=6
        if -2<altitude<2 and -0.5<speed<0.5:
            return 1,time
        if -1< altitude <1 and (speed<-1 or speed>1):
            return 0