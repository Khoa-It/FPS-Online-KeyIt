from ursinanetworking import easyursinanetworking
from ursinanetworking import *
from twisted.internet.protocol import DatagramProtocol
import pyaudio
from data.RandomPosition import playerRandomPositions
# server = UrsinaNetworkingServer('192.168.167.238', 6000)
class MyServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.start_server = True
        self.update_server = False
        self.server = None
        self.easy = None
        self.user_active = {}
        self.messages = []
        self.notifycation = None
        self.notifycation_content = None
        self.audioPort = 3000
        self.numberOfPlayers = 0

    def handle(self):
        if self.start_server:
            self.server = UrsinaNetworkingServer(self.ip, self.port)
            self.easy = easyursinanetworking.EasyUrsinaNetworkingServer(self.server)
            # self.notifycation = Text(f"this is server with ip address: {self.ip}", position=Vec3(-0.25, 0.45, 0))
            # self.notifycation_content = Text("=========Log content============", position=Vec3(-0.85, 0.4, 0))

            # @self.server.event
            # def onClientConnected(Client):
            #     print(f"{Client.id} join game")
            #     self.numberOfPlayers += 1
            #     # self.notifycation_content.text += "\n" + f"{Client.id} join game"
            #     self.easy.create_replicated_variable(Client.id,
            #             {"id": Client.id,
            #              'position': (0,3.5,0),
            #              'rotation': (0,0,0),
            #              'status': 'stand',
            #              'audioPort': self.audioPort,
            #              }
            #              )
            #     Client.send_message('GetID', Client.id)
            #     Client.send_message('initAudioPort', self.audioPort)
            #     self.server.broadcast('newPlayerLogin',
            #         {
            #             'id':Client.id,
            #             'name':Client.name,
            #             'position':(0,3.5,0),
            #             'port': self.audioPort,
            #         }
            #     )
            #     Client.send_message('syncMessage',self.messages)
            #     self.audioPort += 1
            #     print('check easy', self.easy.replicated_variables)

            @self.server.event
            def onClientConnected(Client):
                print(f"{Client.id} join game")
                self.numberOfPlayers += 1
                
                start_position = playerRandomPositions[Client.id]  # Gán vị trí ngẫu nhiên dựa vào ID

                self.easy.create_replicated_variable(Client.id,
                    {
                        "id": Client.id,
                        'position': start_position,  # Cập nhật vị trí mới
                        'rotation': (0,0,0),
                        'status': 'stand',
                        'audioPort': self.audioPort,
                    }
                )
                Client.send_message('GetID', Client.id)  # Gửi ID về client
                Client.send_message('updatePosition', start_position)  # Gửi vị trí mới về client
                Client.send_message('initAudioPort', self.audioPort)

                # Gửi toàn bộ danh sách người chơi hiện tại cho client mới
                for player_id, data in self.easy.replicated_variables.items():
                    Client.send_message('newPlayerLogin', data)

                self.server.broadcast('newPlayerLogin',
                    {
                        'id': Client.id,
                        'name': Client.name,
                        'position': start_position,
                        'port': self.audioPort,
                    }
                )
                Client.send_message('syncMessage', self.messages)
                self.audioPort += 1
                print('check easy', self.easy.replicated_variables)

            @self.server.event
            def onClientDisconnected(Client):
                print(f"{Client} leave game")
                # self.notifycation_content.text += "\n" + f"{Client.id} leave game"
                self.easy.remove_replicated_variable_by_name(Client.id)
                self.server.broadcast('existedClientDisConnected', Client.id)

            @self.server.event
            def messageFromClient(Client,message):
                print(f"{message}")
                # self.notifycation_content.text += "\n" + f"chatmessage feature: {message}"
                self.server.broadcast('newMessage',message)

            @self.server.event
            def updatePosition(Client,content):
                # print('server recieved position:', content)
                self.easy.update_replicated_variable_by_name(Client.id, 'position', content)

            @self.server.event
            def updateRotation(Client,content):
                # print('server recieved rotation:', content)
                self.easy.update_replicated_variable_by_name(Client.id,'rotation',content)

            @self.server.event
            def updateStatus(Client,content):
                # print('server recieved status:', content)
                self.easy.update_replicated_variable_by_name(Client.id,'status',content)

            @self.server.event
            def clientShooting(Client,content):
                print('server recieved client shooting signal:', content)
                self.server.broadcast('bulletFromOtherPlayer',{
                    'id':Client.id,
                    'position':content['position'],
                    'direction':content['direction'],
                })

            @self.server.event
            def player_shot(Client, content):
                print('server recieved player shot signal:', content)
                self.server.broadcast('decrease_hp', content)
            
            @self.server.event
            def checkPlayerSurvival(Client, content):
                print('function checkPlayerSurvival from server')
                self.numberOfPlayers -=1
                if self.numberOfPlayers == 1:
                    self.server.broadcast('endGame', {'id': Client.id})
            
            @self.server.event
            def openOtherVoiceChat(Client, content):
                print(content)
                self.server.broadcast('hearFromOtherClient', content)
                
            @self.server.event
            def stopOtherVoiceChat(Client, content):
                print(content)
                self.server.broadcast('stopHearFromOtherClient', content)


            self.start_server = False
            self.update_server = True


    def input(self,key):
        if held_keys[ 'w']:
            self.notifycation_content.y += .05
        if held_keys['s']:
            self.notifycation_content.y -=.05
        if held_keys[ 'a']:
            self.notifycation_content.x -=.05
        if held_keys[ 'd']:
            self.notifycation_content.x +=.05
        if key =='space':
            print(self.notifycation_content.position)
            

