
def getmass(initmass,phase):#conditions for mass
    sleevemass = 0.1
    if phase == 1:
        initmass =initmass-0.000157894736842
        #print("hello")
        return initmass
    if phase==4:
        initmass=initmass-sleevemass
    return initmass
    if phase==5:
        initmass=initmass-0.000157894736842
        return initmass
    if phase==6:
        return initmass
def getthrust(phase,thrust):#the thrust of the rocket
    if phase==0 or phase==2 or phase==3 or phase==6:
        return 0
    if (phase==1 or phase==4 or phase==5)and thrust==0:
        return 7.4
    if (phase==1 or phase==4 or phase==5)and thrust==7.8:
        return 26
    if phase==1 or phase==4 or phase==5:
        return 14.8