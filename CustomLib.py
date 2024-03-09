from ursina import *


def printInfo():
    print("Mouse position:",mouse.position)


def createMyCube(x, z, width, mycolor) -> Entity:
    return Entity(model='cube', position=(x,width/2,z), collider='box', scale=(width, width, width), texture='brick', color=mycolor)


def createWall(x,z,width,height, mycolor=None, corner = 0) -> Entity:
    return Entity(model='cube', position=(x,height/2,z), collider='box', scale=(width, height, 20), texture='brick', color=mycolor, rotation_y = corner)

