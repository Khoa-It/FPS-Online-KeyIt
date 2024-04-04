from ursinanetworking import *
from Bullet import Bullet
from ChatMessage import ChatMessage
from OtherBullet import OtherBullet
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
        self.player = Player(Vec3(0,3.5,0), [self.sendSignalShooting, self.printPosOfOtherPlayer, self.getListOtherPlayers, self.getIdPlayers])
        self.pos = (0,0,0)
        self.other_bullet:list[OtherBullet] = []
        self.time_start = time.time()
        Audio('asset/static/sound_effect/getready.ogg').play()
        
        @self.client.event
        def GetID(content):
            self.player_info['id'] = content
            # print('recieve id player: ', self.player_info['id'])
            # print('-------ndk log amount of player-------') 
            
            for item in self.easy.replicated_variables:
                # print(item)
                self.list_other_players.append(OtherPlayer((0,3.5,0)))
            self.list_other_players[content].logout()
            # print(self.otherbullet)
            
        
        @self.client.event
        def newPlayerLogin(content):
            # print('-------ndk log new user login-------')
            # print(content)
            if content['id'] != self.player_info['id']:
                self.list_other_players.append(OtherPlayer((0,3.5,0)))
                
            
        
        @self.client.event
        def newMessage(content):
            # print(content)
            self.chatMessage.addNewMessage(contentMessage=content['message'], usermes=content['username'])
            pass
        
        @self.client.event
        def existedClientDisConnected(idPlayerLogout):
            # print('----------ndk log - Existed client disconnect----')
            # print('removed id:', idPlayerLogout)
            self.list_other_players[idPlayerLogout].logout()
            
        @self.client.event
        def bulletFromOtherPlayer(content):
            # print('----------ndk log - other player shooting:', content)
            if content['id'] != self.player_info['id']:
                self.other_bullet.append(OtherBullet(pos=content['position']+(0,40,0), direction=content['direction'])) 
                # print('vi tri nguoi ban:', self.list_other_players[content['id']].getPos())
                # self.otherbullet.shoot()
            
        @self.easy.event
        def onReplicatedVariableCreated(Content):
            # print('-------ndk log new syn var created-------')
            # print(Content)
            pass
        
        @self.easy.event
        def onReplicatedVariableUpdated(Content):
            # print('-------ndk log one syn var updated-------')
            # print(Content)
            if Content.content['id'] != self.player_info['id']:
                self.list_other_players[Content.content['id']].setPos(Content.content['position'])
                self.list_other_players[Content.content['id']].setRot(Content.content['rotation'])
                if Content.content['status'] == 'stand':
                    self.list_other_players[Content.content['id']].stand()
                else:
                    self.list_other_players[Content.content['id']].running()

        
        @self.easy.event
        def onReplicatedVariableRemoved(Content):    
            # print('-------ndk log one syn var remove-------')
            # print(Content)
            pass
        
    def updateUsername(self,name):
        self.player_info['username'] = name
        self.chatMessage.inputText.y = -.43
      
    def sendSignalShooting(self, position, direction):
          self.client.send_message('clientShooting', {
              'position': position,
              'direction': direction
          })
    def printPosOfOtherPlayer(self, hitEntity):
        print('---------function: printPosOfOtherPlayer - client.py-------------')
        count = 0
        for item in self.list_other_players:
            if count != self.player_info['id']:
                if hitEntity == item.character.stand_entity or hitEntity == item.character.running_entity:
                    print('ban trung nguoi choi :', count)
                print('vi tri nguoi choi khac la: ',item.getPos())
            count+=1
            
    def getListOtherPlayers(self):
        return list(filter(lambda x: self.list_other_players.index(x) != self.player_info['id'], self.list_other_players))
    
    def getIdPlayers(self):
        return self.player_info['id']
        
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
        
            
                
    
        
