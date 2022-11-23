from vpython import *

ceiling = box(pos=vector(0, 5, 0), color=color.white, length=10, height=.1, width=10)
leftWall = box(pos=vector(-5, 0, 0), color=color.white, length=.1, height=10, width=10)
rightWall = box(pos=vector(5, 0, 0), color=color.white, length=.1, height=10, width=10)
backWall = box(pos=vector(0, 0, -5), color=color.white, length=10, height=10, width=.1)
floor = box(pos=vector(0, -5, 0), color=color.white, length=10, height=.1, width=10)
marble = sphere(color=color.red, radius=.75)

while True:
    pass