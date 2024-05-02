from random import randint, random

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import pyaudio


class StreamAudio(DatagramProtocol):
    def __init__(self, otherAudio:list) -> None:
        super().__init__()
        self.otherAudio = otherAudio
        
    def startProtocol(self):
        py_audio = pyaudio.PyAudio()
        self.buffer = 1024  # 127.0.0.1
        # self.another_client = input("Write address: "), int(input("Write port: "))
        # self.otherAudio = [('127.0.0.1', 3000), ('127.0.0.1', 5000)]
        self.output_stream = py_audio.open(format=pyaudio.paInt16,
                                           output=True, rate=44100, channels=2,
                                           frames_per_buffer=self.buffer)
        self.input_stream = py_audio.open(format=pyaudio.paInt16,
                                          input=True, rate=44100, channels=2,
                                          frames_per_buffer=self.buffer)
        reactor.callInThread(self.record)

    def record(self):
        while True:
            for other in self.otherAudio:
                data = self.input_stream.read(self.buffer)
                self.transport.write(data, other)

    def datagramReceived(self, datagram, addr):
        self.output_stream.write(datagram)


