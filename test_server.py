from typing import Self
from ursina import *
from Map import Map
from CustomLib import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player
from server import MyServer

app = Ursina()
# server = MyServer('192.168.1.7', 6000)
server = MyServer('localhost', 6000)

# Sky()
# my_map = Map()
# player = Player(Vec3(0,3,0))
# Audio('asset/static/sound_effect/getready.ogg').play()

def input(key):
    if key == Keys.escape:
        exit(0)
def update():
    global server
    server.handle()
    if server.update_server == True:
        server.server.process_net_events()
        server.easy.process_net_events()
    

    

app.run()