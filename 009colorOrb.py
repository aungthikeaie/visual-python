from vpython import *

myOrb = sphere(radius=1, color=color.white)

rChan = 0
gChan = 0
bChan = 0

rInc = 0.001
gInc = 0.002
bInc = 0.0015

while True:
    rate(500)

    rChan = rChan + rInc
    gChan = gChan + gInc
    bChan = bChan + bInc

    myOrb.color =  vector(rChan, gChan, bChan)

    if rChan >= 1 or rChan <= 0:
        rInc = rInc*(-1)
    if gChan >=1  or gChan <= 0:
        gInc = gInc*(-1)
    if bChan >= 1 or bChan <= 0:
        bChan = bChan*(-1)