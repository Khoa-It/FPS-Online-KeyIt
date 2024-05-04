from ursina import *
from helpers.CustomLib import *
from helpers.ipLibrary import *
from networks.database import setIpServer
from networks.server import MyServer

# app = Ursina()

my_ipv4 = get_ipv4_address()
# server = MyServer('localhost', 6000)
setIpServer(my_ipv4)
server = MyServer(my_ipv4, 6000)
# def input(key):
#     if key == Keys.escape:
#         exit(0)
def update():
    global server
    while 1:
        server.handle()
        if server.update_server == True:
            server.server.process_net_events()
            server.easy.process_net_events()
        
update()
# app.run()