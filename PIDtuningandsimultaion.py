import random
from servo import getservodegree
import numpy as np
from variables import getmass,getthrust
from calculations import Trcalculate,Ttcalculate,Newangleformed,geta,geth,getv,getcorrectionalange
import matplotlib.pyplot as plt
#initializing variables
initmass=1#in kg
initvelocity=0#velocity
initheight=0#setting the initial height
pivotdistance=0.4#distance from the center of mass till the pivot point
g=-9.81#gravitational constant
error=0#error in degrees
time=-1#declaring the time, 1 will be equal to 0.1 seconds
fixederror=0#starting with a fixed error
startoferror=0#getting a start error value
integralgain=0#setting the integral gain
olderror=0#olderror
intgain=0#integral gain set to zero
arrmass=[]#declaring the array of mass
arrthrust=[]#declaring the array of thrust
arrangle=[]#declaring array of angle
arre=[]#array of the error
arra=[]#declaring the array of acceleration
arrv=[]#declaring the array of velocity
arrh=[]#declaring the array of altitude
arrs=[]#servo degree change
randomerror=random.randint(-20,20)
while time!=99:
    time=time+1
    randomerror = random.randint(-50,50)
    if -10<randomerror<10:
        if time<80:
            fixederror=fixederror+randomerror
    initmass=getmass(time,initmass)
    arrmass.append(initmass)#getting the mass
    arrthrust.append(getthrust(time))#getting the thrust
    if time==0:
        arra.append(0)
    else:
        arra.append(geta(arrthrust[time],initmass,g))#getting acceleration

    initvelocity=getv(arra[time],initvelocity)
    arrv.append(initvelocity)#getting the velocity

    initheight=geth(arra[time],arrv[time],initheight)
    arrh.append(initheight)#getting height
    correction=getcorrectionalange(fixederror,startoferror,integralgain)#getting the correction angle
    startoferror=correction[0]
    arre.append(startoferror)
    angle=correction[1]
    print(f"this is the angle correction{angle}")
    arrangle.append(angle)
    integralgain=correction[2]
    arrs.append(getservodegree(angle))


    torqueerror=Trcalculate(initmass,g,0.4,fixederror)#getting torque of error

    torquerocket=Ttcalculate(0.4,angle,arrthrust[time])#getting torque of the rocket

    fixederror=Newangleformed(torqueerror,torquerocket,initmass,g,angle,arrthrust[time],0.4,fixederror)
x=np.arange(0,100,1)
y=np.arange(0,100,1)
plt.plot(arrangle, 'b-', label='angle change')
plt.plot(arre, 'r-', label='error')
plt.plot(arrs, 'g-', label='servo angle change')
plt.legend()
plt.show()
plt.show()
