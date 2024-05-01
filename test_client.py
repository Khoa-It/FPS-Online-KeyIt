from ursina import *
from helpers.CustomLib import *
from Login import LoginForm
from networks.client import MyClient
from data.Map import Map


def create_client(username):
    global my_client
    my_client = MyClient(username,'localhost',6000, Vec3(0,1.4,0))
    # my_client = MyClient(username,'localhost',6000, Vec3(-39, 10, 10))
    # my_client = MyClient(username,'192.168.1.7',6000, Vec3(0,1.4,0))
    # my_client = MyClient(username, ip, 6000, Vec3(0, 1.4, 0))


app = Ursina()
# window.title = 'FPS online keyit'
# window.fullscreen = False
# window.borderless = False
# window.exit_button.visible = True
# window.show_ursina_splash = True
# window.size = (650, 600)
my_client = None
Sky()
my_map = Map()
LoginForm([create_client])


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
        my_client.chatMessage.scrollcustom()
        # my_client.update()


def input(key):
    global my_client
    if my_client:
        my_client.input(key)


app.run()