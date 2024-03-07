from ursina import *
from Map import Map
from CustomLib import *


def input(key):
    if key == 'left mouse down':
        printInfo()


app = Ursina()
Map()
EditorCamera()
camera.z = -25
app.run()
