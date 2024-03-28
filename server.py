from ursinanetworking import *
import sys
# server = UrsinaNetworkingServer('192.168.167.238', 6000)
import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

ip_address = get_ip_address()
print("IP Address:", ip_address)

try:
    server = UrsinaNetworkingServer('192.168.167.76', 6000)
except Exception as e:
    print("Error creating server:", e)
    sys.exit(1)
easy = EasyUrsinaNetworkingServer(server)
app = Ursina()
useractive = {}
messages = []
serverStatus = True
@server.event
def onClientConnected(Client):
    print(f"{Client.id} join game")
    Client.send_message('GetID', Client.id)
    useractive[Client.id] = {
        'name':Client.name,
        'position':(0,1,0),
    }
    server.broadcast('newPlayerLogin',
        {
            'id':Client.id,
            'name':Client.name,
            'position':(0,1,0),
        }                 
    )
    Client.send_message('syncMessage',messages)

@server.event
def onClientDisconnected(Client):
    print(f"{Client} leave game")

@server.event
def messageFromClient(Client,message):
    print(f"{message}")
    server.broadcast('newMessage',message)

def update():
    server.process_net_events()

app.run()



