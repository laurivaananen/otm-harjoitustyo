from application import app
from PyQt5.QtCore import QThread, QObject
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QLabel, QGroupBox
import sys
from application import database

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
        self.command_text_edit = QLineEdit()
        self.response_text_edit = QLineEdit()
        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.on_click)

        

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Regex command"), self.command_text_edit)
        form_layout.addRow(QLabel("Response"), self.response_text_edit)
        form_layout.addRow(QLabel("Add to database"), insert_button)
        form_group_box = QGroupBox("Add a new command")
        form_group_box.setLayout(form_layout)

        self.info_label = QLabel("")


        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(QLabel("Haa"))
        vbox.addWidget(form_group_box)
        vbox.addWidget(self.info_label)

        

        self.setLayout(vbox)
        self.setGeometry(0, 0, 300, 200)
        self.setWindowTitle('Slack Bot')    
        self.show()

    @QtCore.pyqtSlot()
    def on_click(self):
        command_text = self.command_text_edit.text()
        response_text = self.response_text_edit.text()
        print("{} -> {}".format(command_text, response_text))
        self.info_label.setText("Added command {} to database".format(command_text))
        database.insert_command(command_text, response_text)
        self.command_text_edit.clear()
        self.response_text_edit.clear()
        print(database.fetch_all_command_pairs())



if __name__ == '__main__':
    gui = QApplication(sys.argv)
    w = MainGui()
    # w.show()
    sys.exit(gui.exec_())

    

    

    