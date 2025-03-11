from turtle import position
from ursinanetworking import *
from ursina import *
from modules.Bullet import Bullet
from modules.ChatMessage import ChatMessage
from modules.OtherBullet import OtherBullet
from modules.OtherPlayer import OtherPlayer
# from Userform import Userform
from modules.player import Player
from twisted.internet import reactor
from data.RandomPosition import *
import pyaudio
import threading

from networks.streamAudioClientUDP import AudioStreamClient


class MyClient:
    def __init__(self, username, ip, port , start_position):
        self.isStreaming = False
        self.audioStreamClient = None
        self.startStreamThread = None
        self.stopStreamThread = None
        self.otherAudioPorts = []
        self.result = None
        self.ip = ip
        self.port = port
        self.list_other_players:list[OtherPlayer] = []
        self.player_info = {
            'id' : -1,
            'username' : username,
        }
        self.start_position = start_position
        self.client = UrsinaNetworkingClient(self.ip,self.port)
        self.easy = EasyUrsinaNetworkingClient(self.client)
        self.chatMessage = ChatMessage(username)
        self.player = Player(position= self.start_position, clientCallback= [self.sendSignalShooting, self.printPosOfOtherPlayer, self.getListOtherPlayers, self.getIdPlayers, self.check_player_shot], ignorePosition= self.start_position)
        self.other_bullet:list[OtherBullet] = []
        self.time_start = time.time()
        Audio('asset/static/sound_effect/getready.ogg').play()
        
        @self.client.event
        def GetID(content):
            self.player_info['id'] = content
            self.player.position = playerRandomPositions[int(content)]
            self.nickname = Text(
                text=f'uid: {self.player_info['id']} - {self.player_info['username']}',
                parent = camera.ui,
                position = Vec3(-0.15,0.42,0),
                scale = 1.5,
                color = color.rgb(62, 92, 176),
                )
            self.client.send_message('updatePosition',playerRandomPositions[int(content)])
        # Cập nhật danh sách người chơi khác
            for item in self.easy.replicated_variables:
                if int(item) != self.player_info['id']:  # Không tạo model trùng với chính mình
                    other_player = OtherPlayer(item, Vec3(0, 3.5, 0))
                    other_player.setPos(self.easy.replicated_variables[item].content['position'])
                    self.list_other_players.append(other_player)   
            self.list_other_players[content].logout()
            
        
            
        # @self.client.event
        # def newPlayerLogin(content):
        #     # print('-------ndk log new user login-------')
        #     # print(content)
        #     if content['id'] != self.player_info['id']:
        #         self.list_other_players.append(OtherPlayer(content['id'], Vec3(0,3.5,0)))

        @self.client.event
        def newPlayerLogin(data):
            player_id = data['id']
            position = data['position']

            if player_id in self.list_other_players:
                print(f"⚠️ Người chơi {player_id} đã tồn tại!")
                return

            # Kiểm tra nếu dữ liệu hợp lệ
            if position is None:
                print(f"❌ Lỗi: Dữ liệu vị trí của {player_id} không hợp lệ!")
                return

            # Tạo người chơi mới
            new_player = OtherPlayer(player_id, position)
            self.list_other_players[player_id] = new_player  

            print(f"✅ Đã tạo người chơi mới: {player_id} tại vị trí {position}")
 
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
        @self.client.event
        def decrease_hp(content):
            if content == self.player_info['id']:
                self.player.healthbar.value -= 20
        
        @self.client.event
        def hearFromOtherClient(content):
            print(content)
            # self.openVoiceChat()
        
        @self.client.event
        def stopHearFromOtherClient(content):
            print(content)
            self.stopVoiceChat()
        
        self.endGameMessage = None   
        self.allowRestartGame = False
        @self.client.event
        def endGame(content):
            print(content)
            self.allowRestartGame = True
            self.result = content
            if content['id'] == self.player_info['id']:
                self.endGameMessage = Text(
                    text='Victory', 
                    style = 'bold', 
                    parent = camera.ui,
                    position = Vec3(-0.595996, 0.136, 0),
                    scale = Vec3(13.9, 10.6, 5),
                    color = color.rgb(231, 245, 32),
                    )
                Audio('asset/static/sound_effect/victory.mp3').play()
            else:
                self.endGameMessage = Text(
                    text='Defeat',  
                    style = 'bold',
                    parent = camera.ui,
                    position = Vec3(-0.595996, 0.136, 0),
                    scale = Vec3(13.9, 10.6, 5),
                    color = color.rgb(57, 45, 89),
                    )
                Audio('asset/static/sound_effect/defeat.mp3').play()
            
                
        
        @self.easy.event
        def onReplicatedVariableCreated(Content):
            # print('-------ndk log new syn var created-------')
            # print(Content)
            pass
        
        # @self.easy.event
        # def onReplicatedVariableUpdated(Content):
        #     # print('-------ndk log one syn var updated-------')
        #     # print(Content)
        #     if Content.content['id'] != self.player_info['id']:
        #         print(f"Nhận vị trí mới từ server: {Content.content['id']} - {Content.content['position']}")
        #         self.list_other_players[Content.content['id']].setPos(Content.content['position'])
        #         self.list_other_players[Content.content['id']].setRot(Content.content['rotation'])
        #         if Content.content['status'] == 'stand':
        #             self.list_other_players[Content.content['id']].stand()
        #         else:
        #             self.list_other_players[Content.content['id']].running()

        @self.easy.event
        def onReplicatedVariableUpdated(Content):
            player_id = Content.content['id']
            
            # Kiểm tra xem player_id có trong danh sách chưa
            if player_id not in self.list_other_players:
                print(f"⚠️ ID {player_id} chưa tồn tại trong danh sách! Tạo mới...")
                self.list_other_players[player_id] = OtherPlayer(player_id, Vec3(0,3.5,0))

            print(f"Nhận vị trí mới từ server: {player_id} - {Content.content['position']}")

            # Cập nhật vị trí, xoay và trạng thái
            self.list_other_players[player_id].setPos(Content.content['position'])
            self.list_other_players[player_id].setRot(Content.content['rotation'])
            
            if Content.content['status'] == 'stand':
                self.list_other_players[player_id].stand()
            else:
                self.list_other_players[player_id].running()

     
        @self.easy.event
        def onReplicatedVariableRemoved(Content):    
            # print('-------ndk log one syn var remove-------')
            # print(Content)
            pass

    
    def resetGame(self, content):
        self.list_other_players[int(content['id'])].logout()
        self.list_other_players = []
        for item in self.easy.replicated_variables:
            self.list_other_players.append(OtherPlayer(item,Vec3(0,3.5,0)))
            self.list_other_players[int(item)].setPos(playerRandomPositions[int(item)])
        self.list_other_players[int(self.player_info['id'])].logout()
        if content['id'] != self.player_info['id']:
            self.player.healthbar.value = 100
            self.player.ndk_revival()
        else:
            self.player.position = playerRandomPositions[int(self.player_info['id'])]
    def updateUsername(self,name):
        self.player_info['username'] = name
        self.chatMessage.inputText.y = -.43
      
    def sendSignalShooting(self, position, direction):
          self.client.send_message('clientShooting', {
              'position': position,
              'direction': direction
          })
    def printPosOfOtherPlayer(self):
        print('---------function: printPosOfOtherPlayer - client.py-------------')
        count = 0
        for item in self.list_other_players:
            if count != self.player_info['id']:
                print('vi tri nguoi choi khac la: ',item.pos)
            count+=1
            
    def check_player_shot(self, bullet_pos):
        count = 0
        for item in self.list_other_players:
            if count != self.player_info['id']:
                if item.pos == bullet_pos:
                    item.healthbar.value -= 20
                    self.client.send_message('player_shot',count)
                    print('nguoi choi bi tru mau co id:', count)
                    print('so mau con lai cua nguoi choi la:', item.healthbar.value)
                    if item.healthbar.value <= 0:
                        self.client.send_message('checkPlayerSurvival', 'reset')
                        item.logout()
            count += 1
                            
    def getListOtherPlayers(self):
        return list(filter(lambda x: self.list_other_players.index(x) != self.player_info['id'], self.list_other_players))
    
    def getIdPlayers(self):
        return self.player_info['id']
        
    def input(self,key):
        
        if key == Keys.enter:
            if self.chatMessage.inputText.position == Vec3(0, -1, 0):
                self.chatMessage.inputText.position = Vec3(0, -0.43, 0)
                self.player.disable()
                self.chatMessage.inputText.active=True
                
            if self.chatMessage.inputText.text != '' and self.chatMessage.inputText.position == Vec3(0, -0.43, 0):
                self.client.send_message('messageFromClient',
                                    {
                                        'username': self.player_info['username'],
                                        'message': self.chatMessage.inputText.text
                                    }
                )
                self.chatMessage.inputText.position = Vec3(0, -1, 0)
                self.chatMessage.inputText.active=False
                self.player.enable()
        if held_keys['a'] or held_keys['s'] or held_keys['d'] or held_keys['w']:
            self.client.send_message('updatePosition',self.player.model.world_position)
            self.client.send_message('updateRotation', self.player.model.world_rotation)
            self.client.send_message('updateStatus', 'running')
        if not held_keys['a'] and not held_keys['s'] and not held_keys['d'] and not held_keys['w']:
            self.client.send_message('updateStatus', 'stand')
            
        if key == '0':
            self.startStreamThread = threading.Thread(target=self.openVoiceChat)
            self.startStreamThread.start()
                
        if key == '9':
            self.stopStreamThread = threading.Thread(target=self.stopVoiceChat)
            self.stopStreamThread.start()
            # self.startStreamThread.join()
            # self.stopStreamThread.join()
        if key == 'home':
            if self.allowRestartGame:
                destroy(self.endGameMessage)
                self.resetGame(self.result)
                self.allowRestartGame = False
            
    def openVoiceChat(self):
        if not self.isStreaming:
            username = self.player_info['username']
            ip_server = self.ip
            port_server = 4000
            room = 1
            self.audioStreamClient = AudioStreamClient(name=username, target_ip= ip_server, target_port= port_server, room= room)
            self.isStreaming = True    
        
        
    def stopVoiceChat(self):
        if self.isStreaming:
            # self.audioStreamClient.connected = False
            # self.audioStreamClient.stop_audio()
            # self.isStreaming = False
            self.startStreamThread.terminate()
            self.stopStreamThread.terminate()
                
    
        
