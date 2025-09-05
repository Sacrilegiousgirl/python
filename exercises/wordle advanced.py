import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WordleGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.row1_label = QLabel("🟩🟩🟩🟩🟩", self)
    def initUI(self):
        self.setWindowTitle("Wordle Game")
