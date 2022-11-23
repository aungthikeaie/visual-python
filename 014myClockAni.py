from vpython import *
import numpy as np

clockR = 1
clockT = clockR/10

majorL = clockR/7
majorT = 2*np.pi*clockR/400
majorW = clockT*1.2

minorL = clockR/12
minorT = 2*np.pi*clockR/600
minorW = clockT*1.2

minuteHandL = clockR-majorL
minuteHandT = minuteHandL/25
minuteHandOffset = clockT/2+minuteHandT

hourHandL = 0.75*minuteHandL
hourHandT = minuteHandT*1.25
hourHandOffset = clockT+hourHandT

hubRadius = clockT/2

for theta in np.linspace(0, 2*np.pi, 13):
    majorTick = box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), pos=vector((clockR-majorL/2)*np.cos(theta),(clockR-majorL/2)*np.sin(theta),0),length=majorL, height=majorT, width=majorW, color=color.black)

for theta in np.linspace(0, 2*np.pi, 61):
    minorTick = box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), pos=vector((clockR-minorL/2)*np.cos(theta),(clockR-minorL/2)*np.sin(theta),0),length=minorL, height=minorT, width=minorW, color=color.black)

clockFace = cylinder(axis=vector(0,0,1), pos=vector(0,0,-clockT/2), radius=clockR, length=clockT, color=vector(0, 1, 0.8))

minuteHand = arrow(axis=vector(1,0,0), pos=vector(0,0,minuteHandOffset), length=minuteHandL, shaftwidth=minuteHandT, color=color.red)

hourHand = arrow(axis=vector(0,1,0), pos=vector(0,0,hourHandOffset),length=hourHandL, shaftwidth=hourHandT, color=color.red)

hub = cylinder(axis=vector(0,0,1), length=clockT*2, radius = hubRadius, color=color.red)

hourAngle = np.pi/2
minuteAngle = np.pi/2

minuteInc = 0.01
hourInc = minuteInc/12

while True:
    rate(50)

    hourAngle = hourAngle - hourInc
    minuteAngle = minuteAngle - minuteInc

    hourHand.axis = vector(hourHandL*np.cos(hourAngle), hourHandL*np.sin(hourAngle), 0)
    minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle), minuteHandL*np.sin(minuteAngle), 0)