# ServerHelloMessage.py

from Admins.Converter.PiranhaMessage import PiranhaMessage

class ServerHelloMessage(PiranhaMessage):
    def __init__(self):
        super().__init__()
        self.id = 20100

    def encode(self):
        self.byter.writeInt(24)  # session key
        for i in range(24):
            self.byter.writeByte(1)