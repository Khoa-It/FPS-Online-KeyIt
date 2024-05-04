from helpers.ipLibrary import get_ipv4_address
from networks.database import setIpServer
from networks.streamAudioServerUDP import StreamAudioServer


ipAudioServer = get_ipv4_address()
setIpServer(ipAudioServer)
portAudioServer = 4000
audioServer = StreamAudioServer(ip= ipAudioServer, port=portAudioServer)