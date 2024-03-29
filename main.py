from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from CustomLib import *
from OtherPlayer import OtherPlayer
from client import MyClient
from player import Player
from Map import Map

def create_player():
    global player, otherplayer
    player = Player(Vec3(0,3,0))
    Audio('asset/static/sound_effect/getready.ogg').play()
    otherplayer = OtherPlayer(Vec3(0,3,0))
def hello():
    print('hello world')


app = Ursina()
my_client = MyClient('192.168.1.6',6000, [create_player, hello])
Sky()
my_map = Map()
player = None
otherplayer = None

def input(key):
    if key == Keys.escape:
        exit(0)

def update():
    global my_client
    my_client.client.process_net_events()

app.run()
