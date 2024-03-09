from ursina import *
from Map import Map
from CustomLib import *


def input(key):
    global map, step
    if key == 'w':
        map.listWallCube[0].z += step
    if key == 's':
        map.listWallCube[0].z -= step
    if key == 'a':
        map.listWallCube[0].x -= step
    if key == 'd':
        map.listWallCube[0].x += step
    if key =='space':
        print("cube:","{",f"'x':{map.listWallCube[0].x}, 'height':20, 'z':{map.listWallCube[0].z}, 'color':color.green","},")
        print("wall:","{",f"'x':{map.listWallCube[0].x}, 'height':80, 'width':150, 'z':{map.listWallCube[0].z}, 'color':color.rgb(128, 49, 4), 'corner':0 ", "},")
    


app = Ursina()
map = Map()
step = 20
EditorCamera()
camera.z = -25
app.run()
