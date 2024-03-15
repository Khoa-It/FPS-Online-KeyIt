from ursinanetworking import *
app = Ursina()
client = UrsinaNetworkingClient('localhost',3001)
@client.event
def onConnectionEtablished():
    print('Client connected')


@client.event
def onConnectionError(reason):
    print(f'Error connection | error: {reason}')

def update():
    client.process_net_events()

app.run()
