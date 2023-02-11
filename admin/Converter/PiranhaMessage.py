# PiranhaMessage.py

from Admins.DataStream.ByteStream import ByteStream
from Admins.DataStream.BitStream import BitStream


class PiranhaMessage:
    def __init__(self):
        self.id = 0
        self.version = 0
        self.byter = ByteStream()
        self.biter = BitStream()


    def encode(self):
        pass

    def decode(self):
        pass

    def deobfuscation(self):
        pass

    def process(self, con):
        pass
