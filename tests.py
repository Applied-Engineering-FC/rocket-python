def getthrustcontrol(thrust,altitude,speed,mass,timeo,timeA0,time):
    thrustpercentage=0
    timeleftinburn=360-timeo
    if timeleftinburn<=0:
        return 1
    if speed>2.5 or speed<-2.5:
        return 1
    if altitude <= 0:
        return 1
    if thrust==0:
        return 1
    if thrust<0:
        return 0
    #if -0.2 < speed < 0.2:
    if 0<altitude<15:
        timetillcrash=getA0time(mass,thrust,speed,altitude,time)
        print(timetillcrash)
        if speed>0:
            acceleration=speed/(timetillcrash/100)
        if speed<=0:
            acceleration=(-speed)/(timetillcrash/100)
        neededthrust=(acceleration*mass)+mass*9.81
        thrustpercentage=neededthrust/thrust
        return thrustpercentage
