from venv import create
from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from ChatMessage import ChatMessage
from CustomLib import *
from OtherPlayer import OtherPlayer
from Userform import Userform
from client import MyClient
from player import Player
from Map import Map



def create_client(username):
    global my_client
    my_client = MyClient(username,'192.168.1.6',6000)

app = Ursina()
my_client = None
Userform([create_client])
Sky()
my_map = Map()

def input(key):
    if key == Keys.escape:
        exit(0)

def update():
    global my_client
    if my_client:
        my_client.client.process_net_events()
        my_client.easy.process_net_events()
        if len(my_client.other_bullet) > 0:
            for bullet in my_client.other_bullet:
                bullet.update()
        
            
            
        
    
def input(key):
    global my_client
    if my_client:
        my_client.input(key)

app.run()
