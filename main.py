from ursina import *
from Map import Map
from CustomLib import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player

app = Ursina()
count_loop = 0
Sky()
my_map = Map()
player = Player(Vec3(0,3,0))
Audio('asset/static/sound_effect/getready.ogg').play()

def input(key):
    if key == Keys.escape:
        exit(0)


    

app.run()
