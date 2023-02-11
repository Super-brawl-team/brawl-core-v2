# ClientHelloMessage.py

from Admins.Converter.PiranhaMessage import PiranhaMessage
from Admins.Converter.Messaging.Server.ServerHelloMessage import ServerHelloMessage


class ClientHelloMessage(PiranhaMessage):
    def __init__(self):
        super().__init__()
        self.id = 10100

    def decode(self):
        pass

    def process(self, con):
        con.messaging.send(ServerHelloMessage())
