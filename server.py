from ursinanetworking import *
app = Ursina()
server = UrsinaNetworkingServer('localhost', 3001)


@server.event
def onClientConnected(client):
    print(f"{client} join game")


@server.event
def onClientDisconnected(client):
    print(f"{client} leave game")


def update():
    server.process_net_events()


app.run()



