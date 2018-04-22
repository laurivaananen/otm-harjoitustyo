from application import app
from PyQt5.QtCore import QThread, QObject
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton
import sys

class ServerThread(QThread):

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        self.app.run(debug=False, port=3000)

class MainGui(QWidget):

    def __init__(self):
        super().__init__()
        # QMainWindow.__init__(self)

        self.thread = ServerThread(app)
        self.thread.start()

        self.initUi()

    def initUi(self):
        button = QPushButton("Hello")
        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(button)

        self.setLayout(vbox)
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Slack Bot')    
        self.show()



if __name__ == '__main__':
    gui = QApplication(sys.argv)
    w = MainGui()
    # w.show()
    sys.exit(gui.exec_())

    

    

    