import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog,
                             QLineEdit, QPushButton, QVBoxLayout, QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from exercises.wordlist_5_letters import words
import random


class Wordle(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("wordle.ui", self)
        self.setWindowTitle("Wordle")
        self.guesses = 0
        # self.answer = random.choice(words)
        self.answer = "apple"
        self.checkbutton.clicked.connect(self.checkanswer)

    def checkanswer(self):
        self.guess_words = []
        self.guess = self.inputword.text().strip().lower()
        if self.appropriate_input(self.guess, words):
            self.guesses += 1
            for i in self.guess:
                self.guess_words.append(i)
            print(self.guess_words)
            print(self.guesses)
            self.show_hint()

    @staticmethod
    def appropriate_input(guess, words):
        if not guess.isalpha():
            print("Invalid input")
            return False
        elif len(guess) != 5:
            print("You must type a 5-letter word")
            return False
        elif guess not in words:
            print("This word doesnt exist in the dictionary!")
            return False
        else:
            return True
        
    def show_hint(self):
        self.hint = ["💩"] * 5 
        for x in range(5):
            if self.guess_words[x] in self.answer:
                self.hint[x] = "🟨"

        for i in range(5):
            if self.guess_words[i] == self.answer[i]:
                self.hint[i] = "🟩"

        match self.guesses:
            case 1:
                labels = [self.b1, self.b2, self.b3, self.b4, self.b5]
            case 2:
                labels = [self.b6, self.b7, self.b8, self.b9, self.b10]
            case 3: 
                labels = [self.b11, self.b12, self.b13, self.b14, self.b15]
            case 4:
                labels = [self.b16, self.b17, self.b18, self.b19, self.b20]
            case 5:
                labels = [self.b21, self.b22, self.b23, self.b24, self.b25]
            case 6:
                labels = [self.b26, self.b27, self.b28, self.b29, self.b30]
        

        # Define colors
        colors = {
            "🟩": "rgb(0, 144, 81)",     # green
            "🟨": "rgb(200,182,83)",     # yellow
            "💩": "rgb(122,124,127)"     # gray/default
        }

        # Apply styles + set text
        for i in range(5):
            bg = colors[self.hint[i]]
            labels[i].setStyleSheet(f"""
                background-color: {bg};
                color: rgb(255, 255, 255);
                font-size: 30px;
            """)
            labels[i].setText(self.guess_words[i].upper())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Wordle()
    mainwindow.show()
    sys.exit(app.exec_())

