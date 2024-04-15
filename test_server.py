from ursina import *
from CustomLib import *
from ipLibrary import *
from server import MyServer

app = Ursina()
my_ipv4 = get_ipv4_address()
# server = MyServer('192.168.1.7', 6000)
server = MyServer(my_ipv4, 6000)
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