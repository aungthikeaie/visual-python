from vpython import *
import numpy as np
import time

clockR = 2
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

secondHandL = clockR-majorL/2
secondHandT = minuteHandL/50
secondHandOffset = clockT*1.5+minuteHandT

hubRadius = clockT/2

for theta in np.linspace(0, 2*np.pi, 13):
    majorTick = box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), pos=vector((clockR-majorL/2)*np.cos(theta),(clockR-majorL/2)*np.sin(theta),0),length=majorL, height=majorT, width=majorW, color=color.black)

for theta in np.linspace(0, 2*np.pi, 61):
    minorTick = box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), pos=vector((clockR-minorL/2)*np.cos(theta),(clockR-minorL/2)*np.sin(theta),0),length=minorL, height=minorT, width=minorW, color=color.black)

clockFace = cylinder(axis=vector(0,0,1), pos=vector(0,0,-clockT/2), radius=clockR, length=clockT, color=vector(0, 1, 0.8))

minuteHand = arrow(axis=vector(1,0,0), pos=vector(0,0,minuteHandOffset), length=minuteHandL, shaftwidth=minuteHandT, color=color.red)

hourHand = arrow(axis=vector(0,1,0), pos=vector(0,0,hourHandOffset),length=hourHandL, shaftwidth=hourHandT, color=color.red)

secondHand = arrow(axis=vector(0,1,0), pos=vector(0,0,secondHandOffset), length=secondHandL, shaftwidth=secondHandT, color=color.red)

hub = cylinder(axis=vector(0,0,1), length=clockT*2, radius = hubRadius, color=color.red)

myLable = text(pos=vector(0,clockR*1.1,-clockT/2), text="Yangon Time", color=color.orange, height=clockR/4, align="center", depth=clockT)

hourAngle = np.pi/2
minuteAngle = np.pi/2
secondAngle = np.pi/2

while True:
    rate(5000)

    hour = time.localtime(time.time())[3]
    if hour>12:
        hour = hour-12
        
    minute = time.localtime(time.time())[4]
    second = time.localtime(time.time())[5]

    hourAngle = -((hour+minute/60)/12)*2*np.pi+np.pi/2
    minuteAngle = -((minute+second/60)/60)*2*np.pi+np.pi/2
    secondAngle = -(second/60)*2*np.pi+np.pi/2

    hourHand.axis = vector(hourHandL*np.cos(hourAngle), hourHandL*np.sin(hourAngle), 0)
    minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle), minuteHandL*np.sin(minuteAngle), 0)
    secondHand.axis = vector(secondHandL*np.cos(secondAngle), secondHandL*np.sin(secondAngle), 0)