# Receiver.py

from Admins.Network.Protocol.Sender import Sender
from Admins.Converter.FindMessage import FindMessage

class Receiver:
    def __init__(self, sock):
        self.socket = sock
        self.messaging = Sender(self)

    def send(self, buffer):
        self.socket.send(buffer)

    def receive_message(self):
        try:
            header = self.socket.recv(7)
            if len(header) > 0:
                message_type, length, version = Sender.readHeader(header)
                payload = self.socket.recv(length)
                print(f"Received message {message_type}, length {length} @normal")
                message = FindMessage.convert(message_type)
                if message != None:
                    message.stream.buffer = payload
                    message.decode()
                    message.process(self)
                return 0
        except:
            return -1
