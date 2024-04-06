from ursina import *

from CustomLib import moveObject
from Map import Map
from OtherPlayer import OtherPlayer
from player import Player

app = Ursina()
Map()
other = OtherPlayer((10,0,10))
sphere = Entity(model = 'sphere', scale = 10, collider = 'sphere', color = color.black)
sphere.position = Vec3(-1, 48, -42)
EditorCamera()

def input(key):
    global sphere, other
    moveObject(sphere)
def update():
    global sphere, other
    hit_info = sphere.intersects()
    if hit_info.hit:
        destroy(sphere)
        print('va cham voi vat the tai vi tri: ', hit_info.entity.position)
        print('vi tri nguoi choi la: ', other.getPos())
app.run()