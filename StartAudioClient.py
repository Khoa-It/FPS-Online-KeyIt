from networks.database import getIpServer
from networks.streamAudioClientUDP import AudioStreamClient

username = 'admin_gamebansung'
ip_server = getIpServer()
port_server = 4000
room = 1
AudioStreamClient(name=username, target_ip= ip_server, target_port= port_server, room= room)