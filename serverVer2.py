from ursinanetworking import *

server = UrsinaNetworkingServer('localhost', 3010)
easy = EasyUrsinaNetworkingServer(server)
app = Ursina()
useractive = {}
messages = []
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



