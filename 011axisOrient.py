from vpython import *
import numpy as np

arrowL = 2
arrowT = 0.02

xArrow = arrow(axis=vector(1,0,0), color=color.red, length=arrowL, shaftwidth=arrowT)
yArrow = arrow(axis=vector(0,1,0), color=color.green, length=arrowL, shaftwidth=arrowT)
zArrow = arrow(axis=vector(0,0,1), color=color.blue, length=arrowL, shaftwidth=arrowT)

theta = 0

pntArrow = arrow(axis=vector(arrowL*np.cos(theta), arrowL*np.sin(theta), 0), color=color.orange, length=arrowL, shaftwidth=arrowT)

flag = 0

# while True:
#     for theta in np.linspace(0, 2*np.pi, 1000):
#         rate(50)
#         pntArrow.axis = vector(arrowL*np.cos(theta), arrowL*np.sin(theta), 0)
#         pntArrow.length = arrowL

while True:
    if flag%3 == 0:
        for theta in np.linspace(0, 2*np.pi, 1000):
            rate(150)
            pntArrow.axis = vector(arrowL*np.cos(theta), arrowL*np.sin(theta), 0)
            pntArrow.length = arrowL

    if flag%3 == 1:
        for theta in np.linspace(0, 2*np.pi, 1000):
            rate(150)
            pntArrow.axis = vector(arrowL*np.sin(theta), 0,arrowL*np.cos(theta))
            pntArrow.length = arrowL

    if flag%3 == 2:
        for theta in np.linspace(0, 2*np.pi, 1000):
            rate(150)
            pntArrow.axis = vector(0, arrowL*np.cos(theta), arrowL*np.sin(theta))
            pntArrow.length = arrowL

    flag =flag + 1
    
