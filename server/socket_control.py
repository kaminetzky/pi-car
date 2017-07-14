import socket
#import motors


class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.client_socket = self.socket.accept()[0]
        self.listen()

    def listen(self):
        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            self.process_request(data.decode('utf-8'))
        self.client_socket.close()

    @staticmethod
    def process_request(text):
        print(text)
        return
        methods_dict = {'stop': motors.stop,
                        'forward': motors.forward,
                        'left': motors.left,
                        'backwards': motors.backwards,
                        'right': motors.right}
        methods_dict[text]()

if __name__ == '__main__':
    host = ''
    port = 50000
    socket = Socket(host, port)