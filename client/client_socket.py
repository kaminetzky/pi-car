import socket


class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
        except ConnectionRefusedError:
            return False
        else:
            return True

    def stop(self):
        self.client_socket.send('stop'.encode('utf-8'))

    def forward(self):
        self.client_socket.send('forward'.encode('utf-8'))

    def backwards(self):
        self.client_socket.send('backwards'.encode('utf-8'))

    def left(self):
        self.client_socket.send('left'.encode('utf-8'))

    def right(self):
        self.client_socket.send('right'.encode('utf-8'))
