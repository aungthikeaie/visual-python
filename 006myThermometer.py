from vpython import *
import numpy as np

glassBulb = sphere(radius=1.25, color = color.white, opacity=0.3)
glassCyl = cylinder(radius=0.65, length=6, color = color.white, opacity=0.3)
mercSphere = sphere(radius=1, color=color.red)
mercColumn = cylinder(radius=0.45, length=6, color=color.red)
for tick in np.linspace(1, 6, 15):
    box(pos=vector(tick, 0, 0.5), size=vector(0.05, 0.5, 0.25), color=color.white)
while True:
    for myTemp in np.linspace(1, 6, 100):
        rate(25)
        mercColumn.length = myTemp

    for myTemp in np.linspace(6, 1, 100):
        rate(25)
        mercColumn.length = myTemp
