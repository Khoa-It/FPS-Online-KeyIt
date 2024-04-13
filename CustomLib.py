from ursina import *


def printInfo():
    print("Mouse position:", mouse.position)


def createMyCube(x, z, width, mycolor) -> Entity:
    return Entity(model='cube',
                  position=(x, width / 2, z),
                  collider='box',
                  scale=(width, width, width),
                  texture='brick',
                  color=mycolor
                  )


def createWall(x, z, width, height, mycolor=None, corner=0) -> Entity:
    return Entity(model='cube',
                  position=(x, height / 2, z),
                  collider='box',
                  scale=(width, height, 20),
                  texture='brick',
                  color=mycolor,
                  rotation_y=corner)


def createTree(x=0, z=0) -> Entity:
    return Entity(model='asset/static/tree/Tree.obj',
                  texture='asset/static/tree/tree2.jpeg',
                  position=(x, 1, z), colider='box',
                  color=color.rgb(1, 59, 14),
                  scale=(40, 40, 40),
                  )


def createHouse(x=0, z=0, corner=0) -> Entity:
    return Entity(
        model='asset/static/house/farmhouse.obj',
        position=(x, 1, z),
        texture='asset/static/house/Farmhouse Texture.jpg',
        scale=10,
        rotation_y=corner,
        collider='box',
    )

def moveObject(object):
    if not object:
        return
    if held_keys['a']:
        object.x-=.01
    if held_keys['d']:
        object.x+=.01
    if held_keys['w']:
        object.y+=.01
    if held_keys['s']:
        object.y-=.01
    if held_keys[Keys.up_arrow]:
        object.scale_y+=.01
    if held_keys[Keys.down_arrow]:
        object.scale_y-=.01
    if held_keys[Keys.left_arrow]:
        object.scale_x-=.01
    if held_keys[Keys.right_arrow]:
        object.scale_x+=.01
    if held_keys['space']:
        print('position',object.position)
        print('scale',object.scale)