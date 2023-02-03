import math
def getcorrectionalange(randerror,olderror,integralgain):#getting the correctional angle
        gain = 0.5 * randerror
        deltagain = ( randerror-olderror / 1) * 0.2
        integralgain = integralgain+((randerror) * 0.1)
        correctionalangle =gain + integralgain + deltagain
        newerror = randerror - correctionalangle
        return correctionalangle,integralgain
t=0
while t!=10:
