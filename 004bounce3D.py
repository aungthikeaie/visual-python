from vpython import *

roomThickness = .1
roomWidth = 12
roomHeight = 10
roomDepth = 15
mRadius = .5

ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth, roomThickness, roomDepth), color=color.white)
floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth, roomThickness, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth/2, 0, 0), size=vector(roomThickness, roomHeight, roomDepth), color=color.white)
leftWall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(roomThickness, roomHeight, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, roomThickness), color=color.white)
marble = sphere(radius=mRadius, color=color.red)

xPos = 0
yPos = 0
zPos = 0

deltaX = 0.1
deltaY = 0.1
deltaZ = 0.1

while True:
    rate(10)

    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ

    Xrme = xPos + mRadius
    Xlme = xPos - mRadius
    Ytme = yPos + mRadius
    Ybme = yPos - mRadius
    Zfme = zPos + mRadius
    Zbme = zPos - mRadius

    rwe = roomWidth/2 - roomThickness/2
    lwe = -roomWidth/2 + roomThickness/2
    cwe = roomHeight/2 - roomThickness/2
    floorwe = -roomHeight/2 + roomThickness/2
    frontwe = roomDepth/2 - roomThickness/2
    bwe = -roomDepth/2 + roomThickness/2

    if(Xrme >= rwe or Xlme <= lwe):
        deltaX = deltaX*(-1)

    if(Ytme >= cwe or Ybme <= floorwe):
        deltaY = deltaY*(-1)

    if(Zfme >= frontwe or Zbme <= bwe):
        deltaZ = deltaZ*(-1)

    marble.pos=vector(xPos, yPos, zPos)