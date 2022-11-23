from vpython import *

cyl1 = cylinder(radius=1, color=color.orange, length=6)
cyl2 = cylinder(radius=1, color=color.cyan, length=6, pos=vector(0,3,0))

cyanDelta = 0.02
orangeDelta = 0.01

cyanLen = 1
orangeLen = 1

while True:
    rate(100)
    cyanLen = cyanLen + cyanDelta
    orangeLen = orangeLen + orangeDelta

    cyl2.length = cyanLen
    cyl1.length = orangeLen

    if cyanLen >= 6 or cyanLen <=0.1:
        cyanDelta = cyanDelta*(-1)
    if orangeLen >=6 or orangeLen <=0.1:
        orangeDelta = orangeDelta*(-1)