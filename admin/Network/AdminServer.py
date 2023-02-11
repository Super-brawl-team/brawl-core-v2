# Protocol: TCP network

import os
import json
import socket
import select
import urllib.request
from datetime import datetime
from Admins.Network.Protocol.Receiver import Receiver


class AdminServer:
    def __init__(self, start, off):
        self.start = start
        self.off = off
        self.addr = ("0.0.0.0", 9119)
        self.socket = socket.socket()
        self.socket.setblocking(0)
        self.inputs = {self.socket: None}
        self.adminlist = ["127.0.0.1"]
        self.whitelist = ["127.0.0.1"]
        self.tim = {}

    def disconnect(self, socket, addr):
        if socket in self.inputs:
            address = addr
            print(f"Disconnect from AdminServer! - " + address)
            socket.close()
            self.inputs.pop(socket)

    def start_server(self):
        if self.start:
            if self.off:
                print("AdminServer Off!")
            else:
                self.socket.bind(self.addr)
            self.socket.listen(3)
            print(f"Admin server started! To: {self.addr}.")
            while True:
                read_fds, write_fds, except_fds = select.select(self.inputs, [], self.inputs)  # [] - output
                for i in read_fds:
                    if i == self.socket:
                        client, addr = self.socket.accept()
                        client.setblocking(0)
                        # checker
                        if addr[0] not in self.whitelist:
                            url = "https://ipinfo.io/" + addr[0] + "/json"
                            upl = urllib.request.urlopen(url)
                            ip = json.load(upl)
                            print(f"[INFO] IP information: \n   {ip}   \n       Information END!")
                            if ip["bogon"]:
                                print(f"New connection from {addr[0]}:{addr[1]} to AdminServer @developer")
                                print("Dev IP - " + addr[0])
                            else:
                                if ip["country"] not in ["RU", "AZ", "KZ", "AM", "BY", "KG", "MD", "TJ", "UZ"]:
                                    print("War country: " + ip["country"] + " for IP - " + addr[0] + " @ban")
                                    os.system(
                                        f'sudo iptables -t filter -A INPUT -s {addr[0]} -j DROP && sudo netfilter-persistent save')
                                    socket.close()
                                    pass
                                else:
                                    print(f"New connection from {addr[0]}:{addr[1]} to AdminServer")
                            if addr[0] in self.adminlist:
                                print("Admin authorized!")
                                continue
                            else:
                                socket.close()
                                break
                        else:
                            print(f"New connection from {addr[0]}:{addr[1]} to AdminServer @white user")
                        # antiddos
                        print(f"{addr[0]} start checked!")
                        if addr[0] in self.tim:
                            print(f"{addr[0]} 45% checked!")
                            if int(datetime.timestamp(datetime.now())) - self.tim[addr[0]] < 3:
                                os.system(
                                    f'sudo iptables -t filter -A INPUT -s {addr[0]} -j DROP && sudo netfilter-persistent save')
                                socket.close()
                                print(f"{addr[0]} 100% checked! @ban")
                            else:
                                self.tim.update({addr[0]: int(datetime.timestamp(datetime.now()))})
                                print(f"{addr[0]} 100% checked! @normal")
                        else:
                            self.tim.update({addr[0]: int(datetime.timestamp(datetime.now()))})
                        # worker
                        self.inputs[client] = Receiver(client)
                    else:
                        if i in self.inputs:
                            try:
                                result = self.inputs[client].receive_message()
                                if result == -1:
                                    self.disconnect(i, self.addr[0])
                            except:
                                self.disconnect(i, self.addr[0])

    def morecloser(self):
        socket.close()
