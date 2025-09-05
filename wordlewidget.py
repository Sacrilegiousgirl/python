#future improvements:
#add keyboard
#add animation maybe?

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDialog,
                             QLineEdit, QPushButton, QVBoxLayout, QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from exercises.wordlist_5_letters import words
import random

answer = random.choice(words)
solved = False

class Wordle(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("wordle.ui", self)
        self.setWindowTitle("Wordle")
        self.guesses = 0
        self.solved = False
        self.checkbutton.clicked.connect(self.checkanswer)

    def checkanswer(self):
        if self.guesses < 7:
            self.guess_words = []
            self.guess = self.inputword.text().strip().lower()
            if self.appropriate_input():
                self.error_message.setText("")
                self.guesses += 1
                for i in self.guess:
                    self.guess_words.append(i)
                self.show_hint()
        else:
            gameover = GameOver()
            widget.addWidget(gameover)
            widget.setCurrentIndex(widget.currentIndex() + 1)


    def appropriate_input(self):
        global words
        if not self.guess.isalpha():
            self.error_message.setText("Invalid input")
            return False
        elif len(self.guess) != 5:
            self.error_message.setText("You must type a 5-letter word")
            return False
        elif self.guess not in words:
            self.error_message.setText("This word doesnt exist in the dictionary!")
            return False
        else:
            return True
        
    def show_hint(self):
        self.hint = ["💩"] * 5 
        for x in range(5):
            if self.guess_words[x] in answer:
                self.hint[x] = "🟨"

        for i in range(5):
            if self.guess_words[i] == answer[i]:
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

        if self.hint == ["🟩","🟩","🟩","🟩","🟩"]:
            global solved
            solved = True
            gameover = GameOver()
            widget.addWidget(gameover)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        if self.hint != ["🟩","🟩","🟩","🟩","🟩"] and self.guesses == 6:
            gameover = GameOver()
            widget.addWidget(gameover)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class GameOver(QDialog):
    def __init__(self):
        global answer
        global solved
        super().__init__()
        loadUi("gameover.ui", self)
        widget.setGeometry(520, 300, 400, 300)
        self.answer_label.setText(answer.upper())
        if solved:
            self.result_label.setText("You Won!")
        else:
            self.result_label.setText("You Lost!")
        self.newgame_button.clicked.connect(self.start_new_game)
    
    def start_new_game(self):
        global solved
        global answer
        solved = False
        answer = random.choice(words)
        newgame = Wordle()
        widget.addWidget(newgame)
        widget.setGeometry(370, 150, 700, 600)
        widget.setCurrentIndex(widget.currentIndex()+1)
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Wordle()
    widget = QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setGeometry(370, 150, 700, 600)
    widget.show()
    sys.exit(app.exec_())

