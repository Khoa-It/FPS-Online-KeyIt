from ursina import *


def printInfo():
    print("Mouse position:",mouse.position)


def createWallCube(pos, height=5):
    Entity(model='cube', position=pos, collider='box', scale=(20, height, 20), texture='brick', color=color.gray)

# create a value random a value between 10 and 80
