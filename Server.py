import socket


class TheSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connection(self):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        while True:
            clientsocket, address = s.accept()
            clientsocket.send(bytes(,"utf-8"))
