
import math

def Trcalculate(m,g,l,teta):#calculates the torque of the weight of the rocket
    torqueeerror=m*g*l*math.sin(math.radians(180-teta))
    #print(f"this is the torque of the error{torqueeerror}")
    return torqueeerror
def Ttcalculate(l,correctionalteta,thrust):#calculating the torque from the thrust
    counterthrust=l*math.sin(math.radians(correctionalteta))*thrust
    #print(f"this is the torque of the thrust{counterthrust}")
    return counterthrust
def Newangleformed(t1,t2,m,g,thetathrut,thrust,l,error):#calculating the new angle
    vec1=[0,-1*g*m]
    vec2=[thrust*math.cos(thetathrut),thrust*math.sin(math.radians(90-thetathrut))]
    resultant=vec1+vec2
    resultantvalue=math.sqrt(resultant[0]**2+resultant[1]**2)
    #print(f"this is the value of the remaining force{resultantvalue}")
    newtorque=t1+t2
    #print(f"this is new torque{newtorque}")
    newanglefreshvalue=newtorque/(l*resultantvalue)
    #print(f"this is new freshvalue{newanglefreshvalue}")
    finalanglevalue=math.degrees(newanglefreshvalue)
    finalanglevalue = error + finalanglevalue
        #print(f"this is new anglevalue{finalanglevalue}")
    return finalanglevalue
def geta(thrust,m,g):#getting acceeration
    a=(thrust-(m*(-g)))/m
    return a
def getv(a,Vo):#getting the velocity
    velocity=a*0.1+Vo
    return velocity
def geth(a,Vo,xo):#getting the altitude
    altitude=0.5*a*0.1**2+Vo*0.1+xo
    return altitude


def getcorrectionalange(randerror, olderror, integralgain):  # getting the correctional angle
    gain = randerror*0.15
    deltagain = (randerror - olderror / 1)*0.3
    integralgain = integralgain + ((randerror*0.0001))
    correctionalangle = gain + integralgain + deltagain
    if correctionalangle>10:
        correctionalangle=10
        newerror = randerror - correctionalangle
    elif correctionalangle<-10:
        correctionalangle=-10
        newerror = randerror - correctionalangle

    else:
        newerror = randerror - correctionalangle
    print(f"PID angle is {correctionalangle}")
    return newerror,correctionalangle, integralgain