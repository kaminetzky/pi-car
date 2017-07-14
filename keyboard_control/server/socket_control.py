import socket
from motors import Motors
import RPi.GPIO as GPIO

class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.client_socket = self.socket.accept()[0]
        Motors()
        self.listen()

    def listen(self):
        while True:
            data = self.client_socket.recv(1024)
            self.client_socket.send('ok'.encode('utf-8'))
            if not data:
                break
            self.process_request(data.decode('utf-8'))
        self.client_socket.close()

    @staticmethod
    def process_request(text):
        methods_dict = {'stop': Motors.stop,
                        'forward': Motors.forward,
                        'left': Motors.left,
                        'backwards': Motors.backwards,
                        'right': Motors.right}
        methods_dict[text]()

if __name__ == '__main__':
    host = ''
    port = 50000
    socket = Socket(host, port)
    GPIO.cleanup()