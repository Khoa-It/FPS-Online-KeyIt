from ursinanetworking import *

from ChatMessage import ChatMessage
from Userform import Userform

# ######################
client = UrsinaNetworkingClient('localhost',3002)
easy = EasyUrsinaNetworkingClient(client)
app = Ursina()
seftID = -1
username = 'khoa'
chatMessage = ChatMessage(username='khoa')
def updateUsername(name):
    global username, chatMessage
    username = name
    chatMessage.inputText.y = -.43

usform = Userform(updateUsername)



@client.event
def GetID(content):
    global seftID
    seftID = content
    print('recieve id player: ', seftID)

@client.event
def newPlayerLogin(content):
    print(content)
    pass

@client.event
def newMessage(content):
    print(content)
    chatMessage.addNewMessage(contentMessage=content['message'], usermes=content['username'])
    pass

def update():
    global chatMessage
    client.process_net_events()
    chatMessage.scrollcustom()

def input(key):
    global chatMessage, username
    if key == Keys.enter:
        if chatMessage.inputText.text != '':
            client.send_message('messageFromClient',
                                {
                                    'username': username,
                                    'message': chatMessage.inputText.text
                                }
            )
    

app.run()
