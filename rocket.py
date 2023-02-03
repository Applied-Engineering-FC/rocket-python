import math
from variables import getmass,getthrust
from matplotlib import pyplot as plt
class rocket:
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
        land=0
        speed1=[]
        altitude=[]
        acceleration=[]
        thrust=[]
        mass=[]
        speed1.append(self.speed)
        acceleration.append(self.acceleration)
        altitude.append(self.altitude)
        thrust.append(self.thrust)
        mass.append(self.mass)#arrays inside of the class to be able to determine the phases
        if self.mass==1:#standing on the ground
            phase=0
        if self.first_motor==0 and self.second_motor==1:#motor is working and starts loosing mass
            phase=1
        if self.first_motor==0 and thrust==0:#first motor burn off
            phase==2
        if phase==2:
            if altitude[self.time-2]<altitude[self.time-1]and altitude[self.time-1]>altitude[self.time]:#peak
                phase==3
        if self.second_motor==0 and mass[time-1]==mass[time]:#falling part
            phase==4
        if self.second_motor==0 and self.thrust>0:#burn of second motor
            phase==5
        if self.second_motor==0 and self.thrust==0:#end of motor burn phase
            phase==6
        if self.land==1:
            return

        #phase determination

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
            return 0,0
def getA0time(mass,thrust,speed,altitude,time):
    while altitude >0:
        time = time + 1
        mass = getmass(mass, 5)  # getting the mass of the rocket
        thrust = getthrust(5, thrust)  # getting the thrust of the rocket
        acceleration = rocketacceleration(thrust, mass)  # getting acceleration
        speed = rocketspeed(acceleration, speed)  # getting speed
        altitude = rocketheight(acceleration, altitude, speed)  # getting altitude
        return time
def getthrustcontrol(thrust,altitude,speed,mass,timeo,timeA0,time):
        force=(speed**2)/(2*altitude)
        neededthrust =mass * 9.81+force
        print(f"this is needed thrust{neededthrust}")
        thrustpercentage = neededthrust / thrust
        if thrustpercentage>1:
            return 1
        return thrustpercentage
def rocketbrain(mass,speed,altitude,acceleration,first_motor,second_motor,thrust):#the brain of the rocket
    time=0
    done=0
    error1=0
    counter=0
    integralgain=0
    timeA0=0
    timex=0
    phase=0
    land=0
    timeo=0
    x1=[]
    y=0
    spector=rocket(speed,altitude,acceleration,first_motor,second_motor,thrust,mass,phase,time,land)
    spector.speed=0
    spector.mass=1.2
    spector.altitude=0
    spector.acceleration=0
    spector.first_motor=1
    spector.second_motor=1
    spector.thrust=0
    spector.phase=0
    spector.time=time#set the initial condition of the rocket itself
    speed = []
    altitude = []
    acceleration = []
    thrust = []
    mass = []
    time=[]
    error=[]
    time1=0
    timeo=0
    #declared all the arrays used to store the information
    #start
    while spector.land==0:
        time.append(time1)
        if time1==0:
            spector.phase=1
        #print(time1)
        #print(spector.phase)

        mass.append(spector.mass)
        thrust.append(spector.thrust)
        acceleration.append(spector.acceleration)
        speed.append(spector.speed)
        altitude.append(spector.altitude)
        #recording the measurments
        spector.mass=getmass(spector.mass,spector.phase)#getting the mass of the rocket
        spector.thrust=getthrust(spector.phase,spector.thrust)#getting the thrust of the rocket
        if spector.phase==5:
            timex=timex+1
            y=getthrustcontrol(spector.thrust,spector.altitude,spector.speed,spector.mass,timex,timeA0,time1)#control of the thrust
            print(f"this is y {y}")
            spector.thrust=spector.thrust*y
            fixedthrust=spector.thrust
        spector.acceleration=rocketacceleration(spector.thrust,spector.mass)#getting acceleration
        spector.speed=rocketspeed(spector.acceleration,spector.speed)#getting speed
        spector.altitude=rocketheight(spector.acceleration,spector.altitude,spector.speed)#getting altitude
        #print(spector.height)
        if time1==350:
            spector.phase=2
        if 355<time1<600 and spector.phase<3:
            if altitude[time1-2]<altitude[time1-1] and altitude[time1-1]>altitude[time1]:
                spector.phase=3
        #print(spector.phase)
        time1=time1+1
        if spector.phase==4:
            spector.phase=5
        if spector.phase==3:
            x,timeA0=startsecondengine(spector.mass,spector.speed,spector.altitude,spector.thrust,time1)
            if x==1:
            #if time1==5800:
                spector.phase=4
                timeo=time1
                print(timeo)
        if time1-timeo==360 and spector.phase==5:
            spector.phase=6
        if spector.altitude<-2 :
            spector.land=1
        if time1>1500:
            spector.land=1
        x1.append(0)

    plt.plot(time,speed,altitude)
    plt.plot(x1)
    plt.plot(acceleration)
    plt.show()
#running simulation
shadow=rocket(0,0,0,1,1,0,1,0,0,0)
rocketbrain(shadow.mass,shadow.speed,shadow.altitude,shadow.acceleration,shadow.first_motor,shadow.second_motor,shadow.thrust)

