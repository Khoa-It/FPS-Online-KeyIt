from ursina import *

from CustomLib import createMyCube, moveObject
from Map import Map
from OtherPlayer import OtherPlayer
from player import Player

app = Ursina()
Map()
my_cube = createMyCube(0,0,20, color.red)
EditorCamera()
window.borderless = False


def input(key):
    
    pass
def update():
    global my_cube
    moveObject(my_cube)
    pass

app.run()