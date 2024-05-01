from ursina import *

from helpers.CustomLib import createMyCube, moveObject
from data.Map import Map
from modules.OtherPlayer import OtherPlayer
from modules.player import Player

app = Ursina()
Map()
Player()
window.borderless = False


def input(key):
    
    pass
def update():
    global my_cube
    moveObject(my_cube)
    pass

app.run()