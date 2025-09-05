import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog,
                             QLineEdit, QPushButton, QVBoxLayout, QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        print(f"Successfully logged in with email: {email} and password: {password}")

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAcc(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmpass.setEchoMode(QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text() and self.password.text() != "":
            password = self.password.text()
            print(f"Successfully logged in with email: {email} and password: {password}")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(480)
    widget.setFixedHeight(620)
    widget.show()
    sys.exit(app.exec_())
    