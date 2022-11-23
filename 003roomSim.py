from vpython import *

roomThickness = 1
roomWidth = 15
roomHeight = 8
roomDepth = 12
mRadius = 2

ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth, roomThickness, roomDepth), color=color.white)
floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth, roomThickness, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth/2, 0, 0), size=vector(roomThickness, roomHeight, roomDepth), color=color.white)
leftWall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(roomThickness, roomHeight, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, roomThickness), color=color.white)
marble = sphere(radius=mRadius, color=color.red)

xPos = 0
DeltaX = 0.1

while True:
    rate(10)
    xPos = xPos + DeltaX
    if ( xPos>=(roomWidth/2-(roomThickness/2+mRadius)) or xPos<=(-roomWidth/2+(roomThickness/2+mRadius)) ):
        DeltaX = DeltaX*(-1)

    
    marble.pos=vector(xPos, 0, 0)