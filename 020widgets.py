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

run = 0
mSpeed = 1

scene.append_to_caption("\n")

def ballColorRed(x):
    marble.color = color.red

button(bind=ballColorRed, text="Red", color=color.black, background=color.red)

def ballColorBlue(x):
    marble.color= color.blue

button(bind=ballColorBlue, text="Blue", color=color.black, background=color.blue)

def ballColorGreen(x):
    marble.color = color.green

button(bind=ballColorGreen, text="Green", color=color.black, background=color.green)

scene.append_to_caption("\n\n")

def runRadio(x):
    global run
    if x.checked == True:
        run = 1
    if x.checked == False:
        run = 0

radio(bind=runRadio, text="Run")

scene.append_to_caption("    ")

def bigBall(x):
    global mRadius
    if x.checked == True:
        mRadius = mRadius*2
        marble.radius = mRadius
    if x.checked == False:
        mRadius = mRadius/2
        marble.radius = mRadius

checkbox(bind=bigBall, text="Big Ball")

scene.append_to_caption("    ")

wtext(text="Choose Ball Speed")
scene.append_to_caption(" ")

def speed(x):
    global mSpeed
    if x.selected == "1":
        mSpeed = 1
    if x.selected == "2":
        mSpeed = 2
    if x.selected == "3":
        mSpeed = 3
    if x.selected == "4":
        mSpeed = 4
    if x.selected == "5":
        mSpeed = 5

menu(bind=speed, choices=["1","2","3","4","5"])

scene.append_to_caption("\n\n")

def ballOpacity(x):
    opacity = x.value
    marble.opacity = opacity

wtext(text="Choose Ball Opacity")
scene.append_to_caption("\n\n")
slider(bind=ballOpacity, min=0, max=1, value=1, vertical=False)

while True:
    rate(10)

    xPos = xPos + deltaX*run*mSpeed
    yPos = yPos + deltaY*run*mSpeed
    zPos = zPos + deltaZ*run*mSpeed

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