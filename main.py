from venv import create
from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from modules.ChatMessage import ChatMessage
from helpers.CustomLib import *
from modules.OtherPlayer import OtherPlayer
from Userform import Userform
from networks.client import MyClient
from modules.player import Player
from data.Map import Map

def create_player():
    global player
    player = Player(Vec3(0,3,0))
    Audio('asset/static/sound_effect/getready.ogg').play()
    
def get_player_position():
    global player
    if player:
        return player.world_position
    return Vec3(0,0,0)

def create_client(username):
    global my_client
    my_client = MyClient(username,'192.168.1.6',6000, [create_player, get_player_position])

app = Ursina()
my_client = None
Userform([create_client])

Sky()
my_map = Map()
player = None
otherplayer = None
listOtherPlayers = []
def input(key):
    if key == Keys.escape:
        exit(0)

def update():
    global my_client
    if my_client:
        my_client.client.process_net_events()
        my_client.easy.process_net_events()
    
def input(key):
    global my_client
    if my_client:
        my_client.input(key)
    if key == 'm':
        print('main - player pos:',get_player_position())

app.run()
