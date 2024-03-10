from ursina import *
from Map import Map
from CustomLib import *


def input(key):
    global map, step
    if key == 'w':
        map.creativeCube.z += step
    if key == 's':
        map.creativeCube.z -= step
    if key == 'a':
        map.creativeCube.x -= step
    if key == 'd':
        map.creativeCube.x += step
    if key =='space':
        print("cube:","{",f"'x':{map.creativeCube.x}, 'height':20, 'z':{map.creativeCube.z}, 'color':color.green","},")
        print("wall:","{",f"'x':{map.creativeCube.x}, 'height':80, 'width':150, 'z':{map.creativeCube.z}, 'color':color.rgb(128, 49, 4), 'corner':0 ", "},")
        print("tree:", "{",f"'x':{map.creativeCube.x}, 'z':{map.creativeCube.z}", "},")
        print("house:", "{", f"'x':{map.creativeCube.x}, 'z':{map.creativeCube.z}, 'corner':0", "},")
        print("building:",
              "{",
              f"'x':{map.creativeCube.x-60}, 'height':80*2, 'width':150*2, 'z':{map.creativeCube.z+200}, 'color':color.rgb(145, 117, 6), 'corner':0 ",
              "},",
              "{",
              f"'x':{map.creativeCube.x+200},'height':80*2, 'width':150*3, 'z':{map.creativeCube.z-60}, 'color':color.rgb(145, 117, 6), 'corner':90 ",
              "},",
              "{",
              f"'x':{map.creativeCube.x}, 'height':80*2, 'width':150*2+100, 'z':{map.creativeCube.z-260}, 'color':color.rgb(145, 117, 6), 'corner':0 ",
              "},",
              "{",
              f"'x':{map.creativeCube.x-200}, 'height':80*2, 'width':150*2, 'z':{map.creativeCube.z+50}, 'color':color.rgb(145, 117, 6), 'corner':90 ",
              "},",
              )
    


app = Ursina()
map = Map()
step = 20
EditorCamera()
camera.z = -25
app.run()
