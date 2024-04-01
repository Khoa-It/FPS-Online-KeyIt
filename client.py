from ursinanetworking import *
from ChatMessage import ChatMessage
from OtherPlayer import OtherPlayer
from Userform import Userform
from player import Player

class MyClient:
    def __init__(self, username, ip, port ):
        self.ip = ip
        self.port = port
        self.list_other_players:list[OtherPlayer] = []
        self.player_info = {
            'id' : -1,
            'username' : username,
        }
        self.client = UrsinaNetworkingClient(self.ip,self.port)
        self.easy = EasyUrsinaNetworkingClient(self.client)
        self.chatMessage = ChatMessage(username)
        self.player = Player(Vec3(0,3.5,0))
        Audio('asset/static/sound_effect/getready.ogg').play()
        
        @self.client.event
        def GetID(content):
            self.player_info['id'] = content
            print('recieve id player: ', self.player_info['id'])
            print('-------ndk log amount of player-------') 
            
            for item in self.easy.replicated_variables:
                print(item)
                self.list_other_players.append(OtherPlayer((0,3.5,0)))
            self.list_other_players[content].logout()
            
        
        @self.client.event
        def newPlayerLogin(content):
            print('-------ndk log new user login-------')
            print(content)
            if content['id'] != self.player_info['id']:
                self.list_other_players.append(OtherPlayer((0,3.5,0)))
            
        
        @self.client.event
        def newMessage(content):
            print(content)
            self.chatMessage.addNewMessage(contentMessage=content['message'], usermes=content['username'])
            pass
        @self.client.event
        def existedClientDisConnected(idPlayerLogout):
            print('----------ndk log - Existed client disconnect----')
            print('removed id:', idPlayerLogout)
            self.list_other_players[idPlayerLogout].logout()
            
        @self.easy.event
        def onReplicatedVariableCreated(Content):
            print('-------ndk log new syn var created-------')
            print(Content)
        
        @self.easy.event
        def onReplicatedVariableUpdated(Content):
            print('-------ndk log one syn var updated-------')
            print(Content)
            if Content.content['id'] != self.player_info['id']:
                print('owwwwww')
                self.list_other_players[Content.content['id']].setPos(Content.content['position'])
                self.list_other_players[Content.content['id']].setRot(Content.content['rotation'])
                if Content.content['status'] == 'stand':
                    self.list_other_players[Content.content['id']].stand()
                else:
                    self.list_other_players[Content.content['id']].running()

        
        @self.easy.event
        def onReplicatedVariableRemoved(Content):    
            print('-------ndk log one syn var remove-------')
            print(Content)
        
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
        if held_keys['a'] or held_keys['s'] or held_keys['d'] or held_keys['w']:
            self.client.send_message('updatePosition',self.player.model.world_position)
            self.client.send_message('updateRotation', self.player.model.world_rotation)
            self.client.send_message('updateStatus', 'running')
        if not held_keys['a'] and not held_keys['s'] and not held_keys['d'] and not held_keys['w']:
            self.client.send_message('updateStatus', 'stand')
        
            

        
    
        
