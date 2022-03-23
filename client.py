from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400,400)
        self.label1 = QLabel("Host ip", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label2 = QLabel("API_key:", self)
        self.label2.move(10,60)
        self.text2 = QLineEdit(self)
        self.text2.move(10,80)
        self.label3 = QLabel("IP", self)
        self.label3.move(10,100)
        self.text3 = QLineEdit(self)
        self.text3.move(10,130)
        self.button = QPushButton("send", self)
        self.button.move(10,150)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        api_key =self.text.text()
        ip = self.text.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()
        
        if api_key == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res1 = self.__query(api_key)
            if res1:
                self.label2.setText("Answer%s" % (res1["Hello"]))
                self.label2.adjustSize()
                self.show()

        if ip == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res2 = self.__query(ip)
            if res2:
                self.label2.setText("Answer%s" % (res2["Hello"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
