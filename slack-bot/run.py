from PyQt5 import QtCore
from application import app
from PyQt5.QtCore import QThread, QObject
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                            QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QLabel,
                            QGroupBox, QTabWidget, QTableWidget, QTableWidgetItem,
                            QTableView, QListWidget, QListWidgetItem, QHBoxLayout,
                            QMessageBox)
import sys
from application import database
import os

class ServerThread(QThread):
    """
    Create a new thread to run the application
    """

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        """
        Run the application
        """
        self.app.run(debug=False, port=3000)


class MainGui(QWidget):
    """
    The gui
    """

    def __init__(self):
        super().__init__()

        self.thread = ServerThread(app)
        self.thread.start()

        self.initUi()

    def initUi(self):
        """Initialize the ui"""
        self.command_text_edit = QLineEdit()
        self.response_text_edit = QLineEdit()
        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.on_click)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Regex trigger"), self.command_text_edit)
        form_layout.addRow(QLabel("Response"), self.response_text_edit)
        form_layout.addRow(QLabel("Add to database"), insert_button)
        form_group_box = QGroupBox("Add a new bot trigger")
        form_group_box.setLayout(form_layout)

        self.trigger_table = None
        self.create_table()

        self.delete_table_button = QPushButton("Delete Row")
        self.delete_table_button.clicked.connect(self.delete_table)

        self.info_label = QLabel("")

        self.tabs = QTabWidget()

        self.triggers_layout = QVBoxLayout(self)

        if not os.environ.get("SLACK_OAUTH"):
            slack_oauth_info = QLabel("SLACK_OAUTH not found")
            self.triggers_layout.addWidget(slack_oauth_info)
        if not os.environ.get("BOT_OAUTH"):
            bot_oauth_info = QLabel("BOT_OAUTH not found")
            self.triggers_layout.addWidget(bot_oauth_info)

        self.triggers_layout.addWidget(form_group_box)
        self.triggers_layout.addWidget(self.info_label)

        self.triggers_tab = QWidget()
        self.triggers_tab.setLayout(self.triggers_layout)

        self.list_layout = QVBoxLayout(self)
        self.list_layout.addWidget(self.trigger_table)
        self.list_layout.addWidget(self.delete_table_button)

        self.list_tab = QWidget()
        self.list_tab.setLayout(self.list_layout)

        self.tabs.addTab(self.triggers_tab, "Set bot triggers")
        self.tabs.addTab(self.list_tab, "List bot triggers")
        self.tabs.move(0, 0)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)
        self.setGeometry(0, 0, 500, 800)
        self.setWindowTitle('Slack Bot')    
        self.show()

    @QtCore.pyqtSlot()
    def create_table(self):
        trigger_table = QTableWidget()
        trigger_table.setColumnCount(2)
        trigger_table.setRowCount(len(database.fetch_all_command_pairs().items()))

        for y_index, row in enumerate(database.fetch_all_command_pairs().items()):
            for x_index in range(0,2):
                trigger_table.setItem(y_index, x_index, QTableWidgetItem(row[x_index]))

        
        trigger_table.setHorizontalHeaderLabels(["Regex Trigger", "Response"])
        self.trigger_table = trigger_table

    @QtCore.pyqtSlot()
    def delete_table(self):
        current_row = self.trigger_table.currentRow()
        current_item = self.trigger_table.item(current_row, 0).text()
        database.delete_command(current_item)
        self.update_table()

    @QtCore.pyqtSlot()
    def update_table(self):
        y_index = self.trigger_table.columnCount()
        x_index = self.trigger_table.rowCount()

        self.trigger_table.setColumnCount(2)
        self.trigger_table.setRowCount(len(database.fetch_all_command_pairs().items()))

        for y_index, row in enumerate(database.fetch_all_command_pairs().items()):
            for x_index in range(0,2):
                self.trigger_table.setItem(y_index, x_index, QTableWidgetItem(row[x_index]))

        
        self.trigger_table.setHorizontalHeaderLabels(["Regex Trigger", "Response"])

    @QtCore.pyqtSlot()
    def on_click(self):
        command_text = self.command_text_edit.text()
        response_text = self.response_text_edit.text()
        print("{} -> {}".format(command_text, response_text))
        if database.insert_command(command_text, response_text):
            self.info_label.setText("Added trigger {} to database".format(command_text))
        else:
            self.info_label.setText("That trigger already exists in the database")
        self.command_text_edit.clear()
        self.response_text_edit.clear()
        self.update_table()

if __name__ == '__main__':
    gui = QApplication(sys.argv)
    w = MainGui()
    sys.exit(gui.exec_())
