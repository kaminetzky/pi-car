from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
import sys
from client_socket import Socket


class Widget(QWidget):
    def __init__(self, host, port):
        super().__init__()
        loadUi('client/widget.ui', self)
        self.connect_button.clicked.connect(self.connect)
        self.show()
        self.socket = Socket(host, port)
        self.connected = False

    def connect(self):
        if self.socket.connect():
            self.status_label.setText('Connected')
            self.connect_button.setEnabled(False)
            self.connected = True
        else:
            self.status_label.setText('Failed to connect')

    def keyPressEvent(self, QKeyEvent):
        if self.connected:
            text = QKeyEvent.text()
            methods_dict = {'w': self.socket.forward,
                            'a': self.socket.left,
                            's': self.socket.backwards,
                            'd': self.socket.right}
            print('text')
            methods_dict[text]()

    def keyReleaseEvent(self, QKeyEvent):
        if self.connected:
            text = QKeyEvent.text()
            if text in ['w', 'a', 's', 'd']:
                print('stop')
                self.socket.stop()


if __name__ == '__main__':
    host_ = 'raspberrypi'
    port_ = 50000
    app = QApplication(sys.argv)
    widget = Widget(host_, port_)
    sys.exit(app.exec_())
