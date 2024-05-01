from random import randint, random

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import pyaudio

myport = 5000
class StreamAudio(DatagramProtocol):
    portAudio = myport
    def startProtocol(self):
        py_audio = pyaudio.PyAudio()
        self.buffer = 1024  # 127.0.0.1
        # self.another_client = input("Write address: "), int(input("Write port: "))
        self.another_clients = [('127.0.0.1', 3000), ('127.0.0.1', 4000)]
        self.output_stream = py_audio.open(format=pyaudio.paInt16,
                                           output=True, rate=44100, channels=2,
                                           frames_per_buffer=self.buffer)
        self.input_stream = py_audio.open(format=pyaudio.paInt16,
                                          input=True, rate=44100, channels=2,
                                          frames_per_buffer=self.buffer)
        reactor.callInThread(self.record)

    def record(self):
        while True:
            for another_client in self.another_clients:
                data = self.input_stream.read(self.buffer)
                self.transport.write(data, another_client)

    def datagramReceived(self, datagram, addr):
        self.output_stream.write(datagram)


reactor.listenUDP(myport, StreamAudio())
reactor.run()

