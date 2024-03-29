from ursinanetworking import *
from ChatMessage import ChatMessage
from Userform import Userform

class MyClient:
    def __init__(self, ip, port , main_callback):
        self.ip = ip
        self.port = port
        self.main_callback = main_callback
        self.player_info = {
            'seftID' : -1,
            'username' : 'khoa',
        }
        self.client = UrsinaNetworkingClient(self.ip,self.port)
        self.easy = EasyUrsinaNetworkingClient(self.client)
        self.chatMessage = ChatMessage(username='client anonymous')
        self.usform = Userform([self.updateUsername , *self.main_callback])
        
        @self.client.event
        def GetID(content):
            self.player_info['seftID'] = content
            print('recieve id player: ', self.player_info['seftID'])
        
        @self.client.event
        def newPlayerLogin(content):
            print(content)
            pass
        
        @self.client.event
        def newMessage(content):
            print(content)
            self.chatMessage.addNewMessage(contentMessage=content['message'], usermes=content['username'])
            pass
        
    def updateUsername(self,name):
        self.player_info['username'] = name
        self.chatMessage.inputText.y = -.43
        
    def input(self,key):
        if key == Keys.enter:
            if self.chatMessage.inputText.text != '':
                self.client.send_message('messageFromClient',
                                    {
                                        'username': self.player_info['username'],
                                        'message': self.chatMessage.inputText.text
                                    }
                )
    
        
